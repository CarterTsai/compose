import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])

class WebGUI(object):
    def run(self):
        PORT = 8080
        print "Server run on ", PORT
        application.listen(PORT)
        tornado.ioloop.IOLoop.instance().start()
