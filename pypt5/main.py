import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QTextEdit, QVBoxLayout


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        self.combo = QComboBox(self)
        self.combo.addItem("")
        self.combo.addItems(['항목1','항목2','항목3','항목4'])
        self.combo.setCurrentIndex(0)
        
        self.label = QLabel("콤보박스에서 하나 선택하세요")
        
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        
        layout.addWidget(self.label)
        layout.addWidget(self.combo)
        layout.addWidget(self.text_edit)
        
        self.combo.currentTextChanged.connect(self.onComboBoxChanged)
        
        self.setLayout(layout)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('콤보박스 예제')
        
    def onComboBoxChanged(self, text):
        if text:
            self.text_edit.setText(f"선택된항목: {text}")
        else:
            self.text_edit.clear()
      


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())
