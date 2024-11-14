from PyQt5.QtWidgets import *
import cv2 as cv
import numpy as np
import winsound
import sys

class Panorama(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('파노라마 영상')
        self.setGeometry(200, 200, 700, 200)

        collectButton = QPushButton('영상 수집', self)
        self.showButton = QPushButton('봉합', self)
        self.stitchButton = QPushButton('저장', self)
        self.saveButtton = QPushButton('나가기', self)
        quitButton = QPushButton('나가기', self)
        self.label = QLabel('환영합니다', self)

        collectButton.setGeometry(10, 25, 100, 30)
        self.showButton.setGeometry(110, 35, 100, 30)
        self.stitchButton.setGeometry(210, 25, 100, 30)
        self.saveButtton.setGeometry(310, 25, 100, 30)
        quitButton.setGeometry(450, 25, 100, 30)
        self.label.setGeometry(10, 70, 600, 170)

        self.showButton.setEnabled(False)
        self.stitchButton.setEnabled(False)
        self.saveButtton.setEnabled(False)

        collectButton.clicked.connect(self.collectFunction)
        self.showButton.clicked.connect(self.showFunction)
        self.stitchButton.clicked.connect(self.stitchFunction)
        self.saveButtton.clicked.connect(self.saveFunction)
        quitButton.clicked.connect(self.quitFunction)

        # Zoom and Pan feature initialization
        self.zoom_level = 1.0
        self.pan_offset = [0, 0]

    def collectFunction(self):
        self.showButton.setEnabled(False)
        self.stitchButton.setEnabled(False)
        self.saveButtton.setEnabled(False)
        self.label.setText('c를 여러 번 눌러 수집하고 끝나며 q를 눌러 비디오를 끕니다.')

        self.cap = cv.VideoCapture(0, cv.CAP_DSHOW)
        if not self.cap.isOpened():
            sys.exit('카메라 연결 실패')

        self.imgs = []
        while True:
            ret, frame = self.cap.read()
            if not ret: break

            cv.imshow('video display', frame)

            key = cv.waitKey(1)
            if key == ord('c'):
                self.imgs.append(frame)
            elif key == ord('q'):
                self.cap.release()
                cv.destroyWindow('video display')
                break

        if len(self.imgs) >= 2:
            self.showButton.setEnabled(True)
            self.stitchButton.setEnabled(True)
            self.saveButtton.setEnabled(True)

    def showFunction(self):
        self.label.setText('수집된 영상은 ' + str(len(self.imgs)) + '장입니다.')
        stack = cv.resize(self.imgs[0], dsize=(0, 0), fx=0.25, fy=0.25)
        for i in range(1, len(self.imgs)):
            stack = np.hstack((stack, cv.resize(self.imgs[i], dsize=(0, 0), fx=0.25, fy=0.25)))
        cv.imshow('Image collection', stack)

    def stitchFunction(self):
        stitcher = cv.Stitcher_create()
        status, self.img_stitched = stitcher.stitch(self.imgs)
        if status == cv.Stitcher_OK:
            self.displayZoomPan(self.img_stitched)
        else:
            winsound.Beep(3000, 500)
            error_message = f'파노라마 제작에 실패했습니다. (오류 코드: {status}) - 다시 시도하세요.'
            self.label.setText(error_message)

    def displayZoomPan(self, img):
        """ Displays image with zoom and pan capabilities. """
        self.current_img = img.copy()
        self.updateZoomPan()

        while True:
            cv.imshow('Image stitched panorama', self.current_display)

            key = cv.waitKey(10)
            if key == ord('+'):
                self.zoom_level = min(3.0, self.zoom_level + 0.1)  # 최대 3배 확대
                self.updateZoomPan()
            elif key == ord('-'):
                self.zoom_level = max(1.0, self.zoom_level - 0.1)  # 최소 원본 크기
                self.updateZoomPan()
            elif key == ord('w'):
                self.pan_offset[1] = max(0, self.pan_offset[1] - 10)  # 위로 이동
                self.updateZoomPan()
            elif key == ord('s'):
                self.pan_offset[1] = min(img.shape[0], self.pan_offset[1] + 10)  # 아래로 이동
                self.updateZoomPan()
            elif key == ord('a'):
                self.pan_offset[0] = max(0, self.pan_offset[0] - 10)  # 왼쪽으로 이동
                self.updateZoomPan()
            elif key == ord('d'):
                self.pan_offset[0] = min(img.shape[1], self.pan_offset[0] + 10)  # 오른쪽으로 이동
                self.updateZoomPan()
            elif key == ord('q'):
                cv.destroyWindow('Image stitched panorama')
                break

    def updateZoomPan(self):
        """ Updates the display image based on current zoom and pan settings. """
        h, w = self.current_img.shape[:2]
        center_x, center_y = w // 2 + self.pan_offset[0], h // 2 + self.pan_offset[1]
        zoomed_img = cv.resize(self.current_img, None, fx=self.zoom_level, fy=self.zoom_level, interpolation=cv.INTER_LINEAR)

        y1 = max(0, center_y - h // 2)
        y2 = min(zoomed_img.shape[0], center_y + h // 2)
        x1 = max(0, center_x - w // 2)
        x2 = min(zoomed_img.shape[1], center_x + w // 2)

        self.current_display = zoomed_img[y1:y2, x1:x2]

    def saveFunction(self):
        fname = QFileDialog.getSaveFileName(self, '파일 저장', './')
        cv.imwrite(fname[0], self.img_stitched)

    def quitFunction(self):
        if hasattr(self, 'cap') and self.cap.isOpened():
            self.cap.release()
        cv.destroyAllWindows()
        self.close()

app = QApplication(sys.argv)
win = Panorama()
win.show()
app.exec_()
