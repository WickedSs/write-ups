from hashlib import sha512
import sys
from z3 import *
import os


solve = Solver()
with open('map2.txt', 'r') as f:
	cipher, chalbox = eval(f.read())

length, gates, check = chalbox
b = [Bool('x' + str(i)) for i in range(length)]

for name, args in gates:
	if name == 'true':
	    b.append(True)
	else:
	    u1 = Xor(b[args[0][0]], args[0][1])
	    u2 = Xor(b[args[1][0]], args[1][1])
	    if name == 'or':
	        b.append(Or(u1, u2))
	    elif name == 'xor':
	        b.append(Xor(u1, u2))

solve = Solver()
solve.add(Xor(b[check[0]], check[1]))

if solve.check():
	model = solve.model()

print list(reversed(b[:length]))
keyencoded = []
keydecoded = []

for i in range(64):
	keyencoded.append(model[b[i]])


for each in keyencoded:
	if each == True:
		keydecoded.append(1)
	else:
		keydecoded.append(0)


binary = "".join(map(str, keydecoded))
print "Binary code --> " + str(binary)

key = 0
for val in reversed(b[:length]):
    key *= 2
    key += bool(model[val])


print "Decoded Key --> " + str(key)
print "\n"
print "-------------- Getting flag ---------------- "
print "\n"
os.system("python decrypt.py " + str(key) + " map2.txt")