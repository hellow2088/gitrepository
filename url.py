import os

import view

url = [
    ('/test', view.test),
    ('/test1', view.test1),
    ('/index', view.index),

]


def response_data(path, client):
    if path == '/' or path == '':
        path = '/index'
    if not os.path.exists('statics' + path + '.html'):
        with open('statics/404.html', 'rb') as f:
            data = f.read()
        rline = 'HTTP/1.1 200 OK\r\n'
        rheader = 'Server: PWS/1.0\r\n'
        response_data = (rline + rheader + '\r\n').encode('utf-8') + data
        client.send(response_data)

    else:
        for k in url:
            if path == k[0]:
                # print(path)
                return k[1](path, client)
                # break
