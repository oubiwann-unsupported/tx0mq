import sys


display_name = "tx0mq"
library_name = "tx0mq"
version = "0.5.0"
author = "Duncan McGreggor"
author_email = "oubiwann@gmail.com"
license = "BSD"
url = "https://github.com/oubiwann/tx0mq"
description = "A Twisted Library for ZeroMQ"
requirements = [
    "Twisted>=10.0",
    "pyzmq-ctypes>=2.1" if sys.subversion[0] == "PyPy" else "pyzmq>=2.1",
    ]
