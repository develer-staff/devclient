#!/usr/bin/python
#-*- coding: utf-8 -*-

import time
import Queue

import event_type

class Application(object):
    """
    Main class for the application part of client.
    """

    def __init__(self, classes, q_app_gui, q_gui_app):
        self.classes = classes
        self.q_app_gui = q_app_gui
        self.q_gui_app = q_gui_app

        self.sock = self.classes['Socket']()

    def mainLoop(self):
        while 1:
            time.sleep(0.2)
            if self.sock.connected:
                data = self.sock.read()
                if data:
                    self.q_app_gui.put((event_type.MSG, data))

            try:
                cmd, msg = self.q_gui_app.get(0)
                if cmd == event_type.MSG and self.sock.connected:
                    self.sock.write(msg)
                elif cmd == event_type.END_APP:
                    return
                elif cmd == event_type.CONNECT:
                    self.sock.connect("localhost", 6666) #FIX
            except Queue.Empty:
                pass