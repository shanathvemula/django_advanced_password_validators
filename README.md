# Django Password Validator

A Django package for custom password validation.

## Installation

```bash
pip install django_advanced_password_validators
```

<br/>
Add the custom validators to your AUTH_PASSWORD_VALIDATORS setting in your Django project's settings file:

<br/>

```shell
# settings.py
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django_advanced_password_validators.validators.password_validators.PasswordValidators',
        'OPTIONS': {
            "min_length_digit": 1,
            "min_length_alpha": 1,
            "min_length_special": 1,
            "min_length_lower": 1,
            "min_length_upper": 1,
            "special_characters": "~!@#$%^&*()_+{}\":;'[]"
        }
    }
]

```