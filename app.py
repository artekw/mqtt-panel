import os
import sys

import tornado.ioloop
import tornado.web
import tornado.template
import tornado.websocket

from display import displayText

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # displayText(5, "Welcome!")
        self.render("app.tpl")

def make_app():

    return tornado.web.Application([
        (r"/", MainHandler),
        (r'/favicon.ico', tornado.web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), "static")}),
    ],
    template_path=os.path.join(os.path.dirname(__file__), "views"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
