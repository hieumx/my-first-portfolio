import pandas as pd
import matplotlib.pyplot as plt # Gọi cọ vẽ ra và đặt tên ngắn gọn là plt

print("📊 Khởi động hệ thống phân tích dữ liệu thị trường...")

ten_file = "lich_su_gia_btc.csv"

try:
    df = pd.read_csv(ten_file)
    
    if df.empty:
        print("⚠️ File dữ liệu đang trống rỗng!")
    else:
        print(f"✅ Đã tải thành công {len(df)} bản ghi dữ liệu.\n")
        
        gia_cao_nhat = df["Giá BTC (USDT)"].max()
        gia_thap_nhat = df["Giá BTC (USDT)"].min()
        gia_trung_binh = df["Giá BTC (USDT)"].mean()
        bien_dong = gia_cao_nhat - gia_thap_nhat
        
        print("================ BÁO CÁO PHÂN TÍCH BTC ================")
        print(f"📈 Giá cao nhất (Đỉnh): ${gia_cao_nhat:,.2f}")
        print(f"📉 Giá thấp nhất (Đáy) : ${gia_thap_nhat:,.2f}")
        print(f"⚖️ Giá trung bình      : ${gia_trung_binh:,.2f}")
        print(f"🔄 Biến động (Spread)  : ${bien_dong:,.2f}")
        print("======================================================")

        # -------- PHẦN MỚI: MA THUẬT VẼ BIỂU ĐỒ --------
        print("\n🎨 Đang phác thảo biểu đồ, vui lòng đợi...")
        
        # 1. Tạo ra một bức tranh trống kích thước 10x5
        plt.figure(figsize=(10, 5)) 
        
        # 2. Vẽ đường đi của giá (Trục X: Thời gian, Trục Y: Giá)
        plt.plot(df["Thời gian"], df["Giá BTC (USDT)"], marker='o', color='#fc00ff', linewidth=2)
        
        # 3. Trang trí tiêu đề và nhãn
        plt.title('Biến Động Giá BTC/USDT', fontsize=16, fontweight='bold')
        plt.xlabel('Thời Gian (Lấy mẫu mỗi 5s)', fontsize=12)
        plt.ylabel('Giá Tiền (USDT)', fontsize=12)
        
        # 4. Xoay chữ ở trục thời gian nghiêng 45 độ cho khỏi bị đè lên nhau
        plt.xticks(rotation=45) 
        
        # 5. Kẻ lưới cho dễ nhìn
        plt.grid(True, linestyle='--', alpha=0.6) 
        
        # Căn chỉnh bố cục tự động
        plt.tight_layout() 
        
        # BẬT BIỂU ĐỒ LÊN MÀN HÌNH!
        #plt.show() 
        # LƯU BIỂU ĐỒ THÀNH FILE ẢNH (Thay vì dùng plt.show())
        plt.savefig('btc_chart.png', dpi=300, bbox_inches='tight')
        print("✅ Đã lưu thành công biểu đồ vào file 'btc_chart.png'")

except FileNotFoundError:
    print(f"❌ Không tìm thấy file {ten_file}. Em đã chạy Bot cào dữ liệu chưa?")
except Exception as loi:
    print("❌ Đã xảy ra lỗi:", loi)