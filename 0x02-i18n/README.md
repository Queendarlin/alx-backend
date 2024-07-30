# ALX Backend - Internationalization and Time Zone Handling

This project demonstrates the implementation of internationalization (i18n) and time zone handling in a Flask application. The application supports multiple languages (English and French) and can infer the user's time zone to display the current time accurately.

## Features

- **Internationalization (i18n)**: Supports English and French languages.
- **Time Zone Handling**: Infers and displays the current time based on the user's time zone.
- **Locale Selection**: Determines the locale based on URL parameters, user settings, or request headers.
- **Time Zone Selection**: Determines the time zone based on URL parameters or user settings, defaulting to UTC if none are provided.

## Requirements

- Python 3.6+
- Flask
- Flask-Babel
- Pytz

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/alx-backend.git
    cd alx-backend/0x02-i18n
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

The Flask application is configured using a `Config` class which includes the supported languages and default locale and time zone.

```python
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
