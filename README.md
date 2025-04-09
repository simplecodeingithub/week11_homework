Team App - README
Overview
The Team Application is a Flask-based web app designed to manage users, teams, and projects. The app supports features like user registration, login, project management, and administrative functionalities. It is connected to a MySQL database where user, project, and contact information is stored.

The app uses Flask, Jinja templates, and Bootstrap 5 for the frontend to create a responsive, user-friendly interface.

Features
1. Basic Routes
/ — The homepage, displays a greeting message.

/home — The same as the homepage.

/home/<string:name> — A personalized homepage greeting. The name in the URL will be used for a custom message (e.g., /home/Bob will greet "Bob").

2. Registration and Login Routes
/register — A registration form for new users.

/login — A login form that allows users to log in by entering their first name.

/logout — Logs the user out and redirects them to the homepage.

3. User and Project Management Routes
/people — Displays a list of all users (people) in the app.

/peopledb — Displays a list of people fetched from the database.

/projects — Lists all projects in the system.

/project/<int:project_id> — Displays a specific project by its ID.

/project_detail/<int:project_id> — Shows detailed information about a specific project.

4. Admin-Specific Pages
/admin/view_users — Admin-only route to view all users in the system.

/admin/peopledb — Admin-only route to view people data from the database.

5. Contact and About Us Pages
/contact — A contact form where users can submit their name, email, and message.

/about — An "About Us" page that gives information about the team and the project.

6. Error Handling
404.html — Displays an error page when a route is not found.

500.html — Displays an error page for server-side issues.

MySQL Database Integration
The app integrates with a MySQL database and uses the following tables:

person — Stores user details (first name, last name, email, role).

project — Stores project details (name, description, image, etc.).

contact — Stores contact form submissions (name, email, message).

Data is fetched from the database using functions in data_access.py.

Session Management
Session management is used to track whether a user is logged in and to store their role (user/admin). The session object is used to handle user authentication:

Login: After logging in, the session is updated with the username, role, and login status.

Logout: Logs the user out by clearing the session data.

Admin Access: Routes such as /admin/view_users and /admin/peopledb are restricted to users with the admin role.