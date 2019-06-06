import random
import string
from z3 import *
import os 
import time




## i tried to solve this the way i solved the first one ( keygen-me-1 ) but failed !
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

def mod_(m, n):
	calc = m % n
	if (calc < 0):
		return n + calc
	else:
		return calc


def key_constraint_001(keygen, length):
	key_constraint = ord_(keygen[0]) + ord_(keygen[1])
	return mod_(key_constraint, 36) == 0xe

def key_constraint_002(keygen, length):
	key_constraint = ord_(keygen[2]) + ord_(keygen[3])
	return mod_(key_constraint, 36) == 0x18

def key_constraint_003(keygen, length):
	key_constraint = ord_(keygen[2]) + ord_(keygen[0])
	return mod_(key_constraint, 36) == 0x6


def key_constraint_004(keygen, length):
	key_constraint = ord_(keygen[1]) + ord_(keygen[3]) + ord_(keygen[5])
	return mod_(key_constraint, 36) == 0x4


def key_constraint_005(keygen, length):
	key_constraint = ord_(keygen[2]) + ord_(keygen[4]) + ord_(keygen[6])
	return mod_(key_constraint, 36) == 0xd


def key_constraint_006(keygen, length):
	key_constraint = ord_(keygen[3]) + ord_(keygen[4]) + ord_(keygen[5])
	return mod_(key_constraint, 36) == 0x16


def key_constraint_007(keygen, length):
	key_constraint = ord_(keygen[6]) + ord_(keygen[8]) + ord_(keygen[10])
	return mod_(key_constraint, 36) == 0x1f


def key_constraint_008(keygen, length):
	key_constraint = ord_(keygen[1]) + ord_(keygen[4]) + ord_(keygen[7])
	return mod_(key_constraint, 36) == 0x7


def key_constraint_009(keygen, length):
	key_constraint = ord_(keygen[9]) + ord_(keygen[12]) + ord_(keygen[15])
	return mod_(key_constraint, 36) == 0x14


def key_constraint_010(keygen, length):
	key_constraint = ord_(keygen[13]) + ord_(keygen[14]) + ord_(keygen[15])
	return mod_(key_constraint, 36) == 0xc

def key_constraint_011(keygen, length):
	key_constraint = ord_(keygen[8]) + ord_(keygen[9]) + ord_(keygen[10])
	return mod_(key_constraint, 36) == 0x1b


def key_constraint_012(keygen, length):
	key_constraint = ord_(keygen[7]) + ord_(keygen[12]) + ord_(keygen[13])
	return mod_(key_constraint, 36) == 0x17





keygen = IntVector("keygen", 16)
solve = Solver()

key_constraint_01 = (keygen[0]) + (keygen[1])
solve.add(key_constraint_01 % 36 == 0xe)

key_constraint_02 = (keygen[2]) + (keygen[3])
solve.add(key_constraint_02 % 36 == 0x18)

key_constraint_03 = (keygen[2]) + (keygen[0])
solve.add(key_constraint_03 % 36 == 0x6)

key_constraint_04 = (keygen[3]) + (keygen[1]) + (keygen[5])
solve.add(key_constraint_04 % 36 == 0x4)

key_constraint_05 = (keygen[2]) + (keygen[4]) + (keygen[6])
solve.add(key_constraint_05 % 36 == 0xd)

key_constraint_06 = (keygen[3]) + (keygen[4]) + (keygen[5])
solve.add(key_constraint_06 % 36 == 0x16)

key_constraint_07 = (keygen[6]) + (keygen[8]) + (keygen[10])
solve.add(key_constraint_07 % 36 == 0x1f)

key_constraint_08 = (keygen[1]) + (keygen[4]) + (keygen[7])
solve.add(key_constraint_08 % 36 == 0x7)

key_constraint_09 = (keygen[9]) + (keygen[12]) + (keygen[15])
solve.add(key_constraint_09 % 36 == 0x14)

key_constraint_10 = (keygen[13]) + (keygen[14]) + (keygen[15])
solve.add(key_constraint_10 % 36 == 0xc)

key_constraint_11 = (keygen[8]) + (keygen[9]) + (keygen[10])
solve.add(key_constraint_11 % 36 == 0x1b)

key_constraint_12 = (keygen[7]) + (keygen[12]) + (keygen[13])
solve.add(key_constraint_12 % 36 == 0x17)




key = []

print "\n"
print "[*] Possible values -> :"
print "\n" 

for i in range(16):
		solve.add(keygen[i] >= 0)
		solve.add(keygen[i] < 35)

if solve.check():
	flag = solve.model()
	for i in range(16):
		ords = flag[keygen[i]].as_long()
		print " " + str(chr(ords + 55)), str(chr(ords + 48)) #we get the possible characters using from the values with chr function


print "\n"
print " [*] check -> :"
print "\n"

		
def checkResult():
		#I checked all the values manually, keep the right ones and change te wrong ones until i got a string that it fulfill all the 12 constraints 
		#0E6IW8BQK7M0I1GH --> 001/006 correct ( 0 1 2 3 4 5 6 )
		#0E6IW8BXR7T7P8NO --> 001/009-011 correct  ( 0 1 2 3 4 5 6 7 8 9 10 12 15)
		#0E6IW8BXR7T0P1NO --> 001/012 correct ( 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15)
		lastKey = "0E6IW8BXR7T0P1NO"
		print "[*] Running calculations on key : " + str(lastKey) + " .... "
		if (key_constraint_001(lastKey, 0)):
				print " [*] 001 Success"
				time.sleep(1)	

		if (key_constraint_002(lastKey, 0)):
				print " [*] 002 Success"
				time.sleep(1)	

		if (key_constraint_003(lastKey, 0)):
				print " [*] 003 Success"
				time.sleep(1)	

		if (key_constraint_004(lastKey, 0)):
				print " [*] 004 Success"
				time.sleep(1)	

		if (key_constraint_005(lastKey, 0)):
				print " [*] 005 Success"
				time.sleep(1)	

		if (key_constraint_006(lastKey, 0)):
				print " [*] 006 Success"
				time.sleep(1)	

		if (key_constraint_007(lastKey, 0)):
				print " [*] 007 Success"
				time.sleep(1)	

		if (key_constraint_008(lastKey, 0)):
				print " [*] 008 Success"
				time.sleep(1)	

		if (key_constraint_009(lastKey, 0)):
				print " [*] 009 Success"
				time.sleep(1)	

		if (key_constraint_010(lastKey, 0)):
				print " [*] 010 Success"
				time.sleep(1)	

		if (key_constraint_011(lastKey, 0)):
				print " [*] 011 Success"
				time.sleep(1)	

		if (key_constraint_012(lastKey, 0)):
				print " [*] 012 Success"
				time.sleep(1)	

		if (key_constraint_001(lastKey, 0) and 
	        key_constraint_002(lastKey, 0) and 
	        key_constraint_003(lastKey, 0) and 
	        key_constraint_004(lastKey, 0) and 
	        key_constraint_005(lastKey, 0) and 
	        key_constraint_006(lastKey, 0) and 
	        key_constraint_007(lastKey, 0) and 
	        key_constraint_008(lastKey, 0) and 
	        key_constraint_009(lastKey, 0) and 
	        key_constraint_010(lastKey, 0) and 
	        key_constraint_011(lastKey, 0) and 
	        key_constraint_012(lastKey, 0)):
			print " [*] Key ( " + str(lastKey) + " ) : is valid !"
			print "\n" 
			os.system("./activate " + str(lastKey))
		else:
			print " [*] Key ( " + str(lastKey) + " ) is not valid !"



checkResult()