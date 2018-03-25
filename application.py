# coding:utf-8

from url import url
import tornado.web
import os
import base64,uuid

settings=dict(
    template_path=os.path.join(os.path.dirname(__file__),"templates"),
    static_path=os.path.join(os.path.dirname(__file__),"statics"),
    cookie_secret=base64.b64encode(uuid.uuid4().bytes+uuid.uuid4().bytes),
    xsrf_cookies=True,
    )

application=tornado.web.Application(
    handlers=url,
    **settings
    )