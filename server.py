#!/usr/bin/python

from simplerouter import Router

router = Router()

router.add_route("/guest/attending_max", "guest:attending_max")

application = router.as_wsgi

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    print "Starting wedding server on port 8080"
    make_server('', 8080, application).serve_forever()
 
