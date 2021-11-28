from main import add, sub, mul, tab

print(add(12, 56))
print(sub(12, 56))
print(mul(3, 4))

ta = tab(5)
for i,t in enumerate(ta):
    print(str(i)+' x 5 = '+str(t))