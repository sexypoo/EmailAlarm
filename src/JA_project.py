from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.remote.switch_to import SwitchTo
from soupsieve import select

from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app)

mongodb_client = PyMongo(app, uri="mongodb+srv://goeun:goeunrealpassword@cluster0.5xfl6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = mongodb_client.db

data=db.tests

#분야                                                                                                                  0!0
전체전체1 = 'https://www.youth.go.kr/youth/act/actSearch/allActSearchLst.yt?sCrtfcText=&sSttemntText=&sort=&order=&page=1&rows=&kCrtfcSn=&kFcltySn=&kSnOne=&kProgrmseCode=&kSnTwo=&kSttemntManageNo=&kSttemntSn=&kCrtfcAt=&kSttemntAt=&kSttemntNo=&kExclnccrtfcAtchmnflId=&searchDtl=&search=search&sActRelmcode=all&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12=&nas.cmm.token.html.TOKEN=9a0657b3cee2bf11c21a13eea61c247d&sKeyword=&sActCtprvnCode1=&sActSignguCode1=&sActCtprvnCode2=&sActSignguCode2=&sActCtprvnCode3=&sActSignguCode3=&sInsttTyCode=&sInsttTyCode2=&sTrget=&sAge=&stayng=&pc=&acteraDe=on&sActeraBeginDe=&sActeraEndDe=&sCurSearchFlag=Y&sChkSearchFlag=Y&curMenuSn=334'
전체전체2 = 'https://www.youth.go.kr/youth/act/actSearch/allActSearchLst.yt?sCrtfcText=&sSttemntText=&sort=&order=&page=2&rows=&kCrtfcSn=&kFcltySn=&kSnOne=&kProgrmseCode=&kSnTwo=&kSttemntManageNo=&kSttemntSn=&kCrtfcAt=&kSttemntAt=&kSttemntNo=&kExclnccrtfcAtchmnflId=&searchDtl=&search=search&sActRelmcode=all&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12=&nas.cmm.token.html.TOKEN=9a0657b3cee2bf11c21a13eea61c247d&sKeyword=&sActCtprvnCode1=&sActSignguCode1=&sActCtprvnCode2=&sActSignguCode2=&sActCtprvnCode3=&sActSignguCode3=&sInsttTyCode=&sInsttTyCode2=&sTrget=&sAge=&stayng=&pc=&acteraDe=on&sActeraBeginDe=&sActeraEndDe=&sCurSearchFlag=Y&sChkSearchFlag=Y&curMenuSn=334'
# 건스포츠 = 'https://www.youth.go.kr/youth/act/actSearch/allActSearchLst.yt?sCrtfcText=&sSttemntText=&sort=&order=&page=1&rows=&kCrtfcSn=&kFcltySn=&kSnOne=&kProgrmseCode=&kSnTwo=&kSttemntManageNo=&kSttemntSn=&kCrtfcAt=&kSttemntAt=&kSttemntNo=&kExclnccrtfcAtchmnflId=&searchDtl=&search=search&sActRelmcode=&sActRelmcode1=059001&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12=&nas.cmm.token.html.TOKEN=2b0e5f230635803f3fe57813be2e0e0e&sKeyword=&sActCtprvnCode1=&sActSignguCode1=&sActCtprvnCode2=&sActSignguCode2=&sActCtprvnCode3=&sActSignguCode3=&sInsttTyCode=&sInsttTyCode2=&sTrget=&sAge=&stayng=&pc=&acteraDe=on&sActeraBeginDe=&sActeraEndDe=&sCurSearchFlag=Y&sChkSearchFlag=Y&curMenuSn=334'
# 모험개척 = 'https://www.youth.go.kr/youth/act/actSearch/allActSearchLst.yt?sCrtfcText=&sSttemntText=&sort=&order=&page=1&rows=&kCrtfcSn=&kFcltySn=&kSnOne=&kProgrmseCode=&kSnTwo=&kSttemntManageNo=&kSttemntSn=&kCrtfcAt=&kSttemntAt=&kSttemntNo=&kExclnccrtfcAtchmnflId=&searchDtl=&search=search&sActRelmcode=&sActRelmcode1=&sActRelmcode2=059002&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12=&nas.cmm.token.html.TOKEN=2b0e5f230635803f3fe57813be2e0e0e&sKeyword=&sActCtprvnCode1=&sActSignguCode1=&sActCtprvnCode2=&sActSignguCode2=&sActCtprvnCode3=&sActSignguCode3=&sInsttTyCode=&sInsttTyCode2=&sTrget=&sAge=&stayng=&pc=&acteraDe=on&sActeraBeginDe=&sActeraEndDe=&sCurSearchFlag=Y&sChkSearchFlag=Y&curMenuSn=334'
# 역사탐방 = 'https://www.youth.go.kr/youth/act/actSearch/allActSearchLst.yt?sCrtfcText=&sSttemntText=&sort=&order=&page=1&rows=&kCrtfcSn=&kFcltySn=&kSnOne=&kProgrmseCode=&kSnTwo=&kSttemntManageNo=&kSttemntSn=&kCrtfcAt=&kSttemntAt=&kSttemntNo=&kExclnccrtfcAtchmnflId=&searchDtl=&search=search&sActRelmcode=&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=059003&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12=&nas.cmm.token.html.TOKEN=2b0e5f230635803f3fe57813be2e0e0e&sKeyword=&sActCtprvnCode1=&sActSignguCode1=&sActCtprvnCode2=&sActSignguCode2=&sActCtprvnCode3=&sActSignguCode3=&sInsttTyCode=&sInsttTyCode2=&sTrget=&sAge=&stayng=&pc=&acteraDe=on&sActeraBeginDe=&sActeraEndDe=&sCurSearchFlag=Y&sChkSearchFlag=Y&curMenuSn=334'
# 봉사협력 = 'https://www.youth.go.kr/youth/act/actSearch/allActSearchLst.yt?sCrtfcText=&sSttemntText=&sort=&order=&page=1&rows=&kCrtfcSn=&kFcltySn=&kSnOne=&kProgrmseCode=&kSnTwo=&kSttemntManageNo=&kSttemntSn=&kCrtfcAt=&kSttemntAt=&kSttemntNo=&kExclnccrtfcAtchmnflId=&searchDtl=&search=search&sActRelmcode=&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=059005&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12=&nas.cmm.token.html.TOKEN=2b0e5f230635803f3fe57813be2e0e0e&sKeyword=&sActCtprvnCode1=&sActSignguCode1=&sActCtprvnCode2=&sActSignguCode2=&sActCtprvnCode3=&sActSignguCode3=&sInsttTyCode=&sInsttTyCode2=&sTrget=&sAge=&stayng=&pc=&acteraDe=on&sActeraBeginDe=&sActeraEndDe=&sCurSearchFlag=Y&sChkSearchFlag=Y&curMenuSn=334'
# 교류교류 = 'https://www.youth.go.kr/youth/act/actSearch/allActSearchLst.yt?sCrtfcText=&sSttemntText=&sort=&order=&page=1&rows=&kCrtfcSn=&kFcltySn=&kSnOne=&kProgrmseCode=&kSnTwo=&kSttemntManageNo=&kSttemntSn=&kCrtfcAt=&kSttemntAt=&kSttemntNo=&kExclnccrtfcAtchmnflId=&searchDtl=&search=search&sActRelmcode=&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=059006&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12=&nas.cmm.token.html.TOKEN=2b0e5f230635803f3fe57813be2e0e0e&sKeyword=&sActCtprvnCode1=&sActSignguCode1=&sActCtprvnCode2=&sActSignguCode2=&sActCtprvnCode3=&sActSignguCode3=&sInsttTyCode=&sInsttTyCode2=&sTrget=&sAge=&stayng=&pc=&acteraDe=on&sActeraBeginDe=&sActeraEndDe=&sCurSearchFlag=Y&sChkSearchFlag=Y&curMenuSn=334'
# 과학정보 = 'https://www.youth.go.kr/youth/act/actSearch/allActSearchLst.yt?sCrtfcText=&sSttemntText=&sort=&order=&page=1&rows=&kCrtfcSn=&kFcltySn=&kSnOne=&kProgrmseCode=&kSnTwo=&kSttemntManageNo=&kSttemntSn=&kCrtfcAt=&kSttemntAt=&kSttemntNo=&kExclnccrtfcAtchmnflId=&searchDtl=&search=search&sActRelmcode=&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=059007&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12=&nas.cmm.token.html.TOKEN=2b0e5f230635803f3fe57813be2e0e0e&sKeyword=&sActCtprvnCode1=&sActSignguCode1=&sActCtprvnCode2=&sActSignguCode2=&sActCtprvnCode3=&sActSignguCode3=&sInsttTyCode=&sInsttTyCode2=&sTrget=&sAge=&stayng=&pc=&acteraDe=on&sActeraBeginDe=&sActeraEndDe=&sCurSearchFlag=Y&sChkSearchFlag=Y&curMenuSn=334'
# 진로탐구 = 'https://www.youth.go.kr/youth/act/actSearch/allActSearchLst.yt?sCrtfcText=&sSttemntText=&sort=&order=&page=1&rows=&kCrtfcSn=&kFcltySn=&kSnOne=&kProgrmseCode=&kSnTwo=&kSttemntManageNo=&kSttemntSn=&kCrtfcAt=&kSttemntAt=&kSttemntNo=&kExclnccrtfcAtchmnflId=&searchDtl=&search=search&sActRelmcode=&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=059008&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12=&nas.cmm.token.html.TOKEN=2b0e5f230635803f3fe57813be2e0e0e&sKeyword=&sActCtprvnCode1=&sActSignguCode1=&sActCtprvnCode2=&sActSignguCode2=&sActCtprvnCode3=&sActSignguCode3=&sInsttTyCode=&sInsttTyCode2=&sTrget=&sAge=&stayng=&pc=&acteraDe=on&sActeraBeginDe=&sActeraEndDe=&sCurSearchFlag=Y&sChkSearchFlag=Y&curMenuSn=334'
# 자기개발 = 'https://www.youth.go.kr/youth/act/actSearch/allActSearchLst.yt?sCrtfcText=&sSttemntText=&sort=&order=&page=1&rows=&kCrtfcSn=&kFcltySn=&kSnOne=&kProgrmseCode=&kSnTwo=&kSttemntManageNo=&kSttemntSn=&kCrtfcAt=&kSttemntAt=&kSttemntNo=&kExclnccrtfcAtchmnflId=&searchDtl=&search=search&sActRelmcode=&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=059009&sActRelmcode10=&sActRelmcode11=&sActRelmcode12=&nas.cmm.token.html.TOKEN=2b0e5f230635803f3fe57813be2e0e0e&sKeyword=&sActCtprvnCode1=&sActSignguCode1=&sActCtprvnCode2=&sActSignguCode2=&sActCtprvnCode3=&sActSignguCode3=&sInsttTyCode=&sInsttTyCode2=&sTrget=&sAge=&stayng=&pc=&acteraDe=on&sActeraBeginDe=&sActeraEndDe=&sCurSearchFlag=Y&sChkSearchFlag=Y&curMenuSn=334'
# 문화예술 = 'https://www.youth.go.kr/youth/act/actSearch/allActSearchLst.yt?sCrtfcText=&sSttemntText=&sort=&order=&page=1&rows=&kCrtfcSn=&kFcltySn=&kSnOne=&kProgrmseCode=&kSnTwo=&kSttemntManageNo=&kSttemntSn=&kCrtfcAt=&kSttemntAt=&kSttemntNo=&kExclnccrtfcAtchmnflId=&searchDtl=&search=search&sActRelmcode=&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=059010&sActRelmcode11=&sActRelmcode12=&nas.cmm.token.html.TOKEN=2b0e5f230635803f3fe57813be2e0e0e&sKeyword=&sActCtprvnCode1=&sActSignguCode1=&sActCtprvnCode2=&sActSignguCode2=&sActCtprvnCode3=&sActSignguCode3=&sInsttTyCode=&sInsttTyCode2=&sTrget=&sAge=&stayng=&pc=&acteraDe=on&sActeraBeginDe=&sActeraEndDe=&sCurSearchFlag=Y&sChkSearchFlag=Y&curMenuSn=334'
# 환경보존 = 'https://www.youth.go.kr/youth/act/actSearch/allActSearchLst.yt?sCrtfcText=&sSttemntText=&sort=&order=&page=1&rows=&kCrtfcSn=&kFcltySn=&kSnOne=&kProgrmseCode=&kSnTwo=&kSttemntManageNo=&kSttemntSn=&kCrtfcAt=&kSttemntAt=&kSttemntNo=&kExclnccrtfcAtchmnflId=&searchDtl=&search=search&sActRelmcode=&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=059004&sActRelmcode12=&nas.cmm.token.html.TOKEN=2b0e5f230635803f3fe57813be2e0e0e&sKeyword=&sActCtprvnCode1=&sActSignguCode1=&sActCtprvnCode2=&sActSignguCode2=&sActCtprvnCode3=&sActSignguCode3=&sInsttTyCode=&sInsttTyCode2=&sTrget=&sAge=&stayng=&pc=&acteraDe=on&sActeraBeginDe=&sActeraEndDe=&sCurSearchFlag=Y&sChkSearchFlag=Y&curMenuSn=334'
# 기타기타 = 'https://www.youth.go.kr/youth/act/actSearch/allActSearchLst.yt?sCrtfcText=&sSttemntText=&sort=&order=&page=1&rows=&kCrtfcSn=&kFcltySn=&kSnOne=&kProgrmseCode=&kSnTwo=&kSttemntManageNo=&kSttemntSn=&kCrtfcAt=&kSttemntAt=&kSttemntNo=&kExclnccrtfcAtchmnflId=&searchDtl=&search=search&sActRelmcode=&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12=059011&nas.cmm.token.html.TOKEN=2b0e5f230635803f3fe57813be2e0e0e&sKeyword=&sActCtprvnCode1=&sActSignguCode1=&sActCtprvnCode2=&sActSignguCode2=&sActCtprvnCode3=&sActSignguCode3=&sInsttTyCode=&sInsttTyCode2=&sTrget=&sAge=&stayng=&pc=&acteraDe=on&sActeraBeginDe=&sActeraEndDe=&sCurSearchFlag=Y&sChkSearchFlag=Y&curMenuSn=334'

firstUrl = 'https://www.youth.go.kr/youth/act/actSearch/allActSearchLst.yt?sCrtfcText=&sSttemntText=&sort=&order=&page='  # 고은이가 크롤링 한 사이트 : https://www.wevity.com/?c=find&s=1&gub=2&cidx=30
lastUrl = '&rows=&kCrtfcSn=&kFcltySn=&kSnOne=&kProgrmseCode=&kSnTwo=&kSttemntManageNo=&kSttemntSn=&kCrtfcAt=&kSttemntAt=&kSttemntNo=&kExclnccrtfcAtchmnflId=&searchDtl=&search=search&sActRelmcode=all&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12=&nas.cmm.token.html.TOKEN=9a0657b3cee2bf11c21a13eea61c247d&sKeyword=&sActCtprvnCode1=&sActSignguCode1=&sActCtprvnCode2=&sActSignguCode2=&sActCtprvnCode3=&sActSignguCode3=&sInsttTyCode=&sInsttTyCode2=&sTrget=&sAge=&stayng=&pc=&acteraDe=on&sActeraBeginDe=&sActeraEndDe=&sCurSearchFlag=Y&sChkSearchFlag=Y&curMenuSn=334'
print("몇개의 페이지를 크롤링할건가요?")
pageNum = int(input())

# if(fieldNum == '전체') : middleUrl = '&sActRelmcode=all&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12='
# elif(fieldNum == '건강스포츠') : middleUrl = '&sActRelmcode=&sActRelmcode1=059001&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12='
# elif(fieldNum == '모험개척') : middleUrl = '&sActRelmcode=&sActRelmcode1=&sActRelmcode2=059002&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12='
# elif(fieldNum == '역사탐방') : middleUrl = '&sActRelmcode=&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=059003&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12='
# elif(fieldNum == '봉사협력') : middleUrl = '&sActRelmcode=&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=059005&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12='
# elif(fieldNum == '교류') : middleUrl = '&sActRelmcode=&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=059006&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12='
# elif(fieldNum == '과학정보') : middleUrl = '&sActRelmcode=&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=059007&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12='
# elif(fieldNum == '진로탐구') : middleUrl = '&sActRelmcode=&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=059008&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12='
# elif(fieldNum == '자기개발') : middleUrl = '&sActRelmcode=&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=059009&sActRelmcode10=&sActRelmcode11=&sActRelmcode12='
# elif(fieldNum == '문화예술') : middleUrl = '&sActRelmcode=&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=059010&sActRelmcode11=&sActRelmcode12='
# elif(fieldNum == '환경보존') : middleUrl = '&sActRelmcode=&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=059004&sActRelmcode12='
# elif(fieldNum == '기타') : middleUrl = '&sActRelmcode=&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12=059011'

activeNum = 0
act_name = [] # 활동명
act_part = [] # 분야
act_img = [] #  이미지
act_age = [] # 대상나이
act_due = [] #  모집 기간
act_orgName = [] #  기관명
act_ration = [] # 지역
act_price = [] #  참가비
total = [] #  전체 활동들의 정보가 dic형태로 담긴 list
dicTotal = {} # 각 활동들의 정보를 임시로 저장할 dic

for page in range (pageNum):

  url = firstUrl + str((page+1)) + lastUrl

  print(page + 1, '페이지')

  options = webdriver.ChromeOptions()
  options.add_experimental_option("excludeSwitches", ["enable-logging"])
  # driver = webdriver.Chrome('C:/VSCode/JA_Korea/크롤링 연습/chromedriver.exe') #C:/VSCode/JA_Korea/크롤링 연습/chromedriver.exe
  # driver = webdriver.Chrome(options=options)
  driver = webdriver.Chrome('D:/samsung-sds/src/chromedriver.exe')
  driver.get(url)

  html = driver.page_source
  soup = BeautifulSoup(html,"html.parser")

  nameResult = soup.select('.act-name-box.st2 > dl > dt > a') # - 활동 이름, 활동 분야
  partResult = soup.select('.act-name-box.st2 > dl > dt > .label-area:nth-child(2)') # - 활동 이름, 활동 분야
  imgResult = soup.select('.act-thum-box > .act-thum-img > a > img') # - 대표 사진
  ddResult = soup.select('.act-name-box.st2 > dl > dd') # - 기관명, 활동일, 활동지역, 모집기간, 인원, 참가비, 연령, 등록일   필요한 것 : 지역, 활동일시, 기관명, 참가비, 인원 및 연령

  print('활동 이름------------------------------------------')
  for name in nameResult: # 활동명
    act_name.append(name.contents[0])
    print(name.contents[0])
  
  print('분야------------------------------------------')
  for part in partResult: # 분야
    act_part.append(part.contents[1].strip())
    print(part.contents[1].strip())

  print('이미지------------------------------------------')
  for img in imgResult: # 이미지
    if img['alt'] != '인증마크' and img['alt'] != '신고완료':
      act_img.append('https://www.youth.go.kr/' + img['src'])
      print('https://www.youth.go.kr/' + img['src'])
    

  for i in ddResult: #  연령층(세부정보), 기간, 주최기관, 지역
    title = i.contents[0].contents[0]
    content = i.contents[1][3:].strip()
    if(title == '기관명'):
      activeNum+=1
      print('-----------------------------------------------------------')
    if(title == '연 령'):
      num = len(i.contents)
      editedContent = []
      for j in range (num-2):
        if((j+2)%2 == 0):
          editedContent.append(i.contents[j+2].contents[0])
      print(editedContent)
    else: # title = 연령
      print(title + '=' + content)
    if title == '기관명':
      act_orgName.append(content)
    elif title == '지역':
      act_ration.append(content)
    elif title == '모집기간':
      act_due.append(content)
    elif title == '참가비':
      act_price.append(content)
    elif title == '연 령':
      act_age.append(editedContent)
       

  driver.close()
  print("===================================================================================")

print('검색 활동 갯수 : ', activeNum)
print('')

print(act_name) #  활동이름, null, 분야, 이미지, 지역, 주최기관, null, 참가비, null, 연령층(세부정보), 기간
print(act_part)
print(act_img)
print(act_ration)
print(act_orgName)
print(act_price)
print(act_age)
print(act_due)
print('')
print('')
print('============================================================= < total_list > =============================================================')
print('')

for plus in range (pageNum*10): #  활동이름, null, 분야, 이미지, 지역, 주최기관, null, 참가비, null, 연령층(세부정보), 기간
  dicTotal['title'] = act_name[plus]
  dicTotal['link'] = ''
  dicTotal['part'] = '기타'
  dicTotal['img'] = act_img[plus]
  dicTotal['local'] = act_ration[plus]
  dicTotal['host'] = act_orgName[plus]
  dicTotal['reward'] = ''
  dicTotal['price'] = act_price[plus]
  dicTotal['hompage'] = ''
  dicTotal['info'] = act_age[plus]
  dicTotal['dday'] = act_due[plus]
  dicTotal_copy = dicTotal.copy()
  total.append(dicTotal_copy)

  print(total)
  
print('')
print('')
print('============================================================= < total_list > =============================================================')
print('')
for last in range (pageNum*10):
  print(total[last])
  print('')

data.insert_many(total)