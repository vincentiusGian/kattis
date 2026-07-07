# Written by Vincent

MOD = int(1e9+7)

s = input()
one = 0 
branch = 1
inv = 0 

for c in s:
    if c == "1":
        one = (one+branch) % MOD
    elif c == "0":   
        inv = (inv+one)%MOD
    else:
        inv = (2*inv + one)%MOD
        one = (2*one + branch)%MOD 
        branch = 2*branch % MOD

print(inv)