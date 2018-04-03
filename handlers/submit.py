# coding:utf-8

import tornado.web
import tornado.escape
import methods.readdb as mrd
from methods.db import *
from methods.settings import *
from methods.get_user import get_user

class SubmitHandler(tornado.web.RequestHandler):
    def get(self):
        user=get_user(self)
        pid=self.get_argument("pid","")
        if not user:
            self.redirect("/login")
        else:
           self.render("submit.html",user=user,pid=pid,languages=languages)

    def post(self):
        user=self.get_argument("username")
        pid=self.get_argument("pid")
        lang=self.get_argument("language")
        code=self.get_argument("code")
        try:
            int(pid)
        except:
            self.write("-1")
            return
        p=mrd.select_table(table="problems",column="id",other="where `index` = '"+pid+"'")
        if not p:
            self.write("-1")
            return
        cur.execute("insert into submissions(username,pid,lang,result,length)values('%s',%s,%s,'等待评测',%d)"%(user,p[0][0],lang,len(code)))
        last=mrd.select_table(table="submissions",column="id",other="where username = '"+user+"' and pid = "+str(p[0][0])+" and lang = "+lang+" and length = "+str(len(code))+" order by id desc limit 1")
        conn.commit()
        self.write(str(last[0][0]))
        f=open("./submissions/"+str(last[0][0])+"."+suffix[int(lang)],"w")
        f.write(code)
        f.close()
        cur.execute("insert into judge_queue(rid)values(%d)"%last[0][0])
        conn.commit()
