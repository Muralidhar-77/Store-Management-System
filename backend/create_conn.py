import datetime
import mysql.connector

__con = None

def connect_db():
  print("connecting to database:")
  global __con
  if __con is None:
    __con = mysql.connector.connect(user='root', password='Doremon@77', database='g_dbase')

  return __con
