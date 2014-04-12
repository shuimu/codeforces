def run():
    n,k = map(int, raw_input().split())
    if k == 0 and n == 1:
        print 1
        return 
    if n/2 > k or n == 1:
        print "-1"
        return 
    a = k - n/2 + 1
    ans = list()
    ans.append(a)
    ans.append(a*2)
    for i in range(2,n):
        ans.append(a*2+i) 
    print " ".join(map(str,ans))

run()
