# Observation: if N < 99 => ans = 99,

N = int(input())
l = N
r = N

while l%100 != 99 and r%100 !=99:
    if l > 1:
        l -= 1 
    r += 1 

if l%100 == 99 and r%100 == 99:
    print(r)
elif l%100 == 99:
    print(l)
else:
    print(r)


