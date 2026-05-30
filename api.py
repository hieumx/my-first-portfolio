from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

# Khởi tạo Máy chủ
app = FastAPI()

# BẬT TÍNH NĂNG CORS (Cho phép truy cập từ mọi nguồn)
# Nó giống như một giấy phép thông hành, cho phép trang web HTML
# (đang chạy ở một cổng khác) được quyền lấy dữ liệu từ máy chủ Python này.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho phép tất cả nguồn truy cập
    allow_methods=["*"],  # Cho phép tất cả phương thức HTTP (GET, POST, v.v.)
    allow_headers=["*"],  # Cho phép tất cả các header
)
# Định tuyến Routing : tạo ra đường dẫn /api/gia-btc
@app.get("/api/gia-btc")
def lay_du_lieu_bitocin():
   # 1. Mở cửa kho SQL
    ket_noi = sqlite3.connect("he_thong_data.db")
    con_tro = ket_noi.cursor()
    
    # 2. Lấy 20 mốc giá gần nhất (Tránh lấy cả nghìn dòng làm web bị chậm)
    con_tro.execute("SELECT thoi_gian, gia_usdt FROM lich_su_gia ORDER BY id DESC LIMIT 20")
    du_lieu = con_tro.fetchall()
    ket_noi.close()
    
    # 3. Phân loại dữ liệu thô thành 2 danh sách riêng biệt
    thoi_gian_list = []
    gia_list = []
    
    # Vì lấy ngược từ dưới lên (DESC) để được dữ liệu mới nhất, 
    # ta phải dùng lệnh 'reversed' để lật ngược mảng lại từ trái qua phải cho đúng trục thời gian
    for dong in reversed(du_lieu): 
        thoi_gian_list.append(dong[0])
        gia_list.append(dong[1])
        
    # 4. Đóng gói thành chuẩn JSON quốc tế và trả về cho người dùng
    return {
        "thoi_gian": thoi_gian_list,
        "gia_usd": gia_list
    }