#!/usr/bin/env python
#
# APIリクエストに対して、ダミーデータを返すスタブAPIサーバー
#

from http.server import HTTPServer, BaseHTTPRequestHandler, CGIHTTPRequestHandler
import json

class StubRequestHandler(CGIHTTPRequestHandler):

    cgi_directories = ['/']

    def do_POST(self):
        print(self.requestline)
        content_length = int(self.headers['content-length'])
        data = self.rfile.read(content_length).decode('utf-8')
        print(data)
        json_data = json.loads(data)
        image_path = json_data.get('image_path')
        if image_path == '/home/user/sample1.jpg':
            data = {
                'success': False,
                'message': 'Error:E50012',
                'estimated_data': {}
            }
        else:
            data = {
                'success': True,
                'message': 'success',
                'estimated_data': {
                    'class': 3,
                    'confidence': 0.8683
                }
            }
        self.wfile.write(("HTTP/1.1 200 OK\n\n" + json.dumps(data)).encode('utf-8'))

if __name__ ==  '__main__':
    
    httpd = HTTPServer(('', 8080), StubRequestHandler)
    httpd.serve_forever()
