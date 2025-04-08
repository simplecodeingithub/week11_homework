from flask import Flask,render_template, url_for, request, redirect, session, flash

from team_application import app
from datetime import datetime
from team_application.utilities import get_time_of_day
from team_application.forms.register_forms import RegisterForm
from team_application.data_access import add_person, get_people
from team_application.data import people, projects
from team_application.fake_data import person
import os

# @app.route('/')
# @app.route('/home')
# def home():
#     session['loggedIn'] = False  # Store the user's logged-in status as False in the session(not logged in when they visit the home page)
#     now = datetime.now()
#     time_slot = get_time_of_day(now.hour)
#     return render_template('home.html', title='Home', time_slot=time_slot, is_morning=True)
#
#
# @app.route('/welcome')
# @app.route('/welcome/<string:name>')
# def welcome(name="World"):
#     return render_template('welcome2.html', name=name, group='Everyone')

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
    if request.method == 'POST':
        # Get the form data
        session['username'] = request.form['username']
        session['loggedIn'] = True

        # Set the role based on the username or some condition
        if session['username'] == 'admin_user':  # Example condition
            session['role'] = 'admin'
        else:
            session['role'] = 'user'

        next_page = request.args.get('next')
        return redirect(next_page or url_for('home'))  # Redirect to /projects after login
    return render_template('login.html', title="Login")


# Route to show an individual project
@app.route('/project/<int:project_id>')
def project_by_id(project_id):
    if project_id + 1 > len(projects):  # If project_id is out of range, redirect to all projects page
        return render_template('projects.html', projects=projects, title='All Projects')

    # Time-based greeting
    time_slot = get_time_of_day(datetime.now().hour)

    # URLs to navigate for next and previous project
    if len(projects) > project_id + 1:
        next_url = url_for('project_by_id', project_id=project_id + 1)
    else:
        next_url = False
    if project_id > 0:
        previous_url = url_for('project_by_id', project_id=project_id - 1)
    else:
        previous_url = False

        # Image paths for the project (checking for .jpg, .jpeg, and .png)
    image_src = '/static/images/project_' + str(project_id) + '.jpg'
    if not os.path.exists(os.path.join(app.static_folder, 'images/project_' + str(project_id) + '.jpg')):
        image_src = '/static/images/project_' + str(project_id) + '.jpeg'
        if not os.path.exists(os.path.join(app.static_folder, 'images/project_' + str(project_id) + '.jpeg')):
            image_src = '/static/images/project_' + str(project_id) + '.png'

    # Check for the existence of the optional GIF file for the project
    gif_path = os.path.join(app.static_folder, 'images/project_' + str(project_id) + '.gif')
    if os.path.exists(gif_path):
        image_gif = '../static/images/project_' + str(project_id) + '.gif'
    else:
        image_gif = False

    # Project title
    title = projects[project_id]['name']

    return render_template(
        'project.html',
        project=projects[project_id],
        time_slot=time_slot,
        next_url=next_url,
        previous_url=previous_url,
        image_src=image_src,
        image_gif=image_gif,
        title=title
    )


# Route to show all projects
@app.route('/projects')
def all_projects():
    return render_template('projects.html', projects=projects, title='All Projects')

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


@app.route("/contact", methods=["GET", "POST"])
def contact_us():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        print(f"Contact form submitted: {name}, {email}, {message}")
        flash("Message sent successfully!", "success")
    return render_template("contact.html", title="Contact Us")


@app.route('/project_details/<int:project_id>')
def project_detail(project_id):
    # This line searches for a project with the given project_id and returns it; if not found, returns None
    project = next((proj for proj in projects if proj['ID'] == project_id), None)
    # If project is not found, return a 404 error page
    if project is None:
        return render_template('404.html'), 404
    # If project is found, it renders the project_details page with the project data
    return render_template('project_details.html', project=project)

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