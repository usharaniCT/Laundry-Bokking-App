from flask import render_template, request, redirect, url_for, session, flash
from app import app, db
from models import Booking, User

@app.route('/')
def dashboard():
    user = session.get('user_id')
    return render_template('dashboard.html', user=user)

@app.route('/student_login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('Please enter both username and password.', 'error')
            return redirect(url_for('student_login'))

        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('book'))
        else:
            flash('Invalid credentials. Please try again.', 'error')
            return redirect(url_for('student_login'))

    return render_template('student_login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if not username or not email or not phone or not password or not confirm_password:
            flash('All fields are required.', 'error')
            return redirect(url_for('register'))

        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return redirect(url_for('register'))

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose another.', 'error')
            return redirect(url_for('register'))

        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash('Email already exists. Please use another email address.', 'error')
            return redirect(url_for('register'))

        new_user = User()
        new_user.username = username
        new_user.email = email
        new_user.phone = phone
        new_user.password = password
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. You can now log in.', 'success')
        return redirect(url_for('student_login'))

    return render_template('register.html')

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Simple admin credentials check
        if username == 'admin' and password == 'admin123':
            session['admin'] = username
            flash("Admin login successful.", 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash("Invalid admin credentials.", 'error')
            return render_template('admin_login.html')

    return render_template('admin_login.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    if 'admin' not in session:
        flash("Please login as admin.", 'error')
        return redirect(url_for('admin_login'))

    bookings = Booking.query.order_by(Booking.id.desc()).all()
    return render_template('admin_dashboard.html', bookings=bookings)

@app.route('/update_status/<int:booking_id>/<status>')
def update_status(booking_id, status):
    if 'admin' not in session:
        flash("Unauthorized access.", 'error')
        return redirect(url_for('admin_login'))
    
    booking = Booking.query.get(booking_id)
    if booking:
        booking.status = status
        db.session.commit()
        flash(f'Booking status updated to {status}', 'success')
    else:
        flash('Booking not found.', 'error')
    return redirect(url_for('admin_dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('dashboard'))

@app.route('/book', methods=['GET', 'POST'])
def book():
    if 'user_id' not in session:
        flash('Please log in to book a slot.', 'error')
        return redirect(url_for('student_login'))
    
    if request.method == 'POST':
        student_name = request.form['student_name']
        room_no = request.form['room_no']
        date = request.form['date']
        time = request.form['time']
        cloth_type = request.form['cloth_type']
        wash_type = request.form['wash_type']
        payment_method = request.form['payment_method']

        # Validate required fields
        if not all([student_name, room_no, date, time, cloth_type, wash_type, payment_method]):
            flash("All fields are required.", 'error')
            return redirect(url_for('book'))

        # Prevent duplicate booking for the same date/time
        existing = Booking.query.filter_by(date=date, time=time).first()
        if existing:
            flash("This slot is already booked. Please choose another time.", 'error')
            return redirect(url_for('book'))

        booking = Booking()
        booking.student_name = student_name
        booking.room_no = room_no
        booking.date = date
        booking.time = time
        booking.cloth_type = cloth_type
        booking.clothes = cloth_type  # For compatibility with existing code
        booking.wash_type = wash_type
        booking.payment_method = payment_method
        booking.payment_status = "Unpaid"
        booking.status = "Pending"

        db.session.add(booking)
        db.session.commit()

        flash("Booking submitted. Please proceed to payment to confirm.", 'success')
        return redirect(url_for('payment', booking_id=booking.id))

    return render_template('book.html')

@app.route('/payment/<int:booking_id>', methods=['GET', 'POST'])
def payment(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    
    if request.method == 'POST':
        # For cash payments, confirm immediately
        if booking.payment_method == 'Cash':
            booking.payment_status = "Paid"
            booking.status = "Confirmed"
            db.session.commit()
            flash("Booking confirmed! Please bring exact cash amount during your time slot.", 'success')
        else:
            # For online payments (UPI, Online, Card), simulate payment verification
            # In a real system, this would integrate with actual payment gateway APIs
            booking.payment_status = "Paid"
            booking.status = "Confirmed"
            db.session.commit()
            flash("Payment successful! Your booking is confirmed. You will receive confirmation shortly.", 'success')
        
        return redirect(url_for('history', student_name=booking.student_name))

    return render_template('payment.html', booking=booking)

@app.route('/history/<student_name>')
def history(student_name):
    if 'user_id' not in session:
        flash('Please log in to view your booking history.', 'error')
        return redirect(url_for('student_login'))
    
    bookings = Booking.query.filter_by(student_name=student_name).order_by(Booking.id.desc()).all()
    return render_template('history.html', bookings=bookings, student_name=student_name)

@app.route('/help')
def help():
    return render_template('help.html')
