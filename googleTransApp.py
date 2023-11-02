import sys

from PyQt5 import uic  # Qt Designer에서 제작한 ui를 불러와주는 클래스
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import googletrans

from_calss = uic.loadUiType("ui/googleUi.ui")[0]

class MyGoogleTrans(QMainWindow, from_calss):
    def __init__(self): # 초기화자(생성자)
        super().__init__() # 부모 클래스의 초기화자 호출
        self.setupUi(self) # 제작해 놓은 googleUi.ui를 연결
        self.setWindowTitle("구글 번역기")  # 번역기 앱의 타이틀
        # self.setWindowIcon(QIcon("icon/google.png")) # 번역기 앱의 아이콘
        self.statusBar().showMessage("Google Trans App v1.0 copyright ⓒ GyojinCompany") # 상태 표시줄

        self.trans_btn.clicked.connect(self.trans_function) # signal
        self.reset_btn.clicked.connect(self.reset_function)


    def trans_function(self): #slot
        trans_kor = self.input_kor_text.text() # input_kor_text 에 입력된 한글을 가져옴

        trans = googletrans.Translator() # 구글트랜스 모듈의 객체(번역해 주는 객체)
        #print(googletrans.LANGUAGES) # 번역 언어 ticker 불러오기

        trans_eng = trans.translate(trans_kor, dest="en") # 영어번역결과
        trans_jap = trans.translate(trans_kor, dest="ja")  # 일본어번역결과
        trans_chn = trans.translate(trans_kor, dest="zh-cn")  # 중국어번역결과

        self.output_eng_text.append(trans_eng.text)
        self.output_jan_text.append(trans_jap.text)
        self.output_ch_text.append(trans_chn.text)
        # .settext, .append

    def reset_function(self):
        self.input_kor_text.clear()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = MyGoogleTrans()
    myApp.show()
    sys.exit(app.exec())
