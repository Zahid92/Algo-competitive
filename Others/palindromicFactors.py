def palindrome(n):
    s=str(n)
    f,l=0,len(s)-1
    while(f<l):
        if s[f]!=s[l]:
            return False
        f+=1
        l-=1
    return True


d={1:1,2:2,3:2,4:3,5:2,6:4}
t=int(input())
for _ in range(1,t+1):
    a=int(input())
    c=0
    k=1
    root=int(a**0.5)
    while k<=root:
        if a % k==0:
            if a/k==k:
                if palindrome(k):
                    c+=1
            else:
                if palindrome(k):
                    c+=1
                if palindrome(a//k):
                    c+=1
        k+=1
    d[a]=c
    print(f"Case# {_}: {c}")


