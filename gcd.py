import sys
import math
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QMessageBox,
)


class GCDApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Найбільший спільний дільник")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label1 = QLabel("Введіть перше число:", self)
        layout.addWidget(self.label1)

        self.num1_input = QLineEdit(self)
        layout.addWidget(self.num1_input)

        self.label2 = QLabel("Введіть друге число:", self)
        layout.addWidget(self.label2)

        self.num2_input = QLineEdit(self)
        layout.addWidget(self.num2_input)

        self.calculate_button = QPushButton("Обчислити НСД", self)
        self.calculate_button.clicked.connect(self.calculate_gcd)
        layout.addWidget(self.calculate_button)

        self.result_label = QLabel("Результат: ", self)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_gcd(self):
        try:
            num1 = int(self.num1_input.text())
            num2 = int(self.num2_input.text())

            if num1 <= 0 or num2 <= 0:
                QMessageBox.warning(self, "Помилка", "Числа мають бути додатними!")
                return

            gcd_result = math.gcd(num1, num2)
            self.result_label.setText(f"Результат: НСД({num1}, {num2}) = {gcd_result}")
        except ValueError:
            QMessageBox.warning(self, "Помилка", "Введіть коректні цілі числа!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GCDApp()
    window.show()
    sys.exit(app.exec_())
