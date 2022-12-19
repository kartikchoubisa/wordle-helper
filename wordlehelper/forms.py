from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, ValidationError
import re
import logging

class Form(FlaskForm):
    gray = StringField('gray')
    green = StringField('green')
    yellow = StringField('yellow')
    submit = SubmitField('Submit')

    def validate_gray(self, gray):
        # if gray has a non-alphabetical character, raise a validation error
        if gray.data and not gray.data.isalpha():
            raise ValidationError('Gray letters must be alphabetical')

    def index_out_of_range(self, st):
        ind = [int(x) for x in st if x.isdigit()]
        print(ind)
        for i in ind:
            if 1 <= i <= 5:
                return False
        return True

    def validate_green(self, green):
        # regular expression to match the type 'a1b2...'
        pattern = re.compile('([a-z][0-9])*')
        if not re.fullmatch(pattern, green.data):
            raise ValidationError('Green letters must be of the form a1b2...')

        if green.data and self.index_out_of_range(green.data):
            raise ValidationError('Green letters must be in the range [1, 5]')

        ind = [int(x) for x in green.data if x.isdigit()]
        if len(ind) != len(set(ind)):
            raise ValidationError('Green letters must be of the form a1b2...')

    def validate_yellow(self, yellow):
        # regular expression to match the type 'a1b2...'
        pattern = re.compile('([a-z][0-9])*')
        if not re.fullmatch(pattern, yellow.data):
            raise ValidationError('Yellow letters must be of the form a1b2...')

        if yellow.data and self.index_out_of_range(yellow.data):
            raise ValidationError('Yellow letters must be in the range [1, 5]')
