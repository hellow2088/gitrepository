def open_response_data(path, client):
    with open('statics' + path + '.html', 'rb') as f:
        data = f.read()

    rline = 'HTTP/1.1 200 OK\r\n'
    rheader = 'Server: PWS/1.0\r\n'
    response_data = (rline + rheader + '\r\n').encode('utf-8') + data
    client.send(response_data)


def test(path, client):
    open_response_data(path, client)


def test1(path, client):
    open_response_data(path, client)


def index(path, client):
    open_response_data(path, client)
