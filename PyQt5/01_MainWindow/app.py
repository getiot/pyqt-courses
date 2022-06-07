from PyQt5.QtWidgets import QWidget, QApplication

app = QApplication([])

mainWindow = QWidget()

mainWindow.setGeometry(0, 0, 400, 300)
mainWindow.setWindowTitle('Hello World')

mainWindow.show()

app.exec()