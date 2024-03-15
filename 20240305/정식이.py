T = int(input())
for tc in range(1, T + 1):
    s2 = list(map(str, input()))
    s3 = list(map(str, input()))

    for i in range(len(s2)):
        s2[i] = str(1 - int(s2[i]))
        s2_0b = '0b' + ''.join(s2)
        s2_10 = int(s2_0b, 2)  # 십진수 변환
        s2_10_save = s2_10

        # 3진수 변환
        s3_tmp = ''
        while s2_10_save > 0:
            s2_10_save, mod = divmod(s2_10_save, 3)
            s3_tmp += str(mod)
        s3_tmp = s3_tmp[::-1]
        s3_tmp = s3_tmp.zfill(len(s3))  # 앞에 0 채워서 자리수 맞추기

        # 3진수 변환 후 기존 s3와 1개 다른지 확인
        cnt = 0
        for j in range(len(s3)):
            if s3_tmp[j] != s3[j]:
                cnt += 1
            if cnt > 1:
                break

        if cnt == 1:  # 1개만 다르면 종료
            break
        else:
            s2[i] = str(1 - int(s2[i]))  # 원상 복구

    print(f'#{tc}', s2_10)