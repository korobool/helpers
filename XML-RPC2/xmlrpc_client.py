__author__ = 'Alien'
from xmlrpclib import ServerProxy
connect = ServerProxy("http://localhost:8000")
#s = ServerProxy("http://user:pass@host:8080")
print connect.system.listMethods()
key = connect.login("root", "xn3ma8")
print connect.add_num(key, 5, 10)
print connect.add_str(key, 5, 10)
print connect.repeater(key, "Hello!")
print connect.repeater(key, 500)
raw_input()
