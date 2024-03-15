import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li = list(map(int, input().split()))

start, end = 0, 1
cnt=0
while (start<=end and end <=N):
    tmp = sum(li[start:end])
    if tmp <M:
        end +=1
    elif tmp>M:
        start +=1
    else:
        cnt +=1
        end +=1

print(cnt)