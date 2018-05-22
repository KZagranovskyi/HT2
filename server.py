import SimpleHTTPServer
import SocketServer

PORT = 8000


class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/simplehttpwebpage_content.html'
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


if __name__== "__main__":
    Handler = MyRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "serving at port", PORT
    httpd.serve_forever()
