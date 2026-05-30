import requests
import time
import datetime
import sqlite3

print("🚀 Khởi động Siêu Bot liên tục cào giá và nạp vào SQL Database...")
print("Nhấn 'Ctrl + C' để dừng Bot.\n")

# Kết nối kho
ket_noi = sqlite3.connect("he_thong_data.db")
con_tro = ket_noi.cursor()

# Đảm bảo đã có kệ hàng
con_tro.execute("""
CREATE TABLE IF NOT EXISTS lich_su_gia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    thoi_gian TEXT,
    gia_usdt REAL
)
""")
ket_noi.commit()

url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

while True:
    try:
        # Cào giá từ Binance
        response = requests.get(url)
        data = response.json()
        gia_btc = float(data["price"])
        
        thoi_gian_hien_tai = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"[{thoi_gian_hien_tai}] 💰 Giá BTC: ${gia_btc:,.2f} -> Đang nạp vào SQL...")
        
        # Nạp dữ liệu mới vào SQL
        cau_lenh_sql = "INSERT INTO lich_su_gia (thoi_gian, gia_usdt) VALUES (?, ?)"
        du_lieu_nap = (thoi_gian_hien_tai, gia_btc)
        con_tro.execute(cau_lenh_sql, du_lieu_nap)
        ket_noi.commit()
        
        # Ngủ 5 giây rồi cào tiếp
        time.sleep(5)

    except KeyboardInterrupt:
        print("\n🛑 Sếp đã dừng Bot.")
        break
    except Exception as loi:
        print("❌ Lỗi mạng:", loi)
        time.sleep(5)

ket_noi.close()