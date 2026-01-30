from PySide6.QtWidgets import QMainWindow, QApplication, QDialog
import sys
from pathlib import Path
from ui.ui_mainWindow import Ui_MainWindow
from ui.ui_newProject import Ui_Dialog as newProj
from core.project_manager import ProjectManager

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1200, 720)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        if getattr(sys, 'frozen', False):
            # Binary mode
            self.mainDirectory = Path(sys._MEIPASS)
        else:
            # Dev mode
            self.mainDirectory = Path(__file__).resolve().parent.parent

        self.projectManager = ProjectManager(self.ui, self.mainDirectory)

        self.ui.newProjectBtn.clicked.connect(self.openNewProjectDialog)
    
    def openNewProjectDialog(self):
        dialog = QDialog(self)
        dialogUI = newProj()
        dialogUI.setupUi(dialog)

        # Pulls versions & adds them to UI
        versionList = self.projectManager.getVersions()
        for version in versionList["versions"]:
            dialogUI.packVersion.addItem(version)
        
        dialogUI.createProjectBtn.clicked.connect(lambda: self.newProject(dialog, dialogUI))

        dialog.exec()
    
    def newProject(self, dialog, dialogUI):
        packDetails = {
            "name": dialogUI.packTitle.text(),
            "namespace": dialogUI.packNamespace.text(),
            "description": dialogUI.packDescription.text(),
            "version": dialogUI.packVersion.currentText()
        }
        self.projectManager.newProject(packDetails)

        dialog.accept()

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())