from flask import Flask, render_template, session, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,DateTimeField,
											RadioField,SelectField,SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'AReallySecretKey'


class TinyForm(FlaskForm):
	name = StringField('Enter your name in the guestbook: ', validators=[DataRequired()])
	feedback = StringField()
	submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
	
	form = TinyForm()

	if form.validate_on_submit():
		session['name'] = form.name.data
		session['feedback'] = form.feedback.data

		return redirect(url_for('thankyou'))

	return render_template('index.html', form=form)


@app.route('/thankyou')
def thankyou():
	flash('Thanks for the info!')
	return render_template('thankyou.html')

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8002, debug=True)
