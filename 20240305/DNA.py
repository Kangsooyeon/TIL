import sys
input = sys.stdin.readline

dic = {'A':0, 'C':1, 'G':2, 'T':3}

S, M = map(int, input().split())
li = list(input())
dna = list(map(int, input().split()))
dna_cnt=[0]*4
cnt = 0

for i in range(M):
    dna_cnt[dic[li[i]]] += 1

tmp_cnt = 0
for d in range(4):
    if dna_cnt[d] >= dna[d]:
        tmp_cnt += 1
if tmp_cnt == 4:
    cnt += 1


for j in range(M,S):
    dna_cnt[dic[li[j - M]]]-=1
    dna_cnt[dic[li[j]]] += 1

    tmp_cnt=0
    for d in range(4):
        if dna_cnt[d]>=dna[d]:
            tmp_cnt+=1
    if tmp_cnt==4:
        cnt+=1

print(cnt)