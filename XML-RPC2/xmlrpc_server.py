from SimpleXMLRPCServer import SimpleXMLRPCServer
import random

class ServerClass():
    def __init__(self):
        self.authenticated = []
        self.username = "root"
        self.password = "xn3ma8"

    def login(self, username, password):
        key = 0.0
        if (self.username == username) and (self.password == password):
            key = random.uniform(1, 100)
            self.authenticated.append(key)
            print key
        return key

    def __check___(self, key):
        flag = False
        #print self.authenticated
        for one in self.authenticated:
            #print one
            if one == key:
                flag = True
        return flag

    def add_num(self, key, a, b):
        if self.__check___(key):
            #print key
            return a + b

    def add_str(self, key, a, b):
        if self.__check___(key):
            #print key
            return str(a) + str(b)

    def repeater(self, key, something):
        if self.__check___(key):
            if isinstance(something, str):
                return "You passed the string: " + something
            else:
                return "You have to pass a string!"

server = SimpleXMLRPCServer(("", 8000))
server.register_instance(ServerClass())
server.register_introspection_functions()
server.serve_forever()