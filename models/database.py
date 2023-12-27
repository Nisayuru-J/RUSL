import psycopg2

HOST = "rosie.db.elephantsql.com"
PORT_NUMBER = 5432
DB_USER_NAME = "untsllnn"
DB_PASSWORD = "ZTq-KPgmoUcb0hxIlgfu11euqlg92Tcn"
DB_NAME = "untsllnn"

def get_connection():

  conn = psycopg2.connect(
    host= HOST,
    port=PORT_NUMBER,
    user=DB_USER_NAME,
    password=DB_PASSWORD,
    database=DB_NAME
  )
  print("======== CONNECTION ESTABLISHED ========")
  cur = conn.cursor()
  return conn , cur


def end_transaction(conn, cur):
  conn.commit()
  cur.close()
  conn.close()
  print("======== TRANSACTION COMMITED & CONNECTION CLOSED ========")