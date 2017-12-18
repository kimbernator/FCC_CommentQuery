import mysql.connector
from settings import db_host, db_user, db_password, db_schema

conn = mysql.connector.Connect(host=db_host,user=db_user,password=db_password,database=db_schema)
cursor = conn.cursor(buffered=True)

DB_INIT = ('CREATE TABLE IF NOT EXISTS filings( '
    'id INT,'
    'id_submission TEXT,'
    'name TEXT,'
    'addressA TEXT,'
    'addressB TEXT,'
    'city TEXT,'
    'state TEXT,'
    'zip TEXT,'
    'comment_text LONGTEXT,'
    'email TEXT,'
    'submission_date TEXT,'
    'dissemination_date TEXT)')

DB_HIGHEST = ('SELECT id FROM filings ORDER BY id DESC LIMIT 1')

DB_ENTRY = ("INSERT INTO filings "
           "(id, id_submission, name, addressA, addressB, city, state, zip, comment_text, email, submission_date, dissemination_date)"
           "VALUES (%(id)s, %(id_submission)s, %(name)s, %(addressA)s, %(addressB)s, %(city)s, %(state)s, %(zip)s, %(comment_text)s, %(email)s, %(submission_date)s, %(dissemination_date)s)")

def init():
    cursor.execute(DB_INIT)
    conn.commit()
    cursor.execute(DB_HIGHEST)
    row = cursor.fetchone()
    cursor.execute('SET NAMES utf8mb4;')
    try:
        return row[0]
    except TypeError:
        return 0

def insert(data_form):
    cursor.execute(DB_ENTRY, data_form)

def commit():
    conn.commit()

def close():
    cursor.close()
    conn.close()
