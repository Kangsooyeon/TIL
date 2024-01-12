Git 이란? <br>
: 분산 버전 관리 시스템<br><br>

단계별 저장<br>
업무 쪼개기 / 단계 생성<br><br>

어제는 API는 리모콘이다!!!<br>
✨✨ add commit push ✨✨<br><br>

working directory (로컬 - 내 컴퓨터)<br>
staging area (스테이지 - 무대)<br>
repository (저장소 - 깃허브)<br>

- add : 스테이지 추가 (로컬에서 스테이지로)
- commit : 스테이지에 올라간 파일에 쪽지를 적는다.
- push : (스테이지 + 커밋)을 깃허브로

커밋이 없으면 푸시가 되지 않음!!<br><br>

git init : 초기화 (한번만 하면 됨)<br>
ls -a : 내가 갈 수 있는 전체 목록을 보여줘<br>
ls -al : 리스트 형식으로 보여줘<br>
📌git status : 상태 확인<br>

📌 탭키 활용 (자동 완성)<br><br>

git add<br>
git commit<br>
esc -> :wq (저장하고 나가기) :q (그냥 나가기)<br><br>

git commit -m "first commit"<br>

history 과거 쳤던 코드 확인 가능<br><br>

📌 git log 커밋 기록 목록 확인 가능<br><br>

git remote add origin https://github.com/Kangsooyeon/study.git (깃허브 연결)<br>

git remote -v (깃허브 연결 확인)<br>

git push<br>

git push --set-upstream origin master<br>