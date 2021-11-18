from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import os
import sys

from ui import main




class Main(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.create_UI()


    def create_UI(self):
        if sys.platform == "linux":
            path = r"/home/user"
        elif sys.platfor == "win32":
            path = r"C:\Users"
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath((QtCore.QDir.rootPath()))
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(path))
        self.treeView.setSortingEnabled(True)

        self.create_context_menu()



    def create_context_menu(self):
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.context_menu)



    def context_menu(self):
        
        menu = QtWidgets.QMenu()

        open_file = menu.addAction("Open file with VScode")
        open_file.triggered.connect(lambda: self.open_file())

        menu.exec_(QtGui.QCursor.pos())


    def open_file(self):
            index = self.treeView.currentIndex()
            file_path = self.model.filePath(index)
            os.system(f"code {file_path}")

        

    


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    fb = Main()
    fb.show()
    sys.exit(app.exec_())
 