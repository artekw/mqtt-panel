import os
import sys

import paho.mqtt.client as mqtt

import tornado.ioloop
import tornado.web
import tornado.template
import tornado.gen
from tornado.queues import Queue

import settings
from display import displayText, clock, dimmer
from standby import stabdby_mode


brokerIP = settings.read('settings', 'mqtt', 'brokerIP')
brokerPort = settings.read('settings', 'mqtt', 'brokerPort')
httpPort = settings.read('settings', 'http', 'port')
standbyFrom = settings.read('settings', 'standby', 'from')
standbyTo = settings.read('settings', 'standby', 'to')

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
    # print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    item = str(msg.payload)
    yield q.put(item)
    # print('Put %s' % item)


def mqtt_run(): 
    feeds = settings.read('feeds')
    print("Follow %s topics") % (len(feeds))
    feedsTopics = [(f.get('topic'),f.get('priority')) for f in feeds]

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(brokerIP, brokerPort, 60)
    client.subscribe(feedsTopics)

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
    standby = stabdby_mode(standbyFrom, standbyTo)
    if not standby:
        dimmer()
        # if items in queue - display them
        if q.qsize():
            item = yield q.get()
            try:
                # print('Doing work on %s' % item)
                displayText(2, item, 'text_green', 'bg_black', 5)
                yield tornado.gen.sleep(0.01)
            finally:
                q.task_done()
            yield q.join()
        clock()

if __name__ == "__main__":
    app = make_app()
    app.listen(httpPort)
    mainLoop = tornado.ioloop.IOLoop.current()
    scheduler = tornado.ioloop.PeriodicCallback(
        update, 500, io_loop=mainLoop)

    scheduler.start()
    mainLoop.start()
