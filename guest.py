#!/usr/bin/python
import mysql.connector
import os
from webob import Response

USER = os.environ['DB_USER']
PASS = os.environ['DB_PASS']
HOST = os.environ['DB_HOST']
DB   = os.environ['DB_DB']

def attending_max(request):
    first_name = request.urlvars['first_name']
    last_name = request.urlvars['last_name']

    cnx = mysql.connector.connect(user=USER, password=PASS,
                                  host=HOST, database=DB)

    cursor = cnx.cursor()
    query = 'SELECT AttendingMax from Guests WHERE FirstName=%s AND LastName=%s'
    cursor.execute(query, (first_name, last_name))

    max_num = cursor.fetchone()[0]

    return Response("{}".format(max_num))

