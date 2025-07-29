# SRIT Laundry Booking System

A comprehensive Flask-based web application for managing laundry bookings in SRIT Autonomous educational institution. The system provides seamless booking management, payment processing, and administrative oversight.

## Features

### For Students
- **User Registration & Authentication**: Secure account creation and login system
- **Real-time Slot Booking**: Book available laundry time slots from 6 AM to 10 PM
- **Multiple Wash Options**: Choose from Regular, Delicate, Heavy Duty wash types
- **Flexible Payment Methods**: Support for Cash, UPI (PhonePe, Google Pay), Credit/Debit Cards
- **Booking History**: Track all past and current bookings with detailed status
- **Interactive Chatbot**: Get instant help and support through the built-in chat assistant
- **Quick Stats Dashboard**: View available slots, active bookings, and queue status

### For Administrators
- **Comprehensive Dashboard**: Manage all student bookings from a centralized interface
- **Booking Management**: Confirm, cancel, or modify student bookings
- **Payment Tracking**: Monitor payment status and method preferences
- **Statistical Insights**: Real-time analytics on booking patterns and system usage
- **Admin Chatbot**: Specialized assistant for management tasks and insights
- **Student Management**: Oversee user accounts and booking behavior

## Technology Stack

- **Backend**: Flask 3.0.0 with Python
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Frontend**: Bootstrap 5 with responsive design
- **Authentication**: Session-based user management
- **Payment Integration**: UPI QR code support
- **Deployment**: Gunicorn WSGI server

## System Architecture

### Database Models
- **User Model**: Student account information (username, email, phone, password)
- **Booking Model**: Laundry reservations with scheduling and payment details

### Key Components
- **Authentication System**: Secure login/logout with session management
- **Booking Engine**: Time slot management with conflict prevention
- **Payment Processing**: Multiple payment method integration
- **Admin Interface**: Comprehensive management dashboard
- **Real-time Features**: Live status updates and notifications

## Installation & Setup

### Prerequisites
- Python 3.8+
- PostgreSQL database
- pip package manager

### Environment Variables
Configure the following environment variables:
```
DATABASE_URL=postgresql://username:password@localhost/database_name
SESSION_SECRET=your-secret-key-here
```

### Running the Application
1. Install dependencies using the package manager
2. Set up PostgreSQL database
3. Configure environment variables
4. Start the application:
   ```bash
   gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
   ```

### Package Dependencies
- Flask & Flask-SQLAlchemy for web framework and ORM
- psycopg2-binary for PostgreSQL connectivity
- Werkzeug for security utilities
- email-validator for form validation
- gunicorn for production deployment

## Usage

### For Students
1. **Registration**: Create an account with username, email, and phone
2. **Login**: Access your dashboard with credentials
3. **Booking**: Select preferred time slot, wash type, and payment method
4. **Payment**: Complete payment through UPI, card, or cash
5. **History**: View all booking details and status updates

### For Administrators
1. **Admin Login**: Access administrative interface
2. **Dashboard**: View all student bookings in organized table format
3. **Management**: Confirm, cancel, or modify bookings as needed
4. **Analytics**: Monitor system usage and payment patterns
5. **Support**: Use admin chatbot for management insights

## Features Overview

### Modern UI Elements
- Gradient color schemes matching SRIT branding
- Responsive card-based layouts
- Real-time status indicators with animations
- Interactive notification badges
- Smooth hover effects and transitions

### Payment Integration
- **UPI Support**: PhonePe (6300622975@ibl) and Google Pay (thippeswamyusha58@okicici)
- **QR Code Scanning**: Integrated payment QR codes
- **Payment Verification**: Simulated payment confirmation process
- **Status Tracking**: Real-time payment status updates

### Chatbot Assistance
- **Student Chatbot**: General help with booking, payments, and schedules
- **Admin Chatbot**: Management insights, statistics, and operational guidance
- **Smart Responses**: Context-aware answers based on user queries
- **24/7 Availability**: Always accessible support system

## System Status

The application includes real-time system monitoring with:
- Live server status indicator in navigation
- Booking availability counters
- Queue status monitoring
- Payment success rate tracking

## Security Features

- Session-based authentication
- Environment variable configuration
- Proxy support for deployment
- Database connection pooling
- Input validation and sanitization

## Branding

The system features complete SRIT Autonomous branding:
- Official SRIT logo integration
- Institutional color scheme
- Professional footer with autonomy designation
- Consistent branding across all pages

## Support

For technical support or system issues:
- Use the integrated chatbot for immediate assistance
- Contact system administrators through the platform
- Access help documentation within the application

## Development

### Project Structure
```
├── main.py              # Application entry point
├── app.py               # Flask application configuration
├── models.py            # Database models
├── routes.py            # URL routing and view functions
├── templates/           # HTML templates
├── static/             # CSS, JavaScript, and images
└── README.md           # This file
```

### Contributing
- Follow existing code style and conventions
- Update documentation for new features
- Test thoroughly before deployment
- Maintain responsive design principles

---

**SRIT Autonomous** - Advanced Laundry Management System  
*Streamlining campus life through technology*