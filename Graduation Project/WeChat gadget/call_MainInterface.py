import sys
from PyQt5.QtWidgets import QApplication, QWidget
import MainInterface

if __name__ == '__main__':
    app = QApplication(sys.argv)

    Form = QWidget()

    ui = MainInterface.Ui_Interface_Main()

    ui.setupUi(Form)

    Form.show()

sys.exit(app.exec_())