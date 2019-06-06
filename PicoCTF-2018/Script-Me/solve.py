from pwn import *
import time




print('''
                              [ Solved by Th3_w1ck3d ]
                    PicoCTF-challenges ==> Name : [ Script me ] 
''')

print "......"
time.sleep(2)

def get_formula(string):
    length = 0
    max_lenght = 0

    for i in string:
        if i == '(':
            length += 1

        if i == ')':
            length -= 1

        if length > max_lenght:
            max_lenght = length

    return max_lenght

def answer(answer1, answer2):
    a1 = get_formula(answer1)
    a2 = get_formula(answer2)

    if a1 < a2:
    	print "absorb-left"
        return answer2[0] + answer1 + answer2[1:]
    elif a1 == a2:
    	print 'combine'
        return answer1 + answer2
    else:
    	print "absorb-right"
        return answer1[:-1] + answer2 + answer1[-1]











def main():
    r = remote('2018shell2.picoctf.com', 1542)

    formule_number = 1
    while True:
        lines = r.recvrepeat(1).split('\n')
        
        print '\n'.join(lines)

        if 'pico' in '\n'.join(lines):
            break

        q = lines[-3].split('=')[0].strip()
        log.info('Got formula #{}: {}'.format(formule_number, q))
        q = q.split()

        while len(q) > 1:
            answer1 = q.pop(0)
            q.pop(0)
            answer2 = q.pop(0)

            n = answer(answer1, answer2)
            print n
            q = [n] + q

        log.info('Sending: {}'.format(q[0]))
        r.sendline(q[0])

        ru = r.recvuntil('\n')

        print ru

        formule_number += 1

if __name__ == '__main__':
    main()




##################################################
##### picoCTF{5cr1pt1nG_l1k3_4_pRo_0466cdd7} #####
##################################################
