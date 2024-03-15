T = int(input())
for _ in range(T):
    S = input()
    str1='..#..'
    str2='.#.#.'
    str3='#.'+S[0]+'.#'

    if len(S)>=2:
        for i in range(1,len(S)):
            str1 = str1[:4]+str1
            str2 = str2[:4]+str2
            str3 = str3[:-1]+'#.'+S[i]+'.#'

    print(str1)
    print(str2)
    print(str3)
    print(str2)
    print(str1)