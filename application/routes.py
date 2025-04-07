# For rendering HTML templates, generating URLs for routes, accessing request data (form data, query parameters), redirecting to different routes, handling user sessions (login state), displaying temporary messages to users
from flask import render_template, url_for, request, redirect, session, flash

from application import app
from datetime import datetime
from application.utilities import get_time_of_day
from application.data import people

# Decorator binds a URL path to a function
@app.route('/')
@app.route('/home')
def home():
    # Sets default logged_in status to False if it doesn't exist in session
    # Ensuring we always have a logged_in value, even for new visitors
    session['loggedIn'] = False if 'logged_in' not in session else session['logged_in']
    # Gets the current time to personalise the greeting
    now = datetime.now()
    # Gets time of day string (Morning, Afternoon, Evening, Night)
    time_slot = get_time_of_day(now.hour)
    # Renders the home.html template with variables that can be used in the template
    # title will be used in the browser tab title
    # is_morning is a boolean flag that can be used for conditional rendering
    return render_template('home.html', title='Home', time_slot=time_slot, is_morning=True)

# Two versions: one with a name parameter, one without
@app.route('/welcome/<name>') # <name> part of the URL is a variable
@app.route('/welcome')
def welcome(name="World"): # Default parameter value if name is not provided
    # Renders the welcome2.html template with name and group variables
    return render_template('welcome2.html', name=name, group='Everyone')


@app.route('/admin')
def admin():
    # Checks if user is logged in by verifying username exists
    if 'username' in session and session.get('logged_in'):
        # If logged in, gets the username from the session
        username = session['username']
        # Renders admin area template with username included
        return render_template('adminarea.html', username=username, title='Admin Area')
    # If not logged in, renders admin area template but with username=False
    # Affects how the template is displayed (showing login prompts instead of admin features)
    return render_template('adminarea.html', username=False, title='Admin Area')


# Route accepts both GET and POST HTTP methods
@app.route('/adminpage1', methods=['GET', 'POST'])
def adminpage1():
    # Checks if user is logged in
    if 'username' in session:
        username = session['username']
        print(username)
        # Renders page1.html template for authenticated users
        return render_template('page1.html', username=username, title='Admin Page 1')
    # Redirects to admin area with login prompt, if not logged in
    return render_template('adminarea.html', username=False, title='Admin Area')


@app.route('/adminpage2')
def adminpage2():
    if 'username' in session:
        username = session['username']
        return render_template('page2.html', username=username, title='Admin Page 2')
    return render_template('adminarea.html', username=False, title='Admin Area')


# Defines login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None # Initialises error variable
    app.logger.debug("Start of login") # Log debug message
    # Checks if form was submitted (POST request)
    if request.method == 'POST':
        # Stores username from form in session
        username = request.form['username']
        # Gets password from form (not used in this example, but would be used for authentication)
        password = request.form['password']
        # Basic hardcoded login
        if username == 'admin' and password == 'password':
            session['username'] = username
            # Sets logged_in session variable to True
            session['logged_in'] = True
            # Sets user role (used for permissions)
            session['role'] = 'admin'
            # Redirects to the people listing page after successful login
            return redirect(url_for('view_people'))
        else:
            error = "Invalid credentials"

    # passing any error messages to display
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    # Removes the username and role from the session if it is there
    # 'None' in case there is no username/it doesn't exist
    session.pop('username', None)
    session.pop('role', None)
    session['loggedIn'] = False
    # Redirects to listing page available to public
    return redirect(url_for('view_people'))


@app.route('/people')
def view_people():
    is_logged_in = session.get('logged_in', False)
    return render_template('people.html', people=people, is_logged_in=is_logged_in, title='Team Members')


# The <int:person_id> part of the URL is an integer variable
@app.route('/people/<int:person_id>')
def member_detail(person_id):
    if not session.get('logged_in'):
        # Flash messages are temporary messages shown to the user
        flash("Please log in to view member details", "warning")
        return redirect(url_for('login'))

    # Finds the first person with matching ID
    person = next((p for p in people if p["id"] == person_id), None)
    if not person:
        return "Member not found", 404
    return render_template('person_detail.html', person=person, title=f"Profile: {person['first_name']}")

@app.route('/contact', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        first_name = contact_us.firstname.data
        last_name = contact_us.lastname.data
        email = contact_us.email.data
        if len(first_name) == 0 or len(last_name) == 0:
            error = 'Please supply both a first and last name'
        else:
            people.append({'Firstname': first_name, 'Lastname': last_name, 'Email': email})
            add_person(first_name, last_name, email)  # Flash a success message
            flash('Registration successful! Please login or signup.', 'success')  # 'success' is the category of the flash message
    return render_template('contact_us.html', form=contact_us)