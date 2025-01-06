
n = int(input())
st = list(map(int, input().split()))

if st == st[::-1]:
    print("YES")
else:
    print("NO")
    
