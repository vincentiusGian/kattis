# Written by vncntgii

n, d = list(map(int, input().split()))

notes = []
for _ in range(n):
   a = int(input())
   notes.append(a)

notes = sorted(notes)
ans = 1
start = notes[0]
for note in notes[1:]:
    if note - start > d:
        ans += 1
        start = note


print(ans)
 
