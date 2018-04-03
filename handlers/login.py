# coding:utf-8

import tornado.web
import tornado.escape
import methods.readdb as mrd
import time
from methods.get_user import get_user

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        user=get_user(self)
        if user:
            self.redirect("/")
        else:
            self.render("login.html",user=None)

    def post(self):
        username=self.get_argument("username")
        password=self.get_argument("password")
        remember=self.get_argument("remember")
        user_infos=mrd.select_table(table="users",column="id,username,password",other="where username = '"+username+"'")
        if user_infos:
            db_pwd=user_infos[0][2]
            if db_pwd==password:
                self.set_current_user((username,password),remember)
            else:
                self.write("-1")
        else:
            self.write("-1")

    def set_current_user(self,user,remember):
        if user:
            if remember:
                self.set_secure_cookie('user',tornado.escape.json_encode(user),httponly=True,expires=time.time()+2592000)
            else:
                self.set_secure_cookie('user',tornado.escape.json_encode(user),httponly=True,expires=time.time()+86400)
        else:
            self.clear_cookie('user')

class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_cookie('user')
        self.redirect("/")
