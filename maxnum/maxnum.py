f = open('input.txt')
n=f.read()
n=n.split('\n')
for ln in n:
    ln = ln.split(' ')
    a = int(ln[0])
    b = int(ln[1])
    c = int(ln[2])
    ans = str(max(a, b, c))
ansv = '\n'.join(ans)

with open('output.txt','w') as f:
    f.write(ansv)