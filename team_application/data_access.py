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

    sql = "INSERT INTO person (firstname, lastname, email,role) VALUES (%s, %s, %s)"
    val = ("Fred", "Flintstone", "FredFlin@gmail.com","user")


    cursor.execute(sql, val)

    mydb.commit()

    print(cursor.rowcount, "record inserted.")


if __name__ == "__main__":
    main()
