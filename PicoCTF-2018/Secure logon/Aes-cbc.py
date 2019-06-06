import base64
import codecs 
import requests


# cookie_old depends on the cookie when you signed in !
cookie_old = "CtdLFMkd/RUmnFFcQKL6azygI7ncZSBrk/3ZjYM0n4+UKcj4j8bye9XVB+oafNgdsB6DStu+WzWI/EX5x7B8dxPIGDrjsHi/rDljus2B3eU="
cookie_64 = base64.b64decode(cookie_old)
print "Len of decoded cookie --> " + str(len(cookie_64))
# create a file to write the flips bit on it !

login_url = "http://2018shell.picoctf.com:56265"
request_url = "http://2018shell.picoctf.com:56265/flag"

credentials = {"user": "Wicked", "password":"Luna"}
request = requests.get(request_url)
response = request.text
print response

# flipped_bits = open("flipped_bits.txt", "w+")
# for i in range(80):
# 	print "-------------" + str(i) + "-------------------"
# 	flipping = ord(cookie_64[i]) ^ ord("0") ^ ord("1")
# 	cookie_new = base64.b64encode(cookie_64[:i]+chr(flipping)+cookie_64[i+1:])
# 	cookies = {"cookie" : cookie_new}
# 	print cookies
# 	request = requests.post("http://2018shell.picoctf.com:56265/flag", cookies=cookies)
# 	respond = request.text
# 	print respond


#replace the cookie_new with the cookie in your browsern refresh and you get the flag 