import cv2 as cv
import numpy as np
from PyQt5.QtWidgets import *
import sys

class SpecialEffect(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('사진 특수 효과')
        self.setGeometry(200, 200, 900, 200)

        pictureButton = QPushButton('사진 읽기', self)
        embossButton = QPushButton('엠보싱', self)
        cartoonButton = QPushButton('카툰', self)
        sketchButton = QPushButton('연필 스케치', self)
        oilButton = QPushButton('유화', self)
        blurButton = QPushButton('블러 효과', self)  # 블러 버튼 추가
        backlightButton = QPushButton('역광 효과', self)  # 역광 버튼 추가
        saveButton = QPushButton('저장하기', self)
        quitButton = QPushButton('나가기', self)
        
        # UI 배치 설정
        pictureButton.setGeometry(10, 10, 100, 30)
        embossButton.setGeometry(110, 10, 100, 30)
        cartoonButton.setGeometry(210, 10, 100, 30)
        sketchButton.setGeometry(310, 10, 100, 30)
        oilButton.setGeometry(410, 10, 100, 30)
        blurButton.setGeometry(510, 10, 100, 30)  # 블러 버튼 위치 설정
        backlightButton.setGeometry(610, 10, 100, 30)  # 역광 버튼 위치 설정
        saveButton.setGeometry(710, 10, 100, 30)
        quitButton.setGeometry(810, 10, 100, 30)
        
        # 버튼 연결
        pictureButton.clicked.connect(self.pictureOpenFunction)
        embossButton.clicked.connect(self.embossFunction)
        cartoonButton.clicked.connect(self.cartoonFunction)
        sketchButton.clicked.connect(self.sketchFunction)
        oilButton.clicked.connect(self.oilFunction)
        blurButton.clicked.connect(self.blurFunction)  # 블러 함수 연결
        backlightButton.clicked.connect(self.backlightFunction)  # 역광 함수 연결
        saveButton.clicked.connect(self.saveFunction)
        quitButton.clicked.connect(self.quitFunction)
        
    def pictureOpenFunction(self):
        fname = QFileDialog.getOpenFileName(self, '사진 읽기', './')
        self.img = cv.imread(fname[0])
        if self.img is None: sys.exit('파일을 찾을 수 없습니다.')
        cv.imshow('Painting', self.img)
        
    # 엠보싱 기능
    def embossFunction(self):
        femboss = np.array([[-1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
        gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        gray16 = np.int16(gray)
        self.emboss = np.uint8(np.clip(cv.filter2D(gray16, -1, femboss) + 128, 0, 255))
        cv.imshow('Emboss', self.emboss)
    
    # 카툰 효과
    def cartoonFunction(self):
        self.cartoon = cv.stylization(self.img, sigma_s=60, sigma_r=0.45)
        cv.imshow('Cartoon', self.cartoon)
    
    # 연필 스케치
    def sketchFunction(self):
        self.sketch_gray, self.sketch_color = cv.pencilSketch(self.img, sigma_s=60, sigma_r=0.07, shade_factor=0.02)
        cv.imshow('Pencil Sketch (Gray)', self.sketch_gray)
        cv.imshow('Pencil Sketch (Color)', self.sketch_color)
    
    # 유화 효과
    def oilFunction(self):
        self.oil = cv.xphoto.oilPainting(self.img, 10, 1, cv.COLOR_BGR2Lab)
        cv.imshow('Oil Painting', self.oil)
    
    # 블러 효과
    def blurFunction(self):
        self.blur = cv.GaussianBlur(self.img, (15, 15), 0)  # 가우시안 블러 적용
        cv.imshow('Blur', self.blur)
    
    # 역광 효과
    def backlightFunction(self):
        hsv = cv.cvtColor(self.img, cv.COLOR_BGR2HSV)
        hsv[:, :, 2] = cv.add(hsv[:, :, 2], 50)  # 밝기 증가
        self.backlight = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
        cv.imshow('Backlight Effect', self.backlight)
    
    # 이미지 저장
    def saveFunction(self):
        fname = QFileDialog.getSaveFileName(self, '파일 저장', './')
        i = self.pickCombo.currentIndex()
        if i == 0: cv.imwrite(fname[0], self.emboss)
        elif i == 1: cv.imwrite(fname[0], self.cartoon)
        elif i == 2: cv.imwrite(fname[0], self.sketch_gray)
        elif i == 3: cv.imwrite(fname[0], self.sketch_color)
        elif i == 4: cv.imwrite(fname[0], self.oil)
        elif i == 5: cv.imwrite(fname[0], self.blur)  # 블러 저장
        elif i == 6: cv.imwrite(fname[0], self.backlight)  # 역광 저장
    
    # 종료
    def quitFunction(self):
        cv.destroyAllWindows()
        self.close()

app = QApplication(sys.argv)
win = SpecialEffect()
win.show()
app.exec_()
