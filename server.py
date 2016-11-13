#!/usr/bin/python

from simplerouter import Router
import os
import ssl

PEM_FILE = os.environ['PEM_FILE']

router = Router()

router.add_route("/guest/attending_max", "guest:attending_max")

application = router.as_wsgi

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    print "Starting wedding server on port 4443"
    https_server = make_server('', 4443, application)
    conn = ssl.wrap_socket(https_server.socket, certfile=PEM_FILE, server_side=True)
    https_server.socket = conn
    https_server.serve_forever()
 
