import random
import string






def randomString(length):
	key = string.ascii_uppercase
	return "".join(random.choice(key) for i in range(length))

def ord_(char):
	character = ord(char)
	if (character > 0x2f and character <= 0x39):
		return character - 0x30
	else:
		if (character > 0x40 and character <= 0x5a):
			return character - 0x37
		else:
			print "Invalid character"
			exit()


def validation():
	keygen = randomString(16)
	print keygen
	keylen = len(keygen)
	sum = 0
	for i in range(keylen - 1):
		sum = sum + (ord_(keygen[i]) + 1) * ( i + 1)

	var_14 = sum % 0x24
	print var_14
	return var_14 == (ord_(keygen[len(keygen) - 1]))



def main():
	result = validation()
	print "[*] Result -> {} ".format(result)

	





if __name__ == '__main__':
	main()