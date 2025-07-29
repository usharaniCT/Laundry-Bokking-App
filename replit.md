# Laundry Booking System

## Overview

This is a Flask-based web application for managing laundry bookings in a dormitory or student housing environment. The system allows students to register, login, book laundry time slots, and view their booking history. It also includes an admin interface for managing all bookings.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

The application follows a traditional MVC (Model-View-Controller) architecture using Flask as the web framework:

- **Frontend**: HTML templates with Bootstrap for styling and responsive design
- **Backend**: Flask web framework with Python
- **Database**: SQLAlchemy ORM with flexible database support (SQLite for development, PostgreSQL for production)
- **Session Management**: Flask sessions for user authentication
- **Deployment**: Configured for cloud deployment with proxy support

## Key Components

### Database Models
- **User Model**: Stores student account information (username, email, phone, password)
- **Booking Model**: Manages laundry slot reservations with details like date, time, wash type, payment status

### Authentication System
- Simple username/password authentication
- Session-based user management
- Separate student and admin login flows
- Password stored in plain text (security improvement needed)

### Booking System
- Time slot selection (6 AM to 8 PM in 2-hour blocks)
- Multiple wash types and cloth type options
- Payment method tracking
- Booking status management (Pending, Confirmed, Completed, Cancelled)

### User Interface
- Responsive Bootstrap-based design with dark theme
- Background image support for branding
- Card-based layout for better organization
- Mobile-friendly responsive design

## Data Flow

1. **User Registration**: Students create accounts with username, email, and phone
2. **Authentication**: Users login with username/password, session established
3. **Booking Creation**: Authenticated users select time slots and preferences
4. **Booking Management**: Admins can view and manage all bookings
5. **History Tracking**: Users can view their past and current bookings

## External Dependencies

- **Flask**: Core web framework
- **Flask-SQLAlchemy**: Database ORM
- **Bootstrap**: Frontend CSS framework (via CDN)
- **Font Awesome**: Icon library (via CDN)
- **Werkzeug**: WSGI utilities and proxy support

## Deployment Strategy

### Development Environment
- SQLite database for local development
- Debug mode enabled
- Automatic table creation on startup
- Environment variable fallbacks for configuration

### Production Considerations
- Environment-based database URL configuration
- Session secret from environment variables
- Proxy fix middleware for deployment behind reverse proxies
- Database connection pooling and health checks

### Recent Updates (2025-07-29)
- **Background Image**: Added SRIT logo as background image for professional branding
- **Logo Integration**: Set official SRIT logo for navbar and main dashboard page
- **Payment Integration**: Enhanced payment system with QR code scanner
  - PhonePe UPI ID: 6300622975@ibl
  - Google Pay UPI ID: thippeswamyusha58@okicici
- **Payment Simulation**: Added realistic payment verification flow
  - Dynamic UPI ID switching based on selected payment method
  - Payment confirmation simulation (3-second delay)
  - Button state management for payment confirmation
- **QR Code**: Integrated actual QR code image for UPI payments
- **Branding**: Updated system title and footer with SRIT Autonomous branding

### Current Limitations
- Password security needs improvement (hashing required)
- No email verification system
- Basic error handling
- Limited admin functionality
- Payment processing is simulated (needs real gateway integration)

The application is structured for easy deployment on cloud platforms and includes proper separation of concerns between models, views, and business logic.