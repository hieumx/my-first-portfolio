import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

print("📊 Khởi động hệ thống phân tích dữ liệu từ SQL Database...")

try:
    # BƯỚC 1: Mở cửa nhà kho SQL
    ket_noi = sqlite3.connect("he_thong_data.db")
    
    # BƯỚC 2: Viết thư yêu cầu lấy toàn bộ dữ liệu
    cau_lenh_sql = "SELECT * FROM lich_su_gia"
    
    # BƯỚC 3: Dùng Pandas lấy dữ liệu đóng gói thành DataFrame
    df = pd.read_sql_query(cau_lenh_sql, ket_noi)
    ket_noi.close()
    
    # BƯỚC 4: Bắt đầu tính toán
    if df.empty:
        print("⚠️ Bảng dữ liệu đang trống rỗng. Hãy chạy 'bot_bitcoin.py' trước!")
    else:
        print(f"✅ Đã tải thành công {len(df)} bản ghi từ Database.\n")
        
        # Tính toán đường xu hướng (Trung bình cộng 3 mốc gần nhất)
        df['SMA_3'] = df['gia_usdt'].rolling(window=3).mean()
        
        # Tìm Đỉnh, Đáy, Trung bình trên TOÀN BỘ dữ liệu
        gia_cao_nhat = df["gia_usdt"].max()
        gia_thap_nhat = df["gia_usdt"].min()
        gia_trung_binh = df["gia_usdt"].mean()
        bien_dong = gia_cao_nhat - gia_thap_nhat
        
        # In báo cáo ra Terminal
        print("================ BÁO CÁO PHÂN TÍCH BTC (TỪ SQL) ================")
        print(f"📈 Giá cao nhất (Đỉnh): ${gia_cao_nhat:,.2f}")
        print(f"📉 Giá thấp nhất (Đáy) : ${gia_thap_nhat:,.2f}")
        print(f"⚖️ Giá trung bình      : ${gia_trung_binh:,.2f}")
        print(f"🔄 Biến động (Spread)  : ${bien_dong:,.2f}")
        print("================================================================")

        # Trực quan hóa dữ liệu (Chỉ lấy 30 bản ghi cuối cùng để vẽ cho gọn đẹp)
        print("\n🎨 Đang xuất biểu đồ từ dữ liệu SQL...")
        plt.figure(figsize=(10, 5)) 
        
        df_ve = df.tail(30) # Cắt lấy 30 dòng cuối
        
        # Vẽ đường giá thực tế
        plt.plot(df_ve["thoi_gian"], df_ve["gia_usdt"], marker='o', color='#fc00ff', linewidth=2, label='Giá Thực Tế')
        
        # Vẽ đường xu hướng
        plt.plot(df_ve["thoi_gian"], df_ve['SMA_3'], marker='', color='#00dbde', linewidth=2, linestyle='--', label='Đường Xu Hướng (SMA-3)')
        
        plt.title('Phân Tích Kỹ Thuật: Xu Hướng BTC/USDT (SQL Backend)', fontsize=16, fontweight='bold')
        plt.xlabel('Thời Gian (30 mốc gần nhất)', fontsize=12)
        plt.ylabel('Giá Tiền (USDT)', fontsize=12)
        plt.xticks(rotation=45) 
        plt.grid(True, linestyle='--', alpha=0.6) 
        plt.legend()
        plt.tight_layout() 
        
        # Lưu file ảnh
        plt.savefig('btc_chart.png', dpi=300, bbox_inches='tight')
        print("✅ Đã lưu thành công biểu đồ Database vào file 'btc_chart.png'")

except sqlite3.OperationalError:
    print("❌ Lỗi: Không tìm thấy file 'he_thong_data.db'. Bạn đã chạy Bot cào giá chưa?")
except Exception as loi:
    print("❌ Đã xảy ra lỗi hệ thống:", loi)