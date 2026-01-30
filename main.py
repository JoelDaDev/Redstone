from PySide6.QtWidgets import QMainWindow, QApplication, QDialog
import sys
from ui.ui_mainWindow import Ui_MainWindow
from ui.ui_newProject import Ui_Dialog as newProj

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1200, 720)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.newProjectBtn.clicked.connect(self.openNewProjectDialog)
    
    def openNewProjectDialog(self):
        dialog = QDialog(self)
        dialogUI = newProj()
        dialogUI.setupUi(dialog)
        dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.setStyle("Breeze")
    sys.exit(app.exec())