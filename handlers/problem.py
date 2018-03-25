# coding:utf-8

import tornado.web
import tornado.escape
import methods.readdb as mrd
from methods.settings import *
from methods.get_user import get_user

class ProblemsHandler(tornado.web.RequestHandler):
    def get(self):
        user=get_user(self)
        problems=mrd.select_table(table="problems",column="id,`index`,name,sub,ac",other="order by `index`")
        temp=[]
        if not user:
            temp=[p+(-1,) for p in problems]
        else:
            for p in problems:
                t=-1
                r=mrd.select_table(table="submissions",column="result",other="where username = '"+user[0]+"'")
                for i in r:
                    if not i[0] in not_judged:
                        t=0
                        break
                if t==0:
                    for i in r:
                        if i[0]==ac:
                            t=1
                            break
                temp.append(p+(t,))
        self.render("problems.html",user=user,problems=temp)

class ProblemHandler(tornado.web.RequestHandler):
    def get(self,pid):
        user=get_user(self)
        problem=mrd.select_table(table="problems",column="id,name,tl,ml,sub,ac,`index`",other="where id = "+pid)
        if not problem:
            self.render("404.html",user=user)
        else:
            self.render("p/"+pid+".html",user=user,p=problem[0])