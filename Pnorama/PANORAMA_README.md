# 파노라마 애플리케이션 (Panorama Application)

이 프로젝트는 PyQt5와 OpenCV를 활용하여 웹캠으로 영상을 수집하고, 이를 통해 파노라마 이미지를 생성하는 애플리케이션입니다. 사용자는 여러 개의 이미지를 하나의 파노라마로 봉합하고, 확대/축소 및 이동 기능을 통해 자세히 확인할 수 있습니다.

## 주요 기능
- **영상 수집**: 웹캠을 통해 다수의 이미지를 수집합니다.
- **파노라마 생성**: 수집된 이미지를 하나의 파노라마로 봉합합니다.
- **확대/축소 및 이동**: 생성된 파노라마 이미지를 확대/축소하고 상하좌우로 이동하여 세부 사항을 확인합니다.
- **파일 저장**: 생성된 파노라마 이미지를 파일로 저장합니다.
- **오류 메시지**: 파노라마 생성 실패 시 오류 코드와 함께 상세 메시지를 제공합니다.

## 설치

이 애플리케이션을 실행하기 위해 다음 의존성을 설치해야 합니다.

```bash
pip install numpy==1.24.3 opencv-python==4.7.0.68 PyQt5==5.15.9
```

## 사용법
 1. 애플리케이션을 실행합니다.
 2. 영상 수집 버튼을 눌러 웹캠에서 여러 장의 이미지를 수집합니다. c 키로 이미지를 추가하고, q 키로 수집을 종료합니다.
 3. 봉합 버튼을 눌러 수집된 이미지를 나열해 확인합니다.
 4. 저장 버튼을 눌러 파노라마 이미지를 생성합니다.
 5. 생성된 파노라마는 +, -, w, s, a, d 키를 이용해 확대/축소 및 이동할 수 있습니다.
 6. 나가기 버튼을 눌러 프로그램을 종료합니다.

## 확대/축소 및 이동 제어
 - '+': 확대
 - '-': 축소
 - 'w': 위로 이동
 - 's': 아래로 이동
 - 'a': 왼쪽으로 이동
 - 'd': 오른쪽으로 이동

## 개발자 정보
 - 개발자 : RYU-YEONJOON (niallgull02@syuin.ac.kr)

---

# Panorama Application

This project is a panorama creation application that uses PyQt5 and OpenCV to collect images from a webcam and merge them into a single panorama. Users can collect multiple images, stitch them together, and inspect the panorama using zoom and pan functions.

## Key Features
 -**Image Collection**: Collect multiple images from a webcam.
 -**Panorama Stitching**: Stitch collected images into a single panorama.
 -**Zoom and Pan**: Zoom in/out and pan the panorama image to inspect details.
 -**Save to File**: Save the generated panorama image as a file.
 -**Error Messages**: Detailed messages are displayed with error codes in case of panorama creation failure.

## Installation

 Install the dependencies required to run this application:

```bash
 pip install numpy==1.24.3 opencv-python==4.7.0.68 PyQt5==5.15.9
 ```

## Usage
 1. Launch the application.
 2. Click the Collect Images button to collect multiple images from the webcam. Press c to capture an image and q to finish collecting.
 3. Click the Show button to display the collected images in a small preview.
 4. Click the Stitch button to create a panorama from the collected images.
 5. Use the +, -, w, s, a, and d keys to zoom and pan around the panorama.
 6. Click the Quit button to exit the application.

## Zoom and Pan Controls
 - '+': Zoom in
 - '-': Zoom out
 - 'w': Pan up
 - 's': Pan down
 - 'a': Pan left
 - 'd': Pan right

## Developer Information
 - Developer: RYU-YEONJOON (niallgull02@syuin.ac.kr)