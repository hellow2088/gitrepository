import signal
import socket
import view
import threading
import url

def server_start():
    s = socket.socket()
    s.bind(('', 8000))
    s.listen(128)

    while True:
        client, addr = s.accept()
        r = client.recv(1024)
        # print(r.decode('utf-8'))
        path = (r.decode('utf-8')).split(' ')[1]
        print(path)
        t = threading.Thread(target=request_handle, args=(path, client))
        t.setDaemon(True)  # <-- add this
        t.start()


def request_handle(path, client):
    url.response_data(path, client)




    # rline = 'HTTP/1.1 200 OK\r\n'
    # rheader = 'Server: PWS/1.0\r\n'
    # if path == '/' or path=='/index':
    #     with open('statics/2.jpg', 'rb') as f:
    #         body = f.read()
    #
    #     rb = (rline + rheader + '\r\n').encode('utf-8') + body
    #     client.send(rb)
    #
    # if path=='/favicon.ico':
    #     with open('statics/icon.png', 'rb') as f:
    #         body = f.read()
    #
    #     rb = (rline + rheader + '\r\n').encode('utf-8') + body
    #     client.send(rb)
    #
    # else:
    #     with open('statics/404.html', 'rb') as f:
    #         body = f.read()
    #
    #     rb = (rline + rheader + '\r\n').encode('utf-8') + body
    #     client.send(rb)



if __name__ == '__main__':
    server_start()
