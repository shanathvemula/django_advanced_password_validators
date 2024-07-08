# Django Password Validator

A Django package for custom password validation. Extends Django password validation options to include minimum uppercase, minimum lowercase, minimum numerical, and minimum special characters. This was created in an attempt to keep up with industry standards for strong user passwords.

This package works for python 3.6+.

## Prerequisites

Requires Django 2.2 or later.
You can install the latest version of Django via pip:

```bash
pip install django
```

Alternatively, you can install a specific version of Django via pip:

```bash
pip install django=3.2
```

> **_NOTE:_**  See the [django-project](https://docs.djangoproject.com) documentation for information on non-deprecated Django versions.


## Installation

```bash
pip install django_advanced_password_validators
```

### Development installation

```bash
git clone https://github.com/shanathvemula/django_advanced_password_validators
cd django-advanced_password_validation
pip install --editable .
```

## Usage

<br/>
Add the custom validators to your AUTH_PASSWORD_VALIDATORS setting in your Django project's settings file:

<br/>


```shell
# settings.py
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django_advanced_password_validators.validators.password_validators.PasswordValidators',
        'OPTIONS': {
            "min_length": 8,
            "max_length": 128,
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
