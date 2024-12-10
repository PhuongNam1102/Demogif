import pyodbc as dt
def testConnect():
        server = 'DESKTOP-UC90H8S'  # Tên server SQL Server của bạn
        database = 'QLDSV'  # Tên cơ sở dữ liệu của bạn
        
        connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        )
        conn = dt.connect(connection_string)
        cursor = conn.cursor()
            # Kiểm tra thông tin đăng nhập
        cursor.execute("SELECT * FROM TAIKHOAN")
        result = cursor.fetchone()
        return result

print(testConnect())

