import os
import sys
from PyQt5 import QtWidgets
from interface import MainWindow
from config import output_pdf_path

def main():
    # Получаем директорию из пути
    output_dir = os.path.dirname(output_pdf_path)

    # Проверяем и создаём папку, если её нет
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Создана папка: {output_dir}")

    # Запуск приложения
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
