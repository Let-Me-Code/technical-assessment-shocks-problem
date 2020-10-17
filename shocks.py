from collections import defaultdict
 
def sockMerchant(n, ar):
    d = defaultdict(int)
 
    for k in ar:
        d[k] += 1
         
    cnt = 0
    for ele in d.values():
        cnt += ele // 2
         
    return cnt
n = int(input())
ar = list(map(int,input().split()))
print(sockMerchant(n,ar))
