T = int(input())
for test_case in range(1,T+1):
    num = int(input())
    c = [0]*12  #각 자리 수를 추출하여 0~9의 개수를 누적할 리스트(인덱스 연산을 위해 +2칸 추가)

    for i in range(6):
        c[num%10] +=1 #일의 자리 수에 해당하는 숫자 카운팅
        num //=10 #다음 자리 수로 넘어가기 위한 작업

    i = 0
    tri = rn = 0

    while i < 10:
        if c[i] >= 3 : #triplete 조사 후 데이터 삭제
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: #run 조사 후 데이터 삭제
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            rn += 1
            continue
        i += 1

    if rn + tri == 2 :
        print(f'#{test_case} true')
    else:
        print(f'#{test_case} false')