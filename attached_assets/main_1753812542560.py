from app import app

if __name__ == '__main__':
    # Flask will automatically use port 5000 by default
    app.run(host='0.0.0.0', port=5000, debug=True)
