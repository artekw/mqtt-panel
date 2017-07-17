import os
import sys

import paho.mqtt.client as mqtt

import tornado.ioloop
import tornado.web
import tornado.template
import tornado.gen
from tornado.queues import Queue

from display import displayText, clock

brokerIP = "192.168.88.245"
brokerPort = 1883

q = Queue(maxsize=2)

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


def on_connect(client, obj, flags, rc):
    print("rc: " + str(rc))


@tornado.gen.coroutine
def on_message(client, obj, msg):
    #print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    item = str(msg.payload)
    yield q.put(item)
    print('Put %s' % item)


def mqtt_run():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(brokerIP, brokerPort, 60)
    client.subscribe([("/sensmon/outnode/temp", 0), ("/sensmon/artekroom/temp", 0)])
    client.loop_start()


class SettingsPage(tornado.web.RequestHandler):
    def get(self):
        self.render('settings.tpl')


def make_app():
    # run MQTT loop in background
    mqtt_run()
    return tornado.web.Application([
        (r'/', HomePage),
        (r'/message', MessagePage),
        (r'/settings', SettingsPage),
        (r'/favicon.ico', tornado.web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), "static")}),
    ],
    template_path=os.path.join(os.path.dirname(__file__), "views"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True)

@tornado.gen.coroutine
def update():
    # if items in queue - display them
    if q.qsize():
        item = yield q.get()
        try:
            print('Doing work on %s' % item)
            displayText(2, item, 'text_green', 'bg_black', 5)
            yield tornado.gen.sleep(0.01)
        finally:
            q.task_done()
        yield q.join()
    clock()

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    mainLoop = tornado.ioloop.IOLoop.current()
    scheduler = tornado.ioloop.PeriodicCallback(
        update, 500, io_loop=mainLoop)

    scheduler.start()
    mainLoop.start()
