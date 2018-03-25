# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from handlers.login import LoginHandler
from handlers.login import LogoutHandler
from handlers.home import HomeHandler
from handlers.home import OtherHandler
from handlers.problem import ProblemsHandler
from handlers.problem import ProblemHandler
from handlers.submit import SubmitHandler
from handlers.submission import SubmissionsHandler
from handlers.submission import SubmissionHandler

url=[
    (r'/',HomeHandler),
    (r'/login',LoginHandler),
    (r'/logout',LogoutHandler),
    (r'/p',ProblemsHandler),
    (r'/p/([0-9]+)',ProblemHandler),
    (r'/submit',SubmitHandler),
    (r'/submissions',SubmissionsHandler),
    (r'/submissions/([0-9]+)',SubmissionHandler),
    (r".*", OtherHandler),
]