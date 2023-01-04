a=input()
l=[]
for i in a:
    c=ord(i)
    l.append(c)
print(chr(min(l))*(l.count(max(l))))
