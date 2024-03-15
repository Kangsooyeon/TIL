T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    answer = list(map(int, input().split()))
    student = [list(map(int, input().split())) for _ in range(N)]
    score_list=[]
    score_sum = []

    for i in range(N):
        score = 0
        score_list = []
        for j in range(M):
            if student[i][j]==answer[j]:
                if score>0:
                    score+=1
                else:
                    score =1
            else:
                score = 0

            score_list.append(score)
        score_sum.append(sum(score_list))

    result = max(score_sum) - min(score_sum)
    print(f'#{tc} {result}')