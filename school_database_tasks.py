import mysql.connector


def get_connection():

  return mysql.connector.connect(
      host="localhost", user="root", password="SqlBasla2026!", database="schooldb"
  )



def get_all_students():
  connection = get_connection()
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM student")
  for row in cursor.fetchall():
    print(row)
  cursor.close()
  connection.close()
def get_student_basic_info():
  connection = get_connection()
  cursor = connection.cursor()
  cursor.execute("SELECT StudentNumber, Name, Surname FROM student")
  for row in cursor.fetchall():
    print(row)
  cursor.close()
  connection.close()



def get_female_students():
  connection = get_connection()
  cursor = connection.cursor()
  cursor.execute("SELECT Name, Surname FROM student WHERE Gender='Q'")
  for row in cursor.fetchall():
    print(row)
  cursor.close()
  connection.close()



def get_students_by_birth_year():
  connection = get_connection()
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM student WHERE YEAR(Birthdate) = 2003")
  for row in cursor.fetchall():
    print(row)
  cursor.close()
  connection.close()

def get_ali_born_2005():
  connection = get_connection()
  cursor = connection.cursor()
  cursor.execute(
      "SELECT * FROM student WHERE YEAR(Birthdate) = 2005 AND name = 'Ali'"
  )
  for row in cursor.fetchall():
    print(row)
  cursor.close()
  connection.close()



def search_students_by_pattern():
  connection = get_connection()
  cursor = connection.cursor()
  cursor.execute(
      "SELECT * FROM student WHERE name LIKE '%an%' OR surname LIKE '%an%'"
  )
  for row in cursor.fetchall():
    print(row)
  cursor.close()
  connection.close()



def count_male_students():
  connection = get_connection()
  cursor = connection.cursor()
  cursor.execute("SELECT COUNT(*) FROM student WHERE Gender='K'")
  res = cursor.fetchone()
  print(f"Erkək tələbə sayı: {res[0]}")
  cursor.close()
  connection.close()



def get_female_students_ordered():
  connection = get_connection()
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM student WHERE Gender='Q' ORDER BY name")
  for row in cursor.fetchall():
    print(row)
  cursor.close()
  connection.close()


