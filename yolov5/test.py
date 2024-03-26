import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import subprocess

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.processes = []

    def run_yolov5(self, filepath):
        process = subprocess.Popen(["python", filepath])
        self.processes.append(process)

    def close_processes(self):
        for process in self.processes:
            process.terminate()
        self.processes.clear()

    def initUI(self):
        layout = QVBoxLayout()

        button1 = QPushButton('자동차실행', self)
        button1.clicked.connect(lambda: self.run_yolov5("C:/Users/hanbin/Desktop/code_A/yolov5/car_detect.py"))
        layout.addWidget(button1)

        button3 = QPushButton('표지판실행', self)
        button3.clicked.connect(lambda: self.run_yolov5("C:/Users/hanbin/Desktop/code_A/yolov5/SIGN_detect.py"))
        layout.addWidget(button3)

        button4 = QPushButton('신호등실행', self)
        button4.clicked.connect(lambda: self.run_yolov5("C:/Users/hanbin/Desktop/code_A/yolov5/tl_detect.py"))
        layout.addWidget(button4)

        button2 = QPushButton('종합실행', self)
        button2.clicked.connect(lambda: self.run_yolov5("C:/Users/hanbin/Desktop/code_A/yolov5/CTS_detect.py"))
        layout.addWidget(button2)

        close_button = QPushButton('프로그램 종료', self)
        close_button.clicked.connect(self.close_processes)
        layout.addWidget(close_button)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('객체인식프로그램')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())