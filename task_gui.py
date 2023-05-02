import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, \
    QHBoxLayout, QVBoxLayout, QStackedLayout, QWidget, QMessageBox
import prime_tester


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Prime Tester")

        pagelayout = QVBoxLayout()
        widget_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(widget_layout)
        pagelayout.addLayout(self.stacklayout)

        self.textwidget = QLineEdit()
        self.textwidget.setPlaceholderText("Enter a nubmer")
        widget_layout.addWidget(self.textwidget)

        button = QPushButton("Check!")
        button.clicked.connect(self.the_button_was_clicked)
        widget_layout.addWidget(button)
        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def the_button_was_clicked(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Answer")
        result = 'Увы...'
        ans = int(self.line_value())
        if prime_tester.is_prime(ans)[0]:
            result = 'Простое!'
        dlg.setText(result)
        button = dlg.exec()

    def line_value(self):
        return self.textwidget.text()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
