T = int(input())

prime_number = [2,3,5,7,11]

for test_case in range(1,T+1):
    case = int(input())
    li = [0]*5
    i=0

    while i<5:
        if case % prime_number[i] ==0:
            li[i] += 1
            case //= prime_number[i]
        else:
            i+=1

    print('#'+str(test_case),*li)
