from flask import render_template
from wordlehelper import app
from wordlehelper.forms import Form
from wordlehelper.utils.solve_wordle import solve_wordle
# from wordlehelper.models import WordState


# app route with method get and post
@app.route('/', methods=['GET', 'POST'])
def home():
    words = []
    errors = []
    form = Form()
    if form.validate_on_submit():
        gray = form.gray.data
        green = form.green.data
        yellow = form.yellow.data
        words = solve_wordle(gray, green, yellow)
    else:
        errors = [e for e in form.errors.values()]
        print(errors)
    return render_template('index.jinja', title='home', form=form, words=words, errors=errors)
