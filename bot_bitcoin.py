import requests
import time       # Trợ thủ canh giờ
import datetime   # Trợ thủ xem đồng hồ
import csv        # Trợ thủ ghi sổ sách

print("🚀 Khởi động Siêu Bot theo dõi BTC/USDT...")
print("Nhấn 'Ctrl + C' bất cứ lúc nào để dừng Bot nhé!\n")

# Tên cuốn sổ chúng ta sẽ ghi chép
ten_file = "lich_su_gia_btc.csv"

# Ghi dòng tiêu đề vào file trước khi bắt đầu lặp (chỉ làm 1 lần)
with open(ten_file, mode='a', newline='', encoding='utf-8') as file:
    nguoi_viet = csv.writer(file)
    # Nếu là file mới tinh, ghi 2 cái cột tiêu đề vào
    nguoi_viet.writerow(["Thời gian", "Giá BTC (USDT)"])

# URL API của Binance
url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

# VÒNG LẶP VÔ TẬN: Dạy Bot làm việc liên tục
while True:
    try:
        # 1. Chạy đi lấy dữ liệu
        response = requests.get(url)
        data = response.json()
        gia_btc = float(data["price"])
        
        # 2. Xem đồng hồ lấy thời gian hiện tại
        thoi_gian_hien_tai = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 3. In ra Terminal cho Sếp Hiếu xem
        print(f"[{thoi_gian_hien_tai}] 💰 Giá BTC: ${gia_btc:,.2f}")
        
        # 4. Âm thầm mở sổ CSV và ghi nối tiếp vào cuối file (mode='a' là append)
        with open(ten_file, mode='a', newline='', encoding='utf-8') as file:
            nguoi_viet = csv.writer(file)
            nguoi_viet.writerow([thoi_gian_hien_tai, gia_btc])
            
        # 5. Nghỉ ngơi 5 giây trước khi chạy vòng lặp tiếp theo
        time.sleep(5)

    except Exception as loi:
        print("❌ Bot vấp ngã! Đang chờ 5s để thử lại... Lỗi:", loi)
        time.sleep(5) # Lỗi cũng phải cho nó nghỉ rồi mới gọi lại, không là sập mạng