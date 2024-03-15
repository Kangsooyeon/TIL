T = int(input())
for tc in range(1, T+1):
    S, N = input().split()
    N = int(N)
    now = set([S])
    next = set()
    for _ in range(N):
        while now:
            tmp=now.pop()
            tmp = list(tmp)
            for i in range(len(S)-1):
                for j in range(i+1, len(S)):
                    tmp[i], tmp[j] = tmp[j], tmp[i]
                    next.add(''.join(tmp))
                    tmp[i], tmp[j] = tmp[j], tmp[i]
        now, next = next, now
    result = max(now)
    print(f'#{tc} {result}')















# T = int(input())
#
# for t in range(1, T + 1):
#     numbers, count = input().split()
#     count = int(count)
#     nums = set([numbers])
#     SET = set()
#     for _ in range(count):
#         while nums:
#             n = nums.pop()
#             n = list(n)
#             for i in range(len(numbers)):
#                 for j in range(i + 1, len(numbers)):
#                     n[i], n[j] = n[j], n[i]
#                     SET.add(''.join(n))
#                     n[i], n[j] = n[j], n[i]
#         nums, SET = SET, nums
#
#     result = max(nums)
#     print(f'#{t} {result}')

















# T = int(input())
#
# for t in range(1, T + 1):
#     numbers, count = input().split()
#     count = int(count)
#     nums = set([numbers])
#     SET = set()
#     for _ in range(count):
#         while nums:
#             n = nums.pop()
#             n = list(n)
#             for i in range(len(numbers)):
#                 for j in range(i + 1, len(numbers)):
#                     n[i], n[j] = n[j], n[i]
#                     SET.add(''.join(n))
#                     n[i], n[j] = n[j], n[i]
#         nums, SET = SET, nums
#
#     result = max(nums)
#     print(f'#{t} {result}')

