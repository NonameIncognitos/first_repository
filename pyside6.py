import sys
from PySide6 import QtCore, QtWidgets, QtGui

class WinNew(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_Side_GUI()

    def init_Side_GUI(self):
        self.setWindowTitle('Второе окошко')
        self.layout = QtWidgets.QVBoxLayout(self)
        self.label = QtWidgets.QLabel('Это второе окно, Добро пожаловать!', alignment=QtCore.Qt.AlignTop)
        
        self.layout.addWidget(self.label)
        self.resize(400, 300)
    
class Main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_Side_GUI()
        
    def init_Side_GUI(self):
        self.setWindowTitle('First GUI')
        self.layout = QtWidgets.QVBoxLayout(self)

        self.initTextLabel()
        self.initButtonsOnGUI()
        self.initSecondOpenNewWindowButton()

        self.counter = 0

        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        self.text.setFont(font)  # Установка шрифта для self.text

    def initTextLabel(self):
        self.text = QtWidgets.QLabel("hello", alignment=QtCore.Qt.AlignCenter)
        self.CHECKe = QtWidgets.QLabel(alignment=QtCore.Qt.AlignHCenter)

        self.layout.addWidget(self.text)
        self.layout.addWidget(self.CHECKe)

    def initButtonsOnGUI(self):
        

        button_data = [
            ('Click Me', self.magic),
            ('Обнулить\nнажаите?', self.resetCounter),
            ('Умножить', self.multiCounter)
        ]
        
        button_layout = QtWidgets.QVBoxLayout()

        

        for text, slot in button_data:
            button = QtWidgets.QPushButton(text)
            button.setFixedSize(100, 50)
            button.clicked.connect(slot)
            button_layout.addWidget(button)

        self.layout.addLayout(button_layout)
        
        # Стилизация кнопок
        for i in range(button_layout.count()):
            button = button_layout.itemAt(i).widget()
            button.setFixedSize(100, 50)

            


    def initSecondOpenNewWindowButton(self):
        self.buttonOpenWindow = QtWidgets.QPushButton('Open New Window')
        self.layout.addWidget(self.buttonOpenWindow)

        self.second_window = None
        self.buttonOpenWindow.clicked.connect(self.open_second_window)

    @QtCore.Slot()
    def open_second_window(self):
        if not self.second_window or self.second_window.isHidden():
            self.second_window = WinNew()
            self.second_window.show()
            
    @QtCore.Slot()
    def magic(self):
        self.counter += 1
        self.CHECKe.setTextFormat(QtCore.Qt.RichText)
        self.CHECKe.setText(f"<b>{str(self.counter)}</b>")

        button = self.layout.itemAt(1).widget()
        button.setFixedSize(100, 50)

    @QtCore.Slot()
    def multiCounter(self):
        self.CHECKe.setTextFormat(QtCore.Qt.RichText)
        self.CHECKe.setText(f"Multi = {self.counter * 2}")
        button = self.layout.itemAt(2).widget()
        button.setFixedSize(100, 50)

    @QtCore.Slot()
    def resetCounter(self):
        self.counter = 0
        self.CHECKe.setText(str(self.counter))
        button = self.layout.itemAt(3).widget()
        button.setFixedSize(100, 50)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Main()
    widget.resize(600, 600)
    widget.show()

    sys.exit(app.exec())
