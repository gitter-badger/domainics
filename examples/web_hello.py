#! /usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from tornice import WebApp, request_base, request, handler
from tornice import set_dsn, transaction, psql


set_dsn(sys='postgres', host='localhost', user='postgres')
request_base(path='/abc', proto='REST')


@request('(?P<sid>\w+)', methods='GET,POST', fields='page,sort')
def hi(sid, page):

    handler.write("Hello, world, sid=%s, page=%s\n" % (sid, page))  
    handler.write("data: %r" % get_list())


@transaction
def get_list():
  psql("""
  SELECT * FROM (VALUES (1,2), (20,30)) s(a, b)
  """)

  return list(psql)

if __name__ == '__main__':
    app = WebApp(port=8888)
    app.add_static_handler(r'/(.*)', folder='static', default='/index.html')
    app.setup()

    import ioloop
    ioloop.run() # 服务主调度
