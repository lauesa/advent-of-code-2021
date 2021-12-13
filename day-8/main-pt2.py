# wiring
#  dddd
# e    a
# e    a
#  ffff
# g    b
# g    b
#  cccc
#        a,b,c,d,e,f,g
num = { (1,1,1,1,1,0,1): '0',
        (1,1,0,0,0,0,0): '1',
        (1,0,1,1,0,1,1): '2',
        (1,1,1,1,0,1,0): '3',
        (1,1,0,0,1,1,0): '4',
        (0,1,1,1,1,1,0): '5',
        (0,1,1,1,1,1,1): '6',
        (1,1,0,1,0,0,0): '7',
        (1,1,1,1,1,1,1): '8',
        (1,1,0,1,1,1,0): '9',
        (1,1,0,0,1,0,0): '4'}

def decoder(live):
    st = ''
    for disp in live:
        print(disp)
        seg = [0] * 7
        for sec in disp:
            seg[ord(sec) - 97] = 1
        st += num[tuple(seg)]
    return int(st)
        
with open("input.txt") as file:
    for i, line in enumerate(file):
        first, last = line.strip().split('|')
        first = first.strip().split(' ')
        last = last.strip().split(' ')
        print (decoder(last))