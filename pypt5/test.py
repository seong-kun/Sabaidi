import sys
from PyQt5.QtWidgets import QApplication, QWidget,  QLabel, QComboBox, QTextEdit, QVBoxLayout



class ComboBoxExample(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 세로 레이아웃
        layout = QVBoxLayout()

        # 콤보박스 생성
        self.combo = QComboBox(self)
        self.combo.addItem("")  # 콤보박스 선택 전 빈칸이 보이도록 빈 항목을 추가
        self.combo.addItems(['항목 1', '항목 2', '항목 3', '항목 4']) # 선택할 항목
        self.combo.setCurrentIndex(0)  # 첫 번째 항목(빈 항목)을 기본 선택으로 설정하여 처음에 빈화면이 보이도록 함

        # 라벨 생성
        self.label = QLabel("콤보박스에서 하나 선택하세요.")
       
        # 텍스트 에디트 생성
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)  # 읽기 전용으로 설정

        # 레이아웃에 위젯 추가
        layout.addWidget(self.label)
        layout.addWidget(self.combo)
        layout.addWidget(self.text_edit)

        # 콤보박스의 선택 변경 시 호출될 함수 연결
        self.combo.currentTextChanged.connect(self.onComboBoxChanged)

        # 레이아웃 설정
        self.setLayout(layout)

        # 윈도우 설정
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('콤보박스 예제')
        self.show()

    def onComboBoxChanged(self, text):

        # 선택된 항목을 텍스트 에디트에 표시. text에 선택된 항목이 있습니다.
        if text:
            self.text_edit.setText(f"선택된 항목: {text}")
        else:
            self.text_edit.clear()  # 빈 항목 선택 시 텍스트 에디트 비우기

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ComboBoxExample()
    sys.exit(app.exec_())