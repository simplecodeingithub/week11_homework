from flask import render_template, url_for, request, redirect, session

from team_application import app
from datetime import datetime
from team_application.utilities import get_time_of_day


@app.route('/')
@app.route('/home')
def home():
    session['loggedIn'] = False
    now = datetime.now()
    time_slot = get_time_of_day(now.hour)
    return render_template('home.html', title='Home', time_slot=time_slot, is_morning=True)


@app.route('/welcome/<string:name>')
@app.route('/welcome')
def welcome(name="World"):
    return render_template('welcome2.html', name=name, group='Everyone')