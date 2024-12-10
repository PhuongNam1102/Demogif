from PyQt6 import QtCore, QtGui, QtWidgets,uic
from PyQt6.QtWidgets import *
from PyQt6.uic  import loadUi
import sys
import pyodbc as dt
from PyQt6.QtCore import QDate
# cửa sổ đăng nhập
class login_w(QMainWindow):
    def __init__(self):
        super(login_w, self).__init__()
        uic.loadUi("dangnhap.ui",self)
        
        self.btnDangNhap.clicked.connect(self.login)

    def login(self):
        tdn=self.taikhoan.text()
        mk=self.matkhau.text()
        server = 'DESKTOP-UC90H8S'  # Tên server SQL Server của bạn
        database = 'QLDSV'  # Tên cơ sở dữ liệu của bạn

        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )

        #xử lý kết nối
        try:
            conn = dt.connect(connection_string)
            cursor = conn.cursor()
            # Kiểm tra thông tin đăng nhập
            cursor.execute("SELECT * FROM TAIKHOAN WHERE TenTN = ? AND Pass = ?", (tdn, mk))
            result = cursor.fetchone()
            if result:
                print("Đăng nhập thành công!")
                # Chuyển sang cửa sổ chính
                widget.setFixedHeight(713)
                widget.setFixedWidth(1122)
                widget.move(250, 50)
                widget.setCurrentIndex(1)
            else:
                print("Thông tin đăng nhập không đúng!")
                QMessageBox.warning(self, "Lỗi", "Thông tin đăng nhập không đúng!")

            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Lỗi kết nối: {e}")
            QMessageBox.critical(self, "Lỗi", f"Lỗi kết nối: {e}")
        
class Main_w(QMainWindow):
    def __init__(self):
        super(Main_w, self).__init__()
        uic.loadUi("trangchu.ui",self)  

        self.setWindowTitle("trangchu menu")


        self.Khoa_1.clicked.connect(self.switch_to_KhoaPage)
        self.Khoa_2.clicked.connect(self.switch_to_KhoaPage)

        self.Lop_1.clicked.connect(self.switch_to_LopPage)
        self.Lop_2.clicked.connect(self.switch_to_LopPage)

        self.Sinhvien_1.clicked.connect(self.switch_to_SinhVienPage)
        self.Sinhvien_2.clicked.connect(self.switch_to_SinhVienPage)


        self.KetQua_2.clicked.connect(self.switch_to_KetQuaPage)

        self.HocPhan_2.clicked.connect(self.switch_to_HocPhanPage)



        # giao dien quan ly sinh vien
        self.showDSSV()
        self.tableDSSV.cellClicked.connect(self.tableDSSV_Clicked)
        self.btnThemSV.clicked.connect(self.themSV)
        self.btnSuaSV.clicked.connect(self.suaSV)
        self.btnXoaSV.clicked.connect(self.xoaSV)
        #---------------------------
        # giao dien Khoa
        self.showDSK()
        self.tableDSK.cellClicked.connect(self.tableDSK_Clicked)
        self.btnThemKhoa.clicked.connect(self.themKhoa)
        self.btnSuaKhoa.clicked.connect(self.suaKhoa)
        self.btnXoaKhoa.clicked.connect(self.xoaKhoa)
        #---------------------------
        # giao dien Lop
        self.showDSL()
        self.tableDSL.cellClicked.connect(self.tableDSL_Clicked)
        self.btnThemLop.clicked.connect(self.themLop)
        self.btnSuaLop.clicked.connect(self.suaLop)
        self.btnXoaLop .clicked.connect(self.xoaLop)
        #---------------------------
        # giao dien KetQua
        self.showDSKQ()
        self.tableDSKQ.cellClicked.connect(self.tableDSKQ_Clicked)
        self.btnThemKetQua.clicked.connect(self.themKQ)
        self.btnSuaKetQua.clicked.connect(self.suaKQ)
        self.btnXoaKetQua.clicked.connect(self.xoaKQ)
        #---------------------------
        # giao dien HocPhan
        self.showDSHP()
        self.tableDSHP.cellClicked.connect(self.tableDSHP_Clicked)
        self.btnThemHocPhan.clicked.connect(self.themHP)
        self.btnSuaHocPhan.clicked.connect(self.suaHP)
        self.btnXoaHocPhan.clicked.connect(self.xoaHP)
        #---------------------------
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
        
  
    #Giao dien quan ly sinh vien
    def showDSSV(self):
        server = 'DESKTOP-UC90H8S' 
        database = 'QLDSV' 
        
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()
            # Kiểm tra thông tin đăng nhập
        cursor.execute("SELECT * FROM SINHVIEN")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        self.tableDSSV.setRowCount(result.__len__())
        self.tableDSSV.setColumnCount(6)
        self.tableDSSV.setHorizontalHeaderLabels(["Mã sinh viên", "Họ tên", "Ngày sinh", "Giới tính", "Địa chỉ", "Lớp"])
        table_row = 0
        for row in result:
            self.tableDSSV.setItem(table_row, 0, QTableWidgetItem(row[0]))
            self.tableDSSV.setItem(table_row, 1, QTableWidgetItem(row[1]))
            self.tableDSSV.setItem(table_row, 2, QTableWidgetItem(str(row[2])))
            self.tableDSSV.setItem(table_row, 3, QTableWidgetItem(row[3]))
            self.tableDSSV.setItem(table_row, 4, QTableWidgetItem(row[4]))
            self.tableDSSV.setItem(table_row, 5, QTableWidgetItem(row[5]))
            table_row += 1

    def tableDSSV_Clicked(self, row, column):
        self.txtMASV.setText(self.tableDSSV.item(row, 0).text())
        self.txtTenSV.setText(self.tableDSSV.item(row, 1).text())
        self.txtGioiTinh.setText(self.tableDSSV.item(row, 3).text())
        self.txtDiaChi.setText(self.tableDSSV.item(row, 4).text())
        self.txtMaLop.setText(self.tableDSSV.item(row, 5).text())
        date = QDate.fromString(self.tableDSSV.item(row, 2).text(), "yyyy-MM-dd")
        self.txtNgaySinh.setDate(date)

    def themSV(self):
        hoTen = self.txtTenSV.text()
        maSV = self.txtMASV.text()
        ngaySinh = self.txtNgaySinh.date().toString("yyyy-MM-dd")
        gioiTinh = self.txtGioiTinh.text()
        diaChi = self.txtDiaChi.text()
        lop = self.txtMaLop.text()
        #Connect sql
        server = 'DESKTOP-UC90H8S' 
        database = 'QLDSV' 
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()

        # Cau lenh them SV
        query = "INSERT INTO SINHVIEN (MASV, HOTEN, NGAYSINH, GIOITINH, DIACHI, MALOP) VALUES (?, ?, ?, ?, ?, ?)"
        data = (maSV, hoTen, ngaySinh, gioiTinh, diaChi, lop)
        #thuc hien them SV
        try:
            cursor.execute(query, data)
            conn.commit()
            QMessageBox.information(self, "Thông báo", "Thêm thành công!")
            self.showDSSV()
            cursor.close()
            conn.close()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi thêm Sinh Vien: {str(e)}") 

    def suaSV(self):
        hoTen = self.txtTenSV.text()
        maSV = self.txtMASV.text()
        ngaySinh = self.txtNgaySinh.date().toString("yyyy-MM-dd")
        gioiTinh = self.txtGioiTinh.text()
        diaChi = self.txtDiaChi.text()
        lop = self.txtMaLop.text()
        #Connect sql
        server = 'DESKTOP-UC90H8S' 
        database = 'QLDSV' 
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()

        # Cau lenh them SV
        query = "UPDATE SINHVIEN SET HOTEN = ?, NGAYSINH = ?, GIOITINH = ?, DIACHI = ?, MALOP = ? WHERE MASV = ?"
        data = (hoTen, ngaySinh, gioiTinh, diaChi, lop, maSV)
        #thuc hien them SV
        try:
            cursor.execute(query, data)
            conn.commit()
            QMessageBox.information(self, "Thông báo", "Sửa thành công!")
            self.showDSSV()
            cursor.close()
            conn.close()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi Sửa Sinh Vien: {str(e)}")

    def xoaSV(self):
        maSV = self.txtMASV.text()
        #Connect sql
        server = 'DESKTOP-UC90H8S' 
        database = 'QLDSV' 
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()

        # Cau lenh them SV
        query = "DELETE SINHVIEN WHERE MASV = ?"
        data = (maSV)
        #thuc hien them SV
        try:
            cursor.execute(query, data)
            conn.commit()
            QMessageBox.information(self, "Thông báo", "Xóa thành công!")
            self.showDSSV()
            cursor.close()
            conn.close()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi Xóa Sinh Vien: {str(e)}")
    #--------------------------------------------
    
    #code giao dien khoa
    def showDSK(self):
        server = 'DESKTOP-UC90H8S' 
        database = 'QLDSV' 
        
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()
            # Kiểm tra thông tin đăng nhập
        cursor.execute("SELECT * FROM KHOA")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        self.tableDSK.setRowCount(result.__len__())
        self.tableDSK.setColumnCount(3)
        self.tableDSK.setHorizontalHeaderLabels(["Mã Khoa", "Tên Khoa", "Năm Thành Lập", ])
        table_row = 0
        for row in result:
            self.tableDSK.setItem(table_row, 0, QTableWidgetItem(row[0]))
            self.tableDSK.setItem(table_row, 1, QTableWidgetItem(row[1]))
            self.tableDSK.setItem(table_row, 2, QTableWidgetItem(str(row[2])))
            table_row += 1

    def tableDSK_Clicked(self, row, column):
        self.txtMaKhoa.setText(self.tableDSK.item(row, 0).text())
        self.txtTenKhoa.setText(self.tableDSK.item(row, 1).text())
        self.txtNamThanhLap.setText(self.tableDSK.item(row, 2).text())

    def themKhoa(self):
        MaKhoa = self.txtMaKhoa.text()
        TenKhoa = self.txtTenKhoa.text()
        NamThanhLap = self.txtNamThanhLap.text()
        #Connect sql
        server = 'DESKTOP-UC90H8S' 
        database = 'QLDSV' 
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()

        # Cau lenh them Khoa
        query = "INSERT INTO KHOA (MAKHOA, TENKHOA, NAMTHANHLAP) VALUES (?, ?, ?)"
        data = (MaKhoa, TenKhoa, int(NamThanhLap))
        #thuc hien them Khoa
        try:
            cursor.execute(query, data)
            conn.commit()
            QMessageBox.information(self, "Thông báo", "Thêm thành công!")
            self.showDSK()
            cursor.close()
            conn.close()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi thêm Khoa: {str(e)}") 

    def suaKhoa(self):
        MaKhoa = self.txtMaKhoa.text()
        TenKhoa = self.txtTenKhoa.text()
        NamThanhLap = self.txtNamThanhLap.text()
        #Connect sql
        server = 'DESKTOP-UC90H8S' 
        database = 'QLDSV' 
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()

        # Cau lenh sua Khoa
        query = "UPDATE KHOA SET TENKHOA = ?, NAMTHANHLAP = ? WHERE MAKHOA = ?"
        data = (TenKhoa, int(NamThanhLap), MaKhoa)
        #thuc hien sửa Khoa
        try:
            cursor.execute(query, data)
            conn.commit()
            QMessageBox.information(self, "Thông báo", "Sửa thành công!")
            self.showDSK()
            cursor.close()
            conn.close()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi Sửa Khoa: {str(e)}")

    def xoaKhoa(self):
        maKhoa = self.txtMaKhoa.text()
        #Connect sql
        server = 'DESKTOP-UC90H8S' 
        database = 'QLDSV' 
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()

        # Cau lenh XOA Khoa
        query = "DELETE KHOA WHERE MAKHOA = ?"
        data = (maKhoa)
        #thuc hien XOA Khoa
        try:
            cursor.execute(query, data)
            conn.commit()
            QMessageBox.information(self, "Thông báo", "Xóa thành công!")
            self.showDSK()
            cursor.close()
            conn.close()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi Xóa Khoa: {str(e)}")
    #code giao dien Lop
    def showDSL(self): 
        server = 'DESKTOP-UC90H8S' 
        database = 'QLDSV' 
        
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()
            # Kiểm tra thông tin đăng nhập
        cursor.execute("SELECT * FROM LOP")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        self.tableDSL.setRowCount(result.__len__())
        self.tableDSL.setColumnCount(4)
        self.tableDSL.setHorizontalHeaderLabels(["Mã Lớp", "Tên Lớp", "Sĩ Số", "Mã Khoa"])
        table_row = 0
        for row in result:
            self.tableDSL.setItem(table_row, 0, QTableWidgetItem(row[0]))
            self.tableDSL.setItem(table_row, 1, QTableWidgetItem(row[1]))
            self.tableDSL.setItem(table_row, 2, QTableWidgetItem(str(row[2])))
            self.tableDSL.setItem(table_row, 3, QTableWidgetItem(row[3]))
            table_row += 1

    def tableDSL_Clicked(self, row, column):
        self.txtMaLop_2.setText(self.tableDSL.item(row, 0).text())
        self.txtTenLop.setText(self.tableDSL.item(row, 1).text())
        self.txtSiSo.setText(self.tableDSL.item(row, 2).text())
        self.txtMaKhoa_2.setText(self.tableDSL.item(row, 3).text())

    def themLop(self):
        MaLop = self.txtMaLop_2.text()
        TenLop = self.txtTenLop.text()
        SiSo = self.txtSiSo.text()
        MaKhoa = self.txtMaKhoa_2.text()
        #Connect sql
        server = 'DESKTOP-UC90H8S' 
        database = 'QLDSV' 
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()

        # Cau lenh them Lop
        query = "INSERT INTO LOP (MALOP, TENLOP, SISO, MAKHOA) VALUES (?, ?, ?, ?)"
        data = (MaLop, TenLop, SiSo, MaKhoa) 
        #thuc hien them Lop
        try:
            cursor.execute(query, data)
            conn.commit()
            QMessageBox.information(self, "Thông báo", "Thêm thành công!")
            self.showDSL()
            cursor.close()
            conn.close()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi thêm lớp: {str(e)}") 

    def suaLop(self):
        MaLop = self.txtMaLop_2.text()
        TenLop = self.txtTenLop.text()
        SiSo = self.txtSiSo.text()
        MaKhoa = self.txtMaKhoa_2.text()
        #Connect sql
        server = 'DESKTOP-UC90H8S' 
        database = 'QLDSV' 
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()

        # Cau lenh sửa Lop
        query = "UPDATE LOP SET TENLOP = ?, SISO = ?, MAKHOA = ? WHERE MALOP = ?"
        data = (TenLop, SiSo, MaKhoa, MaLop)
        #thuc hien sửa Lop
        try:
            cursor.execute(query, data)
            conn.commit()
            QMessageBox.information(self, "Thông báo", "Sửa thành công!")
            self.showDSL()
            cursor.close()
            conn.close()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi Sửa Lớp: {str(e)}")

    def xoaLop(self):
        maLop = self.txtMaLop_2.text()
        #Connect sql
        server = 'DESKTOP-UC90H8S' 
        database = 'QLDSV' 
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()

        # Cau lenh them Lop
        query = "DELETE LOP WHERE MALOP = ?"
        
        #thuc hien them Lop
        #try:
        cursor.execute(query, (maLop,))
        conn.commit()
        QMessageBox.information(self, "Thông báo", "Xóa thành công!")
        self.showDSL()
        cursor.close()
        conn.close()
        #except Exception as e:
        #    QMessageBox.warning(self, "Lỗi", f"Lỗi khi Xóa Lớp: {str(e)}")
    #---------------------------
    #code giao dien KQ
    def showDSKQ(self):
        server = 'DESKTOP-UC90H8S' 
        database = 'QLDSV' 
        
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()
            # Kiểm tra thông tin đăng nhập
        cursor.execute("SELECT * FROM KETQUA")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        self.tableDSKQ.setRowCount(result.__len__())
        self.tableDSKQ.setColumnCount(6)
        self.tableDSKQ.setHorizontalHeaderLabels(["Mã SV", "Mã HP", "Diem QT", "Diem Thi", "Diem TK", "KQ" ])
        table_row = 0
        for row in result:
            self.tableDSKQ.setItem(table_row, 0, QTableWidgetItem(row[0]))
            self.tableDSKQ.setItem(table_row, 1, QTableWidgetItem(row[1]))
            self.tableDSKQ.setItem(table_row, 2, QTableWidgetItem(str(row[2])))
            self.tableDSKQ.setItem(table_row, 3, QTableWidgetItem(str(row[3])))
            self.tableDSKQ.setItem(table_row, 4, QTableWidgetItem(str(row[4])))
            self.tableDSKQ.setItem(table_row, 5, QTableWidgetItem(str(row[5])))
            table_row += 1

    def tableDSKQ_Clicked(self, row, column):
        self.txtMaSV.setText(self.tableDSKQ.item(row, 0).text())
        self.txtMaHP.setText(self.tableDSKQ.item(row, 1).text())
        self.txtDiemQT.setText(self.tableDSKQ.item(row, 2).text())
        self.txtDiemThi.setText(self.tableDSKQ.item(row, 3).text())
        self.txtDiemTK.setText(self.tableDSKQ.item(row, 4).text())
        self.txtKQ.setCurrentText(self.tableDSKQ.item(row, 5).text()) 

    def themKQ(self):
        MaSV = self.txtMaSV.text()
        MaHP = self.txtMaHP.text()
        DiemQT = self.txtDiemQT.text()
        DiemThi = self.txtDiemThi.text()
        DiemTK = self.txtDiemTK.text()
        KQ = self.txtKQ.currentText()
        #Connect sql
        server = 'DESKTOP-UC90H8S' 
        database = 'QLDSV' 
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()

        # Cau lenh them KQ
        query = "INSERT INTO KETQUA (MaSV, MaHP, DiemQT, DiemThi, DiemTK, KQ) VALUES (?, ?, ?, ?, ?, ?)"
        data = (MaSV, MaHP, DiemQT, DiemThi, DiemTK, KQ)
        #thuc hien them KQ
        try:
            cursor.execute(query, data)
            conn.commit()
            QMessageBox.information(self, "Thông báo", "Thêm thành công!")
            self.showDSKQ()
            cursor.close()
            conn.close()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi thêm Kết Quả: {str(e)}") 

    def suaKQ(self):
        MaSV = self.txtMaSV.text()
        MaHP = self.txtMaHP.text()
        DiemQT = self.txtDiemQT.text()
        DiemThi = self.txtDiemThi.text()
        DiemTK = self.txtDiemTK.text()
        KQ = self.txtKQ.currentText()
        #Connect sql
        server = 'DESKTOP-UC90H8S' 
        database = 'QLDSV' 
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()

        # Cau lenh them KQ
        query = "UPDATE KETQUA SET  MAHP = ?, DIEMQT = ?, DIEMTHI = ?, DIEMTK = ?, KQ = ? WHERE MASV = ?"
        data = (MaHP, DiemQT, DiemThi, DiemTK, KQ, MaSV)
        #thuc hien them KQ
        try:
            cursor.execute(query, data)
            conn.commit()
            QMessageBox.information(self, "Thông báo", "Sửa thành công!")
            self.showDSKQ()
            cursor.close()
            conn.close()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi Sửa Kết Quả: {str(e)}")

    def xoaKQ(self):
        maSV = self.txtMaSV.text()
        #Connect sql
        server = 'DESKTOP-UC90H8S' 
        database = 'QLDSV' 
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()

        # Cau lenh them KQ
        query = "DELETE KETQUA WHERE MASV = ?"
        data = (maSV)
        #thuc hien them KQ
        try: 
            cursor.execute(query, data)
            conn.commit()
            QMessageBox.information(self, "Thông báo", "Xóa thành công!")
            self.showDSKQ()
            cursor.close()
            conn.close()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi Xóa KQ: {str(e)}")
    #code giao dien Hoc Phan

    def showDSHP(self):
        server = 'DESKTOP-UC90H8S' 
        database = 'QLDSV' 
        
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()
            # Kiểm tra thông tin đăng nhập
        cursor.execute("SELECT * FROM HOCPHAN")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        self.tableDSHP.setRowCount(result.__len__())
        self.tableDSHP.setColumnCount(6)
        self.tableDSHP.setHorizontalHeaderLabels(["Mã Học Phần", "Tên Học Phần", "Tín Chỉ", "Học Kỳ", "Mã Khoa", "Phần Trăm QT"])
        table_row = 0
        for row in result:
            self.tableDSHP.setItem(table_row, 0, QTableWidgetItem(row[0]))
            self.tableDSHP.setItem(table_row, 1, QTableWidgetItem(row[1]))
            self.tableDSHP.setItem(table_row, 2, QTableWidgetItem(str(row[2])))
            self.tableDSHP.setItem(table_row, 3, QTableWidgetItem(str(row[3])))
            self.tableDSHP.setItem(table_row, 4, QTableWidgetItem(row[4]))
            self.tableDSHP.setItem(table_row, 5, QTableWidgetItem(str(row[5])))
            table_row += 1

    def tableDSHP_Clicked(self, row, column):
        self.txtMaHocPhan.setText(self.tableDSHP.item(row, 0).text())
        self.txtTenHocPhan.setText(self.tableDSHP.item(row, 1).text())
        self.txtTinChi.setText(self.tableDSHP.item(row, 2).text())
        self.txtHocKy.setText(self.tableDSHP.item(row, 3).text())
        self.txtMaKhoa_3.setText(self.tableDSHP.item(row, 4).text())
        self.txtPhanTramQT.setText(self.tableDSHP.item(row, 5).text())

    def themHP(self):
        MaHocPhan = self.txtMaHocPhan.text()
        TenHocPhan = self.txtTenHocPhan.text()
        TinChi = self.txtTinChi.text()
        HocKy = self.txtHocKy.text()
        MaKhoa = self.txtMaKhoa_3.text()
        PhanTramQT = self.txtPhanTramQT.text()
        #Connect sql
        server = 'DESKTOP-UC90H8S' 
        database = 'QLDSV' 
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()

        # Cau lenh them HP
        query = "INSERT INTO HOCPHAN (MAHP, TENHP, TINCHI, HOCKY, MAKHOA, PHANTRAMQT) VALUES (?, ?, ?, ?, ?, ?)"
        data = (MaHocPhan, TenHocPhan, TinChi, HocKy, MaKhoa, PhanTramQT)
        #thuc hien them HP
        try:
            cursor.execute(query, data)
            conn.commit()
            QMessageBox.information(self, "Thông báo", "Thêm thành công!")
            self.showDSHP()
            cursor.close()
            conn.close()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi thêm Học Phần: {str(e)}") 

    def suaHP(self):
        MaHocPhan = self.txtMaHocPhan.text()
        TenHocPhan = self.txtTenHocPhan.text()
        TinChi = self.txtTinChi.text()
        HocKy = self.txtHocKy.text()
        MaKhoa = self.txtMaKhoa_3.text()
        PhanTramQT = self.txtPhanTramQT.text()
        #Connect sql
        server = 'DESKTOP-UC90H8S' 
        database = 'QLDSV' 
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()

        # Cau lenh them HP
        query = "UPDATE HP SET TENHP = ?, TINCHI = ?, HOCKY = ?, MAKHOA = ?, PhanTramQT = ? WHERE MAHP = ?"
        data = (TenHocPhan, TinChi, HocKy, MaKhoa, PhanTramQT, MaHocPhan)
        #thuc hien them HP
        try:
            cursor.execute(query, data)
            conn.commit()
            QMessageBox.information(self, "Thông báo", "Sửa thành công!")
            self.showDSHP()
            cursor.close()
            conn.close()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi Sửa Học Phàn: {str(e)}")

    def xoaHP(self):
        maHP = self.txtMaHocPhan.text()
        #Connect sql
        server = 'DESKTOP-UC90H8S' 
        database = 'QLDSV' 
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()

        # Cau lenh them HP
        query = "DELETE HOCPHAN WHERE MAHP = ?"
        data = (maHP)
        #thuc hien them HP
        try:
            cursor.execute(query, data)
            conn.commit()
            QMessageBox.information(self, "Thông báo", "Xóa thành công!")
            self.showDSHP()
            cursor.close()
            conn.close()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi xóa học phần: {str(e)}")
    #---------------------------
# xử lý
app =QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
login_f=login_w()
main_f = Main_w()
widget.addWidget(login_f)
widget.addWidget(main_f)
widget.setFixedHeight(500)
widget.setFixedWidth(700)
widget.setCurrentIndex(0)
widget.show()
app.exec()
