# 데이터 시각화 프로젝트
## 프로젝트 진행 기록
### 1. 주제 정하는 과정
2월 1일, 공공 데이터들을 확인하면서 어떤 데이터들로 무슨 방향의 인사이트를 뽑을지 오래 고민했습니다.  
그리고 그런 고민도 있었지만 팀원 5명이 기한 3일동안 진행할 프로젝트 계획을 세우기가 쉽지 않아 애를 먹었습니다.   
주제 잡기가 어려워 지호님께서 관련 경험이 있는 지인 분께 조언을 구하고 디렉터 분께 조언을 얻어 시각화 할 때 위치, 지리 정보를 이용하는 편이 시각화하기에 가장 좋을 것이라고 판단하고 아침에 나누었던 의견들 중에서 교통관련 주제가 제일 적합하다고 의견이 모였습니다.   
'어린이 보호 구역에서 벗어난 위치에 어린이 사고가 더 많이 일어나지 않을까?' 에서 노인 교통안전정보 시각화로 주제가 정해졌는데 문제는 사용할 수 있는 공공 데이터의 상태가 전처리를 거쳐야 시각화를 할 수 있는 상태였습니다.  
### 2. 데이터 전처리 과정
노인 보호 구역 반경 데이터, 노인 사고 위치 정보 그리고 사고 차량 정보와 어떤 이유로 사고가 벌어졌는지에 대한 데이터였습니다. 후자의 데이터는 데이터가 웹페이지에 두 개의 열에 데이터가 담겨 있고 세번째 열에 링크가 있어 각 행의 개수만큼 링크를 눌러 창을 띄워야만 데이터를 하나하나 확인할 수 있었습니다.  
그래서 selenium 라이브러리를 이용해 여기에 쓸 크롤링 툴을 만드려고 했는데 html 문서 구성이 크롤링을 하기에 까다로워 문제가 생기게 됩니다. 웹 페이지가 열리면 그래프 데이터가 페이지에 다 띄워지게 되는데 그래도 한 화면에 나올 수 있는 데이터만 가져올 수 있어서, 한 화면에 그래프 row가 12개가 나올 수 있으면 12개의 데이터를 스크래핑한 후 다음 12개 row가 화면에 담기게 끔 스크롤을 조작할 수 있게 설정해야하는 등의 문제였습니다.  
전자의 두 개의 데이터는 건물이름과 그 앞, 뒤, 혹은 그런 표현 없이 그 근처라는 뜻처럼 보이는 도로 표현으로 되어 있어 지도를 그리고 데이터를 시각화하기 위해선 위도, 경도 데이터를 하나하나 확인하고 데이터를 구축하는 작업이 필요했습니다. 
처음엔 두명은 크롤링을 맡고 나머지는 데이터 구축을 진행하다가, 크롤링 작업이 생각보다 많은 시간이 투자될 업무라고 판단했고 또 이 프로젝트에 해당 데이터가 어떤 우선순위를 갖는지 판단해서 다른 팀원들에게 합류해 위도, 경도 데이터 구축을 시작하게 됩니다.  
팀원: 김경목, 윤규헌, 맹지호, 민병창, 신제우