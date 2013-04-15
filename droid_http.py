import SimpleHTTPServer
import SocketServer
import subprocess

import android

droid = android.Android()

PORT = 8001

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def get_data(self):
        save_path = '/mnt/sdcard/photo_.jpg'
        droid.cameraInteractiveCapurePicture(save_path)
        f = open(save_path, 'rb')
        return f.read()
        
    def do_GET(self):
        try:
            #send code
            self.send_response(200)

            #send header first
            self.send_header('Content-type','image/png')
            self.end_headers()
            
            #send file content to client
            self.wfile.write(self.get_data())
            return
        except IOError:
            self.send_error(404, 'file not found')

                        
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
