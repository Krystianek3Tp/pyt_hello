import sys

from PyQt6.QtWidgets import QWidget, QApplication

from layout import Ui_Dialog


class Myform(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.okButton.clicked.connect(self.on_button_clicked)
        self.show()

    def on_button_clicked(self):
        name = self.ui.nameEdit.text()
        self.ui.nameLabel.setText(f'Cześć {name}')



if __name__ == '__main__' :
    app = QApplication(sys.argv)
    window = Myform()
    sys.exit(app.exec())