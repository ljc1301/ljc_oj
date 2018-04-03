# coding:utf-8

import tornado.web
import tornado.escape
import methods.readdb as mrd
from methods.settings import *
from methods.get_user import get_user

class SubmissionsHandler(tornado.web.RequestHandler):
    def get(self):
        user=get_user(self)
        page=self.get_argument('page','0')
        try:
            page=int(page)
        except:
            self.render("404.html",user=user)
        else:
            username=self.get_argument('username','')
            pid=self.get_argument('pid','')
            language=self.get_argument('language','')
            result=self.get_argument('result','')
            self.render("submissions.html",user=user,page=page,username=username
                ,pid=pid,language=language,result=result,results=results,languages=languages)

    def post(self):
        page=int(self.get_argument('page'))
        ps=mrd.select_table(table="problems",column="`index`,name",other="order by `index`")
        p={}
        for i in ps:
            p[i[0]]=i[1]
        sub=mrd.select_table(table="submissions",column="id,username,pid,lang,length,submittime,testcase,result,time,memory",other="order by id desc")
        if self.get_argument('username',''):
            username=self.get_argument('username')
            sub=[i for i in sub if i[1]==username]
        if self.get_argument('pid',''):
            try:
                pid=ps[int(self.get_argument('pid'))]
                sub=[i for i in sub if i[2]==pid]
            except:
                pass
        if self.get_argument('language','-1')!='-1':
            lang=self.get_argument('language')
            try:
                lang=int(self.get_argument('language'))
                sub=[i for i in sub if i[3]==lang]
            except:
                pass
        if self.get_argument('result','-1')!='-1':
            try:
                res=int(self.get_argument('result'))
                if res==-2:
                    sub=[i for i in sub if (not i[7] in not_judged) and (i[7]!=ac)]
                else:
                    res=results[res]
                    sub=[i for i in sub if i[7]==res]
            except:
                pass
        sub=sub[page*20:page*20+20]
        res=[]
        for i in range(len(sub)):
            res.append(["%02d"%i])
            res[-1].append(sub[i][0])
            res[-1].append(sub[i][1])
            res[-1].append(p[sub[i][2]])
            res[-1].append(sub[i][7])
            res[-1].append("--" if sub[i][8]==-1 else "%dms"%sub[8])
            res[-1].append("--" if sub[i][9]==-1 else "%.2lfMB"%(float(sub[9])/1024/1024))
            res[-1].append(languages[sub[i][3]])
            res[-1].append("%dB"%sub[i][4])
            res[-1].append(sub[i][5].strftime("%Y-%m-%d %H:%M:%S"))
        self.write(tornado.escape.json_encode(res))

class SubmissionHandler(tornado.web.RequestHandler):
    def get(self,rid):
        user=get_user(self)
        try:
            res=mrd.select_table(table="submissions",column="id,username,pid,lang,length,submittime,testcase,result,time,memory",other="where id = "+str(int(rid)))
            p=mrd.select_table(table="problems",column="id,name",other="where id = "+str(res[0][2]))
            if not res:
                self.render("404.html",user=user)
            else:
                f=open("./submissions/"+rid+"."+suffix[int(res[0][3])])
                code=f.read()
                f.close()
                self.render("submission.html",user=user,res=res[0],p=p[0],code=code,languages=languages)
        except:
            self.render("404.html",user=user)

    def post(self,rid):
        try:
            data=mrd.select_table(table="submissions",column="result,time,memory",other="where id = "+str(int(rid)))
            res=[data[0][0],
                '--' if data[0][1]==-1 else "%dms"%data[0][1],
                '--' if data[0][2]==-1 else "%.2lfMB"%(float(data[0][2])/1024/1024),
                ""]
            try:
                f=open("./submissions/msg_"+rid+".txt")
                res[3]=f.read()
                f.close()
            except:
                pass
            self.write(tornado.escape.json_encode(res))
        except:
            pass
