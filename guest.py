#!/usr/bin/python

import json
import mysql.connector
import os
from webob import Response

USER = os.environ['DB_USER']
PASS = os.environ['DB_PASS']
HOST = os.environ['DB_HOST']
DB   = os.environ['DB_DB']

def attending_max(request):
    invitee = json.loads(request.body)['invitee']

    print "attending_max: {}".format(invitee)

    cnx = mysql.connector.connect(user=USER, password=PASS,
                                  host=HOST, database=DB)

    cursor = cnx.cursor()
    query = 'SELECT AttendingMax from Guests WHERE Invitee=%s'
    cursor.execute(query, (invitee,))

    max_num = cursor.fetchone()[0]

    return Response(json.dumps({"attending_max": max_num}))

