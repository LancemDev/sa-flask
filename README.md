# 🔗 URL Shortener

A modern, secure URL shortening service built with Flask, TailwindCSS, and PostgreSQL (Supabase). Create custom short links, track clicks, and manage your URLs with ease.

![URL Shortener Screenshot](static/screenshot.png)

## ✨ Features

- **User Authentication**: Secure registration and login system
- **URL Shortening**: Create short, memorable links for any URL
- **Analytics**: Track clicks and view link performance
- **Responsive Design**: Beautiful UI that works on all devices
- **Database Integration**: Powered by Supabase PostgreSQL
- **Security**: Password hashing, protected routes, and SQL injection prevention

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- PostgreSQL (via Supabase)
- pip (Python package manager)

### Installation

1. Clone the repository
```bash
git clone https://github.com/LancemDev/sa-flask.git
cd sa-flask
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
# Create a .env file in the project root and setup a supabase postgres database
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://postgres.xxxxx:[YOUR-PASSWORD]@aws-0-us-east-1.pooler.supabase.com:6543/postgres
```

5. Initialize the database
```bash
flask db upgrade
```

6. Run the application
```bash
flask run
```

Visit `http://localhost:5000` in your browser to start using the application.

## 📦 Project Structure

```
url_shortener/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── static/            # Static files (CSS, images)
│   ├── favicon.svg
│   ├── favicon.png
│   └── apple-touch-icon.png
└── templates/         # HTML templates
    ├── base.html
    ├── index.html
    ├── dashboard.html
    ├── login.html
    └── register.html
```

## 🔧 Configuration

The application can be configured using the following environment variables:

- `SECRET_KEY`: Flask secret key for session management
- `DATABASE_URL`: Supabase PostgreSQL connection string
- `FLASK_ENV`: Set to `development` or `production`
- `FLASK_DEBUG`: Enable/disable debug mode

## 🔒 Security Features

- Password hashing using Werkzeug Security
- CSRF protection
- SQL injection prevention through SQLAlchemy
- Session management with Flask-Login
- Protected routes with login requirements

## 🚀 Deployment

### Deploying to Heroku

1. Create a Heroku account and install the Heroku CLI
2. Login to Heroku and create a new app
```bash
heroku login
heroku create your-app-name
```

3. Set environment variables
```bash
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DATABASE_URL=your-supabase-url
```

4. Deploy the application
```bash
git push heroku main
```

### Other Deployment Options

- Docker containerization available
- Can be deployed to any Python-compatible hosting service
- Works with various PostgreSQL providers

## 📝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/) for the web framework
- [TailwindCSS](https://tailwindcss.com/) for the styling
- [Supabase](https://supabase.com/) for the database
- [Flask-Login](https://flask-login.readthedocs.io/) for authentication

## 📞 Support

If you encounter any problems or have suggestions, please [open an issue](https://github.com/LancemDev/sa-flask/issues) or contact the maintainers.