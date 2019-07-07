from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, InputRequired, Email
from flask_wtf.file import FileField
from app.models import User

mediums = ['Animation', 'Astrology', 'Blogging', 'Calligraphy', 'Ceramics', \
           'Comedy', 'Community', 'Design', 'Digital', 'DJ', 'Education', 'Equity', \
           'Events', 'Film', 'Floral', 'Food', 'Graphic Design', 'Healing', 'Illustration', \
           'Installation', 'Makeup', 'Model', 'Mixed Media', 'Mural', 'Music', 'Painting', \
           'Performance', 'Photography', 'Podcast', 'Poetry', 'Print', 'Radio', 'Sculpture', \
           'Sex Educator', 'Sex Work', 'Skincare', 'Tattoo', 'Theater', 'Visual Arts', 'Web Design', \
           'Writing', 'Zine']
mediums = [(medium, medium) for medium in mediums ]

def medium_list():
    code = "<ul>\n"
    for medium in mediums:
        code += "<li>" + str(medium) + "<li>\n"
    code += "<ul>"
    return code

def medium_check(form, field):
    if field.data not in mediums:
        raise ValidationError('Field not included in list of mediums')

class joinDirectory(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    medium = SelectField('Medium', choices=mediums, validators=[InputRequired()])
    submit = SubmitField('Join the Database!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email has already been used')
