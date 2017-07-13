import os
import sys

import tornado.ioloop
import tornado.web
import tornado.template
#import tornado.websocket

from display import displayText, clock


class HomePage(tornado.web.RequestHandler):
    def get(self):
        self.render('app.tpl')


class MessagePage(tornado.web.RequestHandler):
    def get(self):
        self.render('message.tpl')

    def post(self):
        msg = self.get_argument('msg')
        text_color = self.get_argument('text_color')
        bg_color = self.get_argument('bg_color')
        delay = self.get_argument('delay')


        if msg:
            displayText(5, str(msg), text_color, bg_color, delay)
        else:
            print 'err'
        self.render('message.tpl')


class SettingsPage(tornado.web.RequestHandler):
    def get(self):
        self.render('settings.tpl')


def make_app():

    clock()

    return tornado.web.Application([
        (r'/', HomePage),
        (r'/message', MessagePage),
        (r'/settings', SettingsPage),
        (r'/favicon.ico', tornado.web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), "static")}),
    ],
    template_path=os.path.join(os.path.dirname(__file__), "views"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True)

def update():
    clock()

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    mainLoop = tornado.ioloop.IOLoop.current()
    scheduler = tornado.ioloop.PeriodicCallback(
        update, 500, io_loop=mainLoop)

    scheduler.start()
    mainLoop.start()
