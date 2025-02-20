import sys
import math
import pytest
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

            gcd_result = self.get_gcd(num1, num2)
            self.result_label.setText(f"Результат: НСД({num1}, {num2}) = {gcd_result}")
        except ValueError:
            QMessageBox.warning(self, "Помилка", "Введіть коректні цілі числа!")

    @staticmethod
    def get_gcd(a: int, b: int) -> int:
        """Обчислює НСД двох чисел"""
        return math.gcd(a, b)


# Функція для запуску додатку
def run_app():
    app = QApplication(sys.argv)
    window = GCDApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run_app()


# Тести для pytest
def test_gcd():
    assert GCDApp.get_gcd(48, 18) == 6
    assert GCDApp.get_gcd(101, 103) == 1
    assert GCDApp.get_gcd(56, 98) == 14
    assert GCDApp.get_gcd(270, 192) == 6
    assert GCDApp.get_gcd(25, 5) == 5
