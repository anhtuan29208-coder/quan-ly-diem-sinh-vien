
# PROJECT: QUAN LY DIEM SINH VIEN
# Ung dung: Python, Pandas, Matplotlib, Streamlit

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Cau hinh trang web
st.set_page_config(
    page_title="Quan ly diem sinh vien",
    page_icon="📚",
    layout="wide"
)

# #1. TAO DATAFRAME
data = {
    "Ho_ten": [
        "Nguyen Van An",
        "Tran Thi Binh",
        "Le Hoang Cuong",
        "Pham Minh Duc",
        "Hoang Thu Ha",
        "Vo Quoc Huy",
        "Dang Ngoc Lan",
        "Bui Thanh Nam",
        "Do Minh Phuong",
        "Nguyen Gia Bao"
    ],
    "Chuyen_can": [9, 8, 10, 7, 9, 6, 8, 10, 7, 9],
    "Giua_ky":    [8, 7, 9, 6, 8, 5, 7, 9, 6, 8],
    "Cuoi_ky":    [9, 8, 9, 5, 9, 4, 6, 10, 5, 9]
}

df = pd.DataFrame(data)

# #2. TINH DIEM TONG KET
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
).round(2)

# #3. XEP LOAI
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# #4. TIEU DE
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.write("Ứng dụng quản lý và thống kê điểm của 10 sinh viên.")

# #5. HIEN THI BANG DIEM
st.subheader("1. Bảng điểm sinh viên")

bang_hien_thi = df.rename(columns={
    "Ho_ten": "Họ và tên",
    "Chuyen_can": "Chuyên cần",
    "Giua_ky": "Giữa kỳ",
    "Cuoi_ky": "Cuối kỳ",
    "Tong_ket": "Tổng kết",
    "Xep_loai": "Xếp loại"
})

st.dataframe(
    bang_hien_thi,
    use_container_width=True,
    hide_index=True
)

# #6. THONG KE
st.subheader("2. Thống kê kết quả học tập")

diem_tb = df["Tong_ket"].mean()
idx_max = df["Tong_ket"].idxmax()
idx_min = df["Tong_ket"].idxmin()
so_dat = int((df["Tong_ket"] >= 5).sum())

cot1, cot2, cot3, cot4 = st.columns(4)

cot1.metric("Điểm trung bình", f"{diem_tb:.2f}")
cot2.metric("Điểm cao nhất", f"{df.loc[idx_max, 'Tong_ket']:.2f}")
cot3.metric("Điểm thấp nhất", f"{df.loc[idx_min, 'Tong_ket']:.2f}")
cot4.metric("Số sinh viên đạt", f"{so_dat}/10")

st.write(
    f"**Sinh viên cao nhất:** {df.loc[idx_max, 'Ho_ten']}"
    f" — {df.loc[idx_max, 'Tong_ket']:.2f}"
)

st.write(
    f"**Sinh viên thấp nhất:** {df.loc[idx_min, 'Ho_ten']}"
    f" — {df.loc[idx_min, 'Tong_ket']:.2f}"
)

# #7. CHON SINH VIEN
st.subheader("3. Tra cứu điểm sinh viên")

ten_chon = st.selectbox(
    "Chọn sinh viên:",
    df["Ho_ten"].tolist()
)

sv = df[df["Ho_ten"] == ten_chon].iloc[0]

st.write(f"### Thông tin: {sv['Ho_ten']}")

a, b, c, d = st.columns(4)
a.metric("Chuyên cần", f"{sv['Chuyen_can']:.2f}")
b.metric("Giữa kỳ", f"{sv['Giua_ky']:.2f}")
c.metric("Cuối kỳ", f"{sv['Cuoi_ky']:.2f}")
d.metric("Tổng kết", f"{sv['Tong_ket']:.2f}")

st.write(f"**Xếp loại:** {sv['Xep_loai']}")

# #8. BIEU DO COT
st.subheader("4. Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(12, 5))

ax.bar(
    df["Ho_ten"],
    df["Tong_ket"],
    edgecolor="black"
)

ax.set_title("ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN")
ax.set_xlabel("Họ và tên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
ax.tick_params(axis="x", labelrotation=45)
ax.grid(axis="y", linestyle="--", alpha=0.5)

fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# #9. THONG TIN NGUOI TAO
st.divider()

st.caption("Người tạo ứng dụng: [Dương Anh Tuấn] | MSSV: [052208013177]")
