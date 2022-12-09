## 1. 프로젝트 설명

### - 기획 의도

- MOVIEDIVE 라는 서비스 명은 사용자들이 우리 서비스에 빠지며 영화 감상에 푹 빠지게 한다는 의미.

- 커뮤니티 서비스와 부가적인 재미 요소들에 중점을 둔 서비스. 



### - 개발 기간

- 2022.11.16 ~ 2022.11.25 (10일)



### - 기능 구현

#### 1. `Diveview`

- three.js 객체를 이용해 영화 포스터와 별이 떠 있는 우주 공간을 구현
- 스크롤업하여 화면 중앙, 원점에 있는 로고와 구형 mesh를 향해 다이빙 하는 효과 구현



#### 2. `Movies`

* 최신 영화 10개 중 랜덤으로 트레일러 재생
* 최신 영화, 장르별 추천 영화, 인기 컬렉션 순으로 캐러셀을 이용하여 트레일러 아래 배치



##### - Movie Detail

- OTT 바로가기
- Youtube API 
- 좋아요



#### 3. Collections

##### - Collection Main

- 유저가 좋아요 한 컬렉션, 전체 컬렉션 목록을 인기순으로 나열

##### - Create Collection

- Search Bar를 활용하여 input 에 따라 영화를 검색하여 컬렉션에 추가하는 기능 구현
- 컬렉션 영화 선택 후 Title과 Description 작성 

##### - Collection Detail

- 컬렉션 제목, 설명, 영화 목록 나열 
- 각 영화 클릭하면 Movie Detail Modal 나타남
- 댓글, 좋아요 기능 구현
- 컬렉션 작성자만 수정, 삭제 가능



#### 4. Community(Reviews)

* 리뷰를 스레드 형식으로 구성하여 제목 및 내용을 한 번에 볼 수 있어 가독성이 좋고 최신순 혹은 좋아요 순으로 탐색 가능.
* 리뷰 검색 기능을 활용하여 검색창에 검색한 특정 영화 리뷰만 조회 가능
* 리뷰 작성 시 작성하고자 하는 영화를 제목으로 검색하여 선택 가능
* 리뷰 좋아요, 댓글 구현



#### 5. Game

- Node.js 로 Socket 통신을 활용하여 유저들 간 소통이 가능한 실시간 게임 기능 구현 
- 실시간 접속자 명단 기능 구현
- 방 만들기 기능 구현
- 인물퀴즈, OX 퀴즈 
- 대기실에서 실시간 채팅 기능 구현



#### 6. DEEPDIVE (추천 페이지)

- 아이템 기반 협업 필터링과 유저 기반 협업 필터링을 이용한 영화 추천 알고리즘 설계
- Three.js를 이용해 스크롤 반응형 3D 인터랙션 화면 구성으로 사용자에게 시각적인 재미 제공



#### 7. Accounts

- 로그인, 회원가입, 로그아웃, 비밀번호 변경, 회원 탈퇴 기능 구현
- AWS S3를 활용한 프로필 이미지 변경 기능, 닉네임, 상태메시지 기능 구현
- 마이페이지를 SNS처럼 만들어 유저 개인의 영화 보관함같은 역할을 제공
- 좋아요 한 영화, 내가 만든 컬렉션, 내가 쓴 리뷰 선택하여 조회 가능
- 팔로우, 팔로잉 기능 구현



### - 기술 스택

#### 1) 개발 환경

- IDE : ![Visual_Studio_Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)1.73. 1
- DB : ![MySQL](https://img.shields.io/badge/MySQL-003545?style=for-the-badge&logo=mysql&logoColor=white) 8.0.30
- UI & UX : ![Figma](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white) 
- Server: ![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white) ![S3](https://img.shields.io/badge/S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white)![ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)![NGINX](https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)



#### 2) 상세

- Backend : ![PYTHON](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white)![NODE.JS](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=Node.js&logoColor=white)![DJANGO](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)![SOCKET.IO](https://img.shields.io/badge/Socket.io-010101?style=for-the-badge&logo=socket.io&logoColor=white)

- Frontend : ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)![CSS3](https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white)![JAVASCRIPT](https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white)![Vue.js](https://img.shields.io/badge/vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white) 3.2.39 ![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white)![bootstrap](https://img.shields.io/badge/BootStrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white) 5.2.1

- Data : ![PYTHON](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white)



## 2. KPT

### 1) Keep

- Three.js, AWS, Socket.io 등 접해본 적 없는 새로운 기술들을 시도한 열린 자세와 도전 정신
- 명세에서 요구한 프로젝트의 기본 기능은 모두 완성
- 첫 프로젝트에서 명확한 역할 구분 대신 모든 파트에서 협업
- 의사소통이 원활
- 마음 상하는 일이 없었다 !



### 2) Problem

- **완성도가 낮다**
- 전체 프로젝트 기간에 비해 기획 기간이 길어 프로그래밍 기간이 부족했음. 타임라인 설계가 아쉬웠고 기획 서류 작성이 미비했다고 판단됨.
- 에러가 생겼을 때 해결하는 방법이 미숙



### 3) Try

- 현재 진행 속도를 파악해서 데드라인에 맞추어 완성할 수 있게 유동적으로 계획을 수정. (포기할건 포기..)
- 기획서 세부사항을 제대로 만들어 두기 !
- 능력껏 하기 위해 내 능력을 미리 더 키우자 !!! 



