import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="get_into_tech_c2_2025_v2"
)


def get_db_connection():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",  # Your MySQL username
            password="password",  # Your MySQL password
            database="get_into_tech_c2_2025_v2",  # Your database name
            autocommit=True  # Auto commit to immediately save changes
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


# Add a new person to the database
def add_person(fname, lname, email, role):
    conn = get_db_connection()
    cursor = conn.cursor()


    sql = "INSERT INTO person (firstname, lastname, email, role) VALUES (%s, %s, %s, %s)"
    val = (fname, lname, email, role)
    cursor.execute(sql, val)

    conn.commit()
    print("Person added successfully.")
    cursor.close()
    conn.close()



# Retrieve the list of people from the database
def get_people():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch the ID, Firstname, Lastname, and Email from the person table
    sql = "SELECT PersonID, Firstname, Lastname, email, role FROM person"
    cursor.execute(sql)

    result_set = cursor.fetchall()
    person_list = []
    for person in result_set:
        person_list.append({
            'PersonID': person[0],
            'Firstname': person[1],
            'Lastname': person[2],
            'Email': person[3],  # Added the email in the result
            'Role': person[4]    # added the role in the result
        })

    cursor.close()
    conn.close()

    return person_list


# Example to insert a person
def main():
    print(mydb)

    cursor = mydb.cursor()

    sql = "INSERT INTO person (firstname, lastname, email, role) VALUES (%s, %s, %s, %s)"
    val = [
        ("Fred", "Flintstone", "FredFlin@gmail.com", "user"),
        ("Alice", "Anderson", "alice.admin@example.com", "admin")
    ]
    cursor.executemany(sql, val)

    mydb.commit()

    print(cursor.rowcount, "record inserted.")

# Add a project
def add_project(name, description, image_src):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO project (name, description, image_src) VALUES (%s, %s, %s)"
    val = (name, description, image_src)
    cursor.execute(sql, val)
    conn.commit()
    cursor.close()
    conn.close()

# Get all projects
def get_projects():
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "SELECT id, name, description, image_src FROM project"
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    return [
        {
            'ID': row[0],
            'name': row[1],
            'description': row[2],
            'image_src': row[3]
        }
        for row in results
    ]

# Get project by ID
def get_project_by_id(project_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM project WHERE ID = %s"  # ✅ fixed table name
    cursor.execute(query, (project_id,))
    project = cursor.fetchone()

    connection.close()

    if project:
        return {
            'ID': project[0],
            'name': project[1],
            'description': project[2],
            'image_src': project[3]
        }
    else:
        return None

def add_contact_submission(name, email, message):
    cursor = mydb.cursor()
    query = "INSERT INTO contact_submissions (name, email, message) VALUES (%s, %s, %s)"
    values = (name, email, message)
    cursor.execute(query, values)
    mydb.commit()
    cursor.close()

# def get_user_by_firstname(firstname):
#     conn = get_db_connection()
#     cursor = conn.cursor()
#
#     # If you're using SQLite, use ? instead of %s
#     try:
#         cursor.execute("SELECT firstname, role FROM person WHERE firstname = ?", (firstname,))
#         user = cursor.fetchone()
#         conn.close()
#
#         if user:
#             return {
#                 'firstname': user[0],
#                 'role': user[1]
#             }
#         else:
#             return None
#     except Exception as e:
#         conn.close()
#         print("Error fetching user:", e)
#         return None


if __name__ == "__main__":
    main()
