#!/usr/bin/python

from simplerouter import Router

router = Router()

router.add_route("/guest/{first_name}/{last_name}/attending_max", "guest:attending_max")

application = router.as_wsgi

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    make_server('', 8080, application).serve_forever()
 
