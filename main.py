from PyQt6 import  QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6.QtCore import QDate
from trangchu import MyTrangChu
import sys

app = QApplication(sys.argv)

window = MyTrangChu()

window.show()
app.exec()

def add_SinhVien(self):
        # lay thong tin tu cac o nhap, voi combobox thi lay id
        ten_SinhVien = self.txtTenSinhVien.text()
        Ma_SinhVien = self.txtMaSinhVien.text()
        Ma_Khoa = self.txtMaKhoa.text()
        Ten_Khoa = float(self.TenKhoa.text())
        Ten_Lop = int(self.txtTenLop.text())
        Ma_Mon_Hoc = int(self.txtMaMonHoc.text())
        Nhap_Diem = self.txtNhapDiem.text()
        Ten_Mon_Hoc = int(self.txtTenMonHoc.text())
        So_Tiet = self.txtSoTiet.text()
        Diem_Thanh_Phan = int(self.txtDiemThanhPhan.text())
        Diem_Giua_Ki = int(self.txtDiemGiuaKi.text())
        Diem_Cuoi_Ki = int(self.txtDiemCuoiKi.text())
        #check xem co thieu thong tin nao khong neu co hien thong bao len man hinh
        if not all([ten_SinhVien, Ma_SinhVien, Ma_Khoa, Ten_Khoa, Ten_Lop, Ma_Mon_Hoc, Nhap_Diem, Ten_Mon_Hoc, So_Tiet, Diem_Thanh_Phan, Diem_Giua_Ki, Diem_Cuoi_Ki]):
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đủ thông tin để thêm Sinh Vien.")
            return
        #thuc hien them ve
        try:
            self.db.insert_ve(ten_SinhVien, Ma_SinhVien, Ma_Khoa, Ten_Khoa, Ten_Lop, Ma_Mon_Hoc, Nhap_Diem, Ten_Mon_Hoc, So_Tiet, Diem_Thanh_Phan, Diem_Giua_Ki, Diem_Cuoi_Ki)
            QMessageBox.information(self, "Thông báo", "Đã thêm vé thành công.")
            self.load_data()
            self.clear_data()

        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi thêm vé: {str(e)}")




def update_selected_ve(self):
        # tuong tu them lam sua
        ten_SinhVien = self.txtTenSinhVien.text()
        Ma_SinhVien = self.txtMaSinhVien.text()
        Ma_Khoa = self.txtMaKhoa.text()
        Ten_Khoa = float(self.TenKhoa.text())
        Ten_Lop = int(self.txtTenLop.text())
        Ma_Mon_Hoc = int(self.txtMaMonHoc.text())
        Nhap_Diem = self.txtNhapDiem.text()
        Ten_Mon_Hoc = int(self.txtTenMonHoc.text())
        So_Tiet = self.txtSoTiet.text()
        Diem_Thanh_Phan = int(self.txtDiemThanhPhan.text())
        Diem_Giua_Ki = int(self.txtDiemGiuaKi.text())
        Diem_Cuoi_Ki = int(self.txtDiemCuoiKi.text())
        if not all([ten_SinhVien, Ma_SinhVien, Ma_Khoa, Ten_Khoa, Ten_Lop, Ma_Mon_Hoc, Nhap_Diem, Ten_Mon_Hoc, So_Tiet, Diem_Thanh_Phan, Diem_Giua_Ki, Diem_Cuoi_Ki]):
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đủ thông tin để cập nhật vé.")
            return
        try:
            self.db.update_ve(ten_SinhVien, Ma_SinhVien, Ma_Khoa, Ten_Khoa, Ten_Lop, Ma_Mon_Hoc, Nhap_Diem, Ten_Mon_Hoc, So_Tiet, Diem_Thanh_Phan, Diem_Giua_Ki, Diem_Cuoi_Ki)
            QMessageBox.information(self, "Thông báo", "Đã cập nhật vé thành công.")
            self.clear_data()
            self.load_data()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi cập nhật vé: {str(e)}")



def delete_ve(self):
        # tuong tu them lam xoa
        try:
            id = int(self.txtIDVe.text())
            self.db.delete_ve(id)
            QMessageBox.information(self, "Thông báo", "Đã xóa vé thành công.")
            self.clear_data()
            self.load_data()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi xóa vé: {str(e)}")

