import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
import subprocess

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Program Launcher')
        self.setGeometry(100, 100, 300, 200)

        # 실행 파일 경로와 이름 정의
        self.programs = {
            "자동차": r'C:/Users/hanbin/Desktop/code_A/yolov5/car_detect.py',
            "표지판": r'C:/Users/hanbin/Desktop/code_A/yolov5/SIGN_detect.py',
            "신호등": r'C:/Users/hanbin/Desktop/code_A/yolov5/tl_detect.py',
            "종합": r'C:/Users/hanbin/Desktop/code_A/yolov5/CTS_detect.py'
        }

        layout = QVBoxLayout(self)

        # 실행 버튼 추가
        for name in self.programs:
            button = QPushButton(f'실행 {name}', self)
            button.clicked.connect(lambda _, name=name: self.run_program(name))
            layout.addWidget(button)

        # 종료 버튼 추가
        self.exit_button = QPushButton('종료', self)
        self.exit_button.clicked.connect(self.close)
        layout.addWidget(self.exit_button)

        self.setLayout(layout)
        self.show()

    def run_program(self, name):
        # 실행할 파일 경로 설정
        path = self.programs[name]
        
        # 프로세스 실행
        self.process = subprocess.Popen(['python', path], shell=True)

        # 프로세스가 종료될 때까지 대기
        self.process.wait()

    def closeEvent(self, event):
        # 종료 이벤트 핸들링
        reply = QMessageBox.question(self, 'Message', '프로그램을 종료하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
