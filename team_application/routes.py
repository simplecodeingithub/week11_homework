from flask import Flask,render_template, url_for, request, redirect, session, flash

from team_application import app
from datetime import datetime
from team_application.utilities import get_time_of_day
from team_application.forms.register_forms import RegisterForm
from team_application.forms.contact_form import ContactForm
from team_application.data_access import add_person, get_people ,get_projects ,get_project_by_id, get_db_connection, add_contact_submission
from team_application.data import people, projects
from team_application.fake_data import person
import os


@app.route('/')
@app.route('/home')
@app.route('/home/<string:name>')
def home(name=None):
    session['loggedIn'] = False
    now = datetime.now()
    time_slot = get_time_of_day(now.hour)
    if name is None:
        name = "Guest"
    return render_template('home.html',title='Home-TeamApp', time_slot=time_slot, name=name,group='Group-3')


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ""
    register_form = RegisterForm()
    role = "User"

    if request.method == 'POST':
        first_name = register_form.first_name.data
        last_name = register_form.last_name.data
        email = register_form.email.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = 'Please supply both a first and last name'

        else:
            people.append({'Firstname': first_name, 'Lastname': last_name, 'Email': email, 'Role': role})
            add_person(first_name, last_name, email, role)
            # Flash a success message
            flash('Registration successful! Please login or signup.', 'success')  # 'success' is the category of the flash message
            return redirect(url_for('login'))

    return render_template('register.html', form=register_form, message=error,role=role)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        # Get the form data (assuming username is the firstname here)
        firstname = request.form['username']

        # Simple check for admin user
        if firstname == 'admin_user':  # If the firstname is 'admin_user'
            session['role'] = 'admin'
        else:
            session['role'] = 'user'

        session['username'] = firstname  # Store the username in the session
        session['loggedIn'] = True  # Mark the user as logged in

        # Redirect to home or next page after login
        next_page = request.args.get('next')
        return redirect(next_page or url_for('all_projects'))  # Redirect to home or the requested page

    return render_template('login.html', message=error)  # Show login page


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = ""
#     if request.method == 'POST':
#         firstname = request.form['username']
#
#         # Fetch user from DB using firstname (replace with real query logic)
#         user = get_user_by_firstname(firstname)  # You must have this function
#
#         if user:
#             session['username'] = firstname
#             session['role'] = user['role']  # Set the actual role from DB
#             session['loggedIn'] = True
#
#             return redirect(url_for('all_projects'))
#         else:
#             error = "User not found"
#
#     return render_template('login.html', message=error)
#

# Display only first names to users not logged in, and show full names/emails if they are logged in.
@app.route('/people')
def all_people():
    is_logged_in = session.get('loggedIn', False)
    return render_template('people.html', people=people, title='All People', is_logged_in=is_logged_in)
    # return render_template('people.html', people=people, title='All People')


@app.route('/admin/peopledb')
def all_people_from_db():
    people_from_db = get_people() # This fetches the list of people from the database
    print(people_from_db)
    return render_template('people2.html', people=people_from_db, title='Database People')


# @app.route('/contact', methods=['GET', 'POST'])
# def contact_us():
#     success = False
#     if request.method == 'POST':
#         # Here you can get the form data
#         name = request.form['name']
#         email = request.form['email']
#         message = request.form['message']
#
#
#         # For example, just printing the data to the console
#         print(f"New message from {name} ({email}): {message}")
#
#         # Set the success flag to True after form submission
#         success = True
#
#         # Redirect to the same page with a success message
#         return render_template('contact.html', success=success)
#
#     return render_template('contact.html', success=success)


@app.route("/about")
def about():
    return render_template("about_us.html", title="About Us")

@app.route('/admin/users')
def view_users():
    if session.get('role') != 'admin':
        flash("Access denied. Admins only.", "danger")
        return redirect(url_for('login'))

    users = get_people()
    return render_template('view_users.html', users=users)



@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    session.pop('role', None)
    session['loggedIn'] = False
    return redirect(url_for('home'))


@app.route('/projects')
def all_projects():
    # Fetch all projects from the database
    projects = get_projects()

    # Render the projects page with all the projects
    return render_template('projects.html', projects=projects)


@app.route('/project/<int:project_id>')
def project_by_id(project_id):
    # Fetch the project from the database
    project = get_project_by_id(project_id)

    if not project:
        return render_template('404.html'), 404

    # Time-based greeting
    time_slot = get_time_of_day(datetime.now().hour)

    # Get all projects to create next/previous navigation links
    all_projects = get_projects()
    total = len(all_projects)

    # Generate URLs for next and previous projects
    next_url = url_for('project_by_id', project_id=project_id + 1) if project_id + 1 < 4 else None
    previous_url = url_for('project_by_id', project_id=project_id - 1) if project_id > 0 else None

    # Check for the existence of the project images and choose the correct format
    base_path = os.path.join(app.static_folder, 'images')
    image_src = None
    for ext in ['.jpg', '.jpeg', '.png']:
        candidate = f'project_{project_id}{ext}'
        if os.path.exists(os.path.join(base_path, candidate)):
            image_src = f'/static/images/{candidate}'
            break

    # If no image found, use a default image
    if not image_src:
        image_src = '/static/images/image_1.jpg'

    # Check for an optional GIF for the project
    gif_filename = f'project_{project_id}.gif'
    gif_path = os.path.join(base_path, gif_filename)
    image_gif = f'/static/images/{gif_filename}' if os.path.exists(gif_path) else None

    # Render the project details page
    return render_template(
        'project.html',  # Render project.html
        project=project,
        time_slot=time_slot,
        next_url=next_url,
        previous_url=previous_url,
        image_src=image_src,
        image_gif=image_gif,
        title=project['name']
    )

@app.route('/project_detail/<int:project_id>')
def project_detail(project_id):
    # Fetch the project from the database by its ID
    project = get_project_by_id(project_id)

    if not project:
        return render_template('404.html'), 404  # Handle the case where the project doesn't exist

    return render_template('project_details.html', project=project)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        add_contact_submission(form.name.data, form.email.data, form.message.data)
        flash('Your message has been sent. Thank you!')
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)