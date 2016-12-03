#!/usr/bin/python

import json
import mysql.connector
import os
from webob import Response

USER = os.environ['DB_USER']
PASS = os.environ['DB_PASS']
HOST = os.environ['DB_HOST']
DB   = os.environ['DB_DB']

def get_guest(request):
    invitee = request.urlvars['invitee']

    cnx = mysql.connector.connect(user=USER, password=PASS,
                                  host=HOST, database=DB)

    cursor = cnx.cursor()
    query = 'SELECT * from Guests WHERE Invitee=%s'
    cursor.execute(query, (invitee,))
    row = cursor.fetchone()

    if not row:
      result = {"errors":[
        {
          "title":"Could not find guest for given invitee.",
          "code":"API_ERR",
          "status":"404"
        }
      ]}
      status = 404
    else:
      result = {'data': {
          'type': 'guests',
          'id': row[9],
          'attributes': {
            'invitee': row[0],
            'attendingMax': row[1],
            'attendingNum': row[2],
            'guestNames': row[3],
            'entree1': row[4],
            'entree2': row[5],
            'hotel': row[6],
            'shuttleToTime': row[7],
            'shuttleFromTime': row[8],
            'attending': row[10]
          }
        }
      }
      status = 200


    cursor.close();
    cnx.close();

    res = Response(json.dumps(result))
    res.status = status
    return res
