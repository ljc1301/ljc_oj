# coding:utf-8

from db import *

def select_table(table,column,other=''):
    sql="select "+column+" from "+table+" "+other
    cur.execute(sql)
    return cur.fetchall()