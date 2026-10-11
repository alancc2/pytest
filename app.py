import streamlit as st
import pandas as pd
import numpy as np

# 網頁標題與說明
st.title("📊 我的第一個 Streamlit 數據儀表板")
st.write("這是一個不需要寫任何 HTML 就能生成的互動網頁！")

# 側面欄 (Sidebar) 互動組件
st.sidebar.header("使用者設定")
name = st.sidebar.text_input("輸入你的名字", "訪客")
chart_rows = st.sidebar.slider("選擇數據筆數", 10, 100, 50)

# 動態顯示個人化問候
st.subheader(f"歡迎，{name}！")

# 生成隨機數據與圖表
chart_data = pd.DataFrame(
    np.random.randn(chart_rows, 3),
    columns=['指標 A', '指標 B', '指標 C']
)

# 顯示趨勢折線圖
st.write("### 📈 即時數據趨勢")
st.line_chart(chart_data)

# 顯示數據表格
if st.checkbox("顯示原始數據表格"):
    st.dataframe(chart_data)