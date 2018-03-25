# coding:utf-8

import tornado.escape
import methods.readdb as mrd

def get_user(s):
    user=s.get_secure_cookie('user')
    if user:
        user=tornado.escape.json_decode(user)
        user_infos=mrd.select_table(table="users",column="*",other="where username = '"+user[0]+"'")
        if user_infos:
            db_pwd=user_infos[0][2]
            if db_pwd!=user[1]:
                user=None
                s.clear_cookie('user')
        else:
            user=None
    else:
        user=None
    return user