# li=[-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# n=len(li)
#
#
# def get_count(tar):
#     result = []
#     for i in range(n):
#         if tar&0x1:
#             result.append(li[i])
#         tar>>=1
#
#     if result and sum(result)==0:
#         print(result)
#
#
# for tar in range(1<<n):
#     get_count(tar)

def get_count(tar):
    global cnt
    SUM = 0
    for i in range(N):
        if SUM>K:
            return

        if tar&0x1:
            SUM+=li[i]
        tar>>=1

    if SUM==K:
        cnt+=1

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    li = list(map(int, input().split()))
    cnt = 0

    for tar in range(1 << N):
        get_count(tar)

    print(f'#{tc} {cnt}')





