# coding:utf-8

import MySQLdb
conn=MySQLdb.connect(host="localhost",user="oj",passwd="_oj_password_",db="ljc_oj",port=3306,charset="utf8")
cur=conn.cursor()
