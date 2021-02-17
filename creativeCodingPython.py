from tkinter import *
from urllib.request import urlopen, Request
import urllib
import bs4
from tkinter import messagebox


city = ['서울','경기','강원','충남','충북','전남','전북','경남','경북','제주']

seoul = ['종로구','중구','용산구','성동구','광진구','동대문구','중랑구',
            '성북구','강북구','도봉구','노원구','은평구','서대문구','마포구','양천구','강서구']

gyeoggi = ['수원시', '성남시','의정부시', '안양시',  '부천시', '광명시', '평택시', '동두천시', '안산시','고양시', '과천시', '구리시'
            , '남양주시', '오산시', '시흥시', '군포시', '의왕시', '하남시', '용인시','파주시', '이천시', '안성시', '김포시'
            , '화성시', '광주시', '양주시', '포천시', '여주시', '연천군', '가평군', '양평군']

gangwon= ['춘천시', '원주시', '강릉시', '동해시', '태백시', '속초시', '삼척시', '홍천군'
            , '횡성군', '영월군', '평창군', '정선군', '철원군', '화천군', '양구군', '인제군'
            , '고성군', '양양군']
chungnam = ['천안시', '공주시', '보령시', '아산시', '서산시', '논산시', '계룡시', '당진시', '금산군',
           '부여군', '서천군', '청양군', '홍성군', '예산군', '태안군']

chungbuk = ['청주시',  '충주시', '제천시', '보은군', '옥천군', '영동군', '증평군', '진천군', '괴산군',
            '음성군', '단양군']

jeonnam = ['목포시', '여수시', '순천시', '나주시', '광양시', '담양군', '곡성군', '구례군', '고흥군', '보성군'
           , '화순군', '장흥군', '강진군', '해남군', '영암군', '무안군', '함평군', '영광군', '장성군', '완도군'
           , '진도군', '신안군']

jeonbuk = ['전주시', '군산시', '익산시', '정읍시', '남원시', '김제시', '완주군', '진안군', '무주군', '장수군',
           '임실군', '순창군', '고창군', '부안군']

gyeongnam=['창원시', '진주시', '통영시', '사천시', '김해시','마산시', '밀양시', '거제시', '양산시', '의령군', '함안군', '창녕군', '고성군'
            , '남해군', '하동군', '산청군', '함양군', '거창군', '합천군']

gyeongbuk = ['포항시', '경주시', '김천시', '안동시', '구미시', '영주시', '영천시', '상주시', '문경시', '경산시', '군위군', '의성군',
             '청송군', '영양군', '영덕군', '청도군', '고령군'
            , '성주군', '칠곡군', '예천군', '봉화군', '울진군', '울릉군']

jeju = ['제주시','서귀포시']



def clickListBox(event):         #리스트박스를 클릭했을때
    if (cityBox.curselection() == ()):
        return

    # 클릭시 클릭된거 이름 가져옴.
    cityName = str(cityBox.get(cityBox.curselection()))

    # 이름과  비교한담에 채우기.
    if cityName == '서울':
        fillListBox(seoul)
    if cityName == '경기':
        fillListBox(gyeoggi)
    if cityName == '강원' :
        fillListBox(gangwon)
    if cityName == '경남' :
        fillListBox(gyeongnam)
    if cityName == '경북' :
        fillListBox(gyeongbuk)
    if cityName == '충북':
        fillListBox(chungbuk)
    if cityName == '충남':
        fillListBox(chungnam)
    if cityName == '전남':
        fillListBox(jeonnam)
    if cityName == '전북':
        fillListBox(jeonbuk)
    if cityName == '제주':
        fillListBox(jeju)
        
def fillListBox(area): #도시 채우는 함수
    global  cityBox, fileListBox

    #삭제하고 다시 넣기.
    cityBox.delete(0, END)
    fileListBox.delete(0, END)

    #지역리스트
    for item in city:
        cityBox.insert(END, item)

    #도시리스트
    if not(area == None):
        for item in area:
            fileListBox.insert(END, item)

def weather(event): #날씨 불러오는 함수
    if (fileListBox.curselection() == ()):
        return

    loc = str(fileListBox.get(fileListBox.curselection()))

    enc_loc = urllib.parse.quote(loc + '+날씨')

    url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_loc

    req = Request(url)
    page = urlopen(req)
    html = page.read()
    soup = bs4.BeautifulSoup(html,'html.parser')

    messagebox.showinfo(title='날씨 정보', message= '현재' + loc + ' 날씨는 '
                        + soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text + '도 입니다.')

window = None
cityBox, fileListBox = None, None


## 메인 코드 부분 ##
window = Tk()
window.title("지역 날씨")
window.geometry('500x500')



cityBox = Listbox(window) #도를 보여주는 리스트박스
cityBox.bind('<<ListboxSelect>>', clickListBox)
cityBox.pack(side=LEFT, fill=BOTH, expand=1)

fileListBox = Listbox(window) #시를 보여주는 리스트박스 
fileListBox.bind("<<ListboxSelect>>",weather)
fileListBox.pack(side=RIGHT, fill=BOTH, expand=2)



fillListBox(None)  # 초기엔 아무것도 안띄우기.(오른쪽 리스트 박스)

window.mainloop()
