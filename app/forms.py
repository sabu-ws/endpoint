from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Length,Regexp


class LoginForm(FlaskForm):
    username = StringField(validators=[Length(min=4, max=20)])
    code = StringField(
        validators=[
            Length(min=6, max=6),
            Regexp(
                r"^[0-9]{6}$",
                message="The code doestn't match",
            ),
        ]
    )  # noqa: E501