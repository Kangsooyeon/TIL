from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]

nums = list(range(1,N+1))
combi = list(combinations(nums, N//2))
result = float('inf')

start_team=combi[:len(combi)//2]
link_team=combi[:-(len(combi)//2+1):-1]

for i in range(len(start_team)): #팀 능력치 차이 구하기
    start = list(combinations(start_team[i], 2))
    link = list(combinations(link_team[i], 2))
    start_score=0
    link_score=0

    for j in range(len(start)):
        s1=start[j][0]-1
        s2=start[j][1]-1
        l1=link[j][0]-1
        l2 = link[j][1]-1

        start_score+=li[s1][s2]+li[s2][s1]
        link_score+=li[l1][l2]+li[l2][l1]

    diff = abs(start_score - link_score)
    if result > diff:
        result = diff

print(result)