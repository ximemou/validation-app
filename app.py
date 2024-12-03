import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QLoggingCategory
from controllers.main_window import MainWindowForm
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    QLoggingCategory.setFilterRules('*=false\n')
    app = QApplication()
    window = MainWindowForm()
    window.show()

    sys.exit(app.exec())