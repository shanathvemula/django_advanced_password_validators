# django_password_validator/validators/password_validators.py
from django.core.exceptions import ValidationError

try:
    from django.utils.translation import gettext as _, ngettext
except ImportError:
    from django.utils.translation import ugettext as _, ungettext as ngettext

from django.contrib.auth.password_validation import (
    UserAttributeSimilarityValidator as BaseUserAttributeSimilarityValidator,
    CommonPasswordValidator as BaseCommonPasswordValidator
)


class PasswordValidators:
    def __init__(
            self,
            max_length=128,
            min_length=8,
            min_length_digit=0,
            min_length_alpha=0,
            min_length_special=0,
            min_length_lower=0,
            min_length_upper=0,
            special_characters="~!@#$%^&*()_+{}\":;'[]",
            user_attributes=None
    ):
        self.max_length = max_length
        self.min_length = min_length
        self.min_length_digit = min_length_digit
        self.min_length_alpha = min_length_alpha
        self.min_length_special = min_length_special
        self.min_length_lower = min_length_lower
        self.min_length_upper = min_length_upper
        self.special_characters = special_characters
        self.user_attributes = user_attributes or ['username', 'email']

    def validate(self, password, user=None):
        validation_errors = []
        length = len(password)
        digit_count = sum(1 for char in password if char.isdigit())
        alpha_count = sum(1 for char in password if char.isalpha())
        lower_count = sum(1 for char in password if char.islower())
        upper_count = sum(1 for char in password if char.isupper())
        special_count = sum(1 for char in password if char in self.special_characters)

        # Entirely Numeric
        if password.isdigit():
            validation_errors.append(ValidationError(
                _(
                    'Password not be numeric.',
                ),
                code='Password not be numeric.',
            ))
        # User attribute similarity check
        similarity_validator = BaseUserAttributeSimilarityValidator(user_attributes=self.user_attributes)
        try:
            similarity_validator.validate(password, user)
        except ValidationError as e:
            validation_errors.extend(e.error_list)

        # Common password check
        common_password_validator = BaseCommonPasswordValidator()
        try:
            common_password_validator.validate(password.lower(), user)
        except ValidationError as e:
            validation_errors.extend(e.error_list)

        if length > self.max_length:
            validation_errors.append(ValidationError(
                ngettext(
                    'Password is too long accepts upto %(max_length)d characters.',
                    'Password is too long accepts upto %(max_length)d characters.',
                    self.max_length
                ),
                params={'max_length': self.max_length},
                code='password_too_long',
            ))

        if length < self.min_length:
            validation_errors.append(ValidationError(
                _(
                    'Password is too short',
                ),
                code='password_too_short',
            ))
            validation_errors.append(ValidationError(
                ngettext(
                    'This password must contain at least %(min_length)d characters.',
                    'This password must contain at least %(min_length)d characters.',
                    self.min_length
                ),
                params={'min_length': self.min_length},
                code='password_too_short',
            ))

        if digit_count < self.min_length_digit:
            validation_errors.append(ValidationError(
                ngettext(
                    'This password must contain at least %(min_length)d digit (only %(digit_count)d found).',
                    'This password must contain at least %(min_length)d digits (only %(digit_count)d found).',
                    self.min_length_digit
                ),
                params={'min_length': self.min_length_digit, 'digit_count': digit_count},
                code='min_length_digit',
            ))

        if alpha_count < self.min_length_alpha:
            validation_errors.append(ValidationError(
                ngettext(
                    'This password must contain at least %(min_length)d letter (only %(alpha_count)d found).',
                    'This password must contain at least %(min_length)d letters (only %(alpha_count)d found).',
                    self.min_length_alpha
                ),
                params={'min_length': self.min_length_alpha, 'alpha_count': alpha_count},
                code='min_length_alpha',
            ))

        if upper_count < self.min_length_upper:
            validation_errors.append(ValidationError(
                ngettext(
                    'This password must contain at least %(min_length)d upper case letter (only %(upper_count)d found).',
                    'This password must contain at least %(min_length)d upper case letters (only %(upper_count)d found).',
                    self.min_length_upper
                ),
                params={'min_length': self.min_length_upper, 'upper_count': upper_count},
                code='min_length_upper_characters',
            ))

        if lower_count < self.min_length_lower:
            validation_errors.append(ValidationError(
                ngettext(
                    'This password must contain at least %(min_length)d lower case letter (only %(lower_count)d found).',
                    'This password must contain at least %(min_length)d lower case letters (only %(lower_count)d found).',
                    self.min_length_lower
                ),
                params={'min_length': self.min_length_lower, 'lower_count': lower_count},
                code='min_length_lower_characters',
            ))

        if special_count < self.min_length_special:
            validation_errors.append(ValidationError(
                ngettext(
                    'This password must contain at least %(min_length)d special character (only %(special_count)d found).',
                    'This password must contain at least %(min_length)d special characters (only %(special_count)d found).',
                    self.min_length_special
                ),
                params={'min_length': self.min_length_special, 'special_count': special_count},
                code='min_length_special_characters',
            ))

        if validation_errors:
            raise ValidationError(validation_errors)

    def get_help_text(self):
        validation_req = []
        if self.max_length:
            validation_req.append(
                ngettext(
                    "%(max_length)s characters",
                    "%(max_length)s characters",
                    self.max_length
                ) % {'max_length': self.max_length}
            )
        if self.min_length:
            validation_req.append(
                ngettext(
                    "%(min_length)s characters",
                    "%(min_length)s characters",
                    self.min_length
                ) % {'min_length': self.min_length}
            )
        if self.min_length_alpha:
            validation_req.append(
                ngettext(
                    "%(min_length)s letter",
                    "%(min_length)s letters",
                    self.min_length_alpha
                ) % {'min_length': self.min_length_alpha}
            )
        if self.min_length_digit:
            validation_req.append(
                ngettext(
                    "%(min_length)s digit",
                    "%(min_length)s digits",
                    self.min_length_digit
                ) % {'min_length': self.min_length_digit}
            )
        if self.min_length_lower:
            validation_req.append(
                ngettext(
                    "%(min_length)s lower case letter",
                    "%(min_length)s lower case letters",
                    self.min_length_lower
                ) % {'min_length': self.min_length_lower}
            )
        if self.min_length_upper:
            validation_req.append(
                ngettext(
                    "%(min_length)s upper case letter",
                    "%(min_length)s upper case letters",
                    self.min_length_upper
                ) % {'min_length': self.min_length_upper}
            )
        if self.min_length_special and self.special_characters:
            validation_req.append(
                ngettext(
                    "%(min_length_special)s special character, such as %(special_characters)s",
                    "%(min_length_special)s special characters, such as %(special_characters)s",
                    self.min_length_special
                ) % {'min_length_special': str(self.min_length_special), 'special_characters': self.special_characters}
            )
        return _("This password must contain at least") + ' ' + ', '.join(validation_req) + '.'
