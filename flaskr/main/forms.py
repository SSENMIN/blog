from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
from flaskr.models import User

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        # 修改的时候需要检验
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please user a different username.')


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[DataRequired()])
    submit = SubmitField('Submit')