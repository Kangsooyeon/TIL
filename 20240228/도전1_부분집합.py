arr=['A','B','C','D','E']
n=len(arr)

def get_count(tar):
    cnt =0
    for i in range(n):
        #1비트 1인지 확인
        if tar&0x1:
            cnt+=1
        #오른쪽 비트 1개씩 제거
        tar>>=1
    return cnt

result =0
for tar in range(1<<n):
    if get_count(tar) >=2: #2명 이상이라면
        result +=1
print(result)