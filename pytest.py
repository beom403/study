import sys
from PyQt5.QtWidgets import QApplication, QWidget

def makeWindow(nameOfWindow):
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 250)
    w.move(300, 300)
    w.setWindowTitle(nameOfWindow)
    w.show()
    sys.exit(app.exec_())

    return None


if __name__ == '__main__':
    makeWindow('1')
    # makeWindow('asdf')