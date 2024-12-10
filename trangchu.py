from PySide6.QtCore import Qt
from ui_trangchu import Ui_MainWindow
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton, QWidget


class MyTrangChu(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("trangchu menu")

        self.icon_name_widget.setHidden(True )

        self.Khoa_1.clicked.connect(self.switch_to_KhoaPage)
        self.Khoa_2.clicked.connect(self.switch_to_KhoaPage)

        self.Lop_1.clicked.connect(self.switch_to_LopPage)
        self.Lop_2.clicked.connect(self.switch_to_LopPage)

        self.Sinhvien_1.clicked.connect(self.switch_to_SinhVienPage)
        self.Sinhvien_2.clicked.connect(self.switch_to_SinhVienPage)

        self.KetQua_1.clicked.connect(self.switch_to_KetQuaPage)
        self.KetQua_2.clicked.connect(self.switch_to_KetQuaPage)

        self.HocPhan_1.clicked.connect(self.switch_to_HocPhanPage)
        self.HocPhan_2.clicked.connect(self.switch_to_HocPhanPage)

    def switch_to_KhoaPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_LopPage(self):
        self.stackedWidget.setCurrentIndex(1)       
    def switch_to_SinhVienPage(self):
        self.stackedWidget.setCurrentIndex(2)
        
    def switch_to_KetQuaPage(self):
        self.stackedWidget.setCurrentIndex(3)   

    def switch_to_HocPhanPage(self):
        self.stackedWidget.setCurrentIndex(4)
        
