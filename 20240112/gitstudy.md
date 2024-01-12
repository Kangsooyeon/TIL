개발자의 꿀팁 -> 무한대로 늘려봐라
git add 취소하기 -> git reset 파일명
git add . (.은 현재 폴더, 현재 폴더에 있는 파일 모두 add)

git commit 메세지 변경하기 -> git commit --amend
i 를 누르면 하단에 '--INSERT--' 모드로 전환 -> 수정 가능
ESC를 누르면 '--INSERT--'모드 종료 -> :wq (저장하고 나가기)
git log (커밋 메세지 확인)
gi remote -v (원격 저장소 별명 확인)

clone을 하면 remote를 안해도 이미 주소가 연결되어 있음
-> git push 바로 사용 가능

1. git init / 2. remote / 3. upstream  세 가지는 안 해도 됨!!

- add : '로컬' -> '스테이지' 로 '변경사항' 내용 추가
- commit : 스테이지에서 '변경사항'에 쪽지/메모 남긴다.
- push : ‘스테이지’에 있는 ‘변경사항’ 과 그에 대한 쪽지를 원격 저장소로 업로드

commit 메세지도 잘 써야한다.
좋은 커밋이란? 어디에 무엇을 수정했는지

- pull : 용량이 클 때 유용
- clone : 용량이 작을 때 유용

gitignore : git에서 무시할 파일 모음
[gitignore.io](http://gitignore.io/) 에서 다양한 상황에서의 .gitignore 파일들이 존재함