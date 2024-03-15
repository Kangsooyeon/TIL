def babygin(counts, index):
    if counts[index] == 3:
        return True

    for i in (index - 2, index - 1, index):
        if 0 <= i <= 7 and counts[i] > 0 and counts[i + 1] > 0 and counts[i + 2] > 0:
            return True
    return False

T = int(input())

for t in range(T):
    lst = list(map(int, input().split()))
    counts1 = [0] * 10
    counts2 = [0] * 10

    result = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            counts1[lst[i]] = counts1[lst[i]] + 1
            if babygin(counts1, lst[i]):
                result = 1
                break
        else:
            counts2[lst[i]] = counts2[lst[i]] + 1
            if babygin(counts2, lst[i]):
                result = 2
                break

    print(f'#{t + 1} {result}')