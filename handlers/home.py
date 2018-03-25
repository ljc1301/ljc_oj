# coding:utf-8

import tornado.web
import tornado.escape
import methods.readdb as mrd
from methods.get_user import get_user

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        user=get_user(self)
        self.render("home.html",user=user)

class OtherHandler(tornado.web.RequestHandler):
    def get(self):
        user=get_user(self)
        self.render("404.html",user=user)