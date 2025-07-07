import streamlit as st
import pandas as pd

# ---------------------------
# 🎨 계별 색상 정의 (파스텔톤)
# ---------------------------
kingdom_colors = {
    "원핵생물계": "#B2EBF2",  # 연하늘
    "원생생물계": "#D1C4E9",  # 연보라
    "균계":     "#FFECB3",  # 연노랑
    "식물계":   "#C8E6C9",  # 연초록
    "동물계":   "#FFCDD2",  # 연분홍
}

# ---------------------------
# 🧬 생물 데이터
# ---------------------------
data = {
    "이름": ["대장균", "남세균", "아메바", "갈조류", "곰팡이", "송이버섯", "소철", "민들레", "사자", "말미잘"],
    "핵": ["X", "X", "O", "O", "O", "O", "O", "O", "O", "O"],
    "다세포": ["X", "X", "X", "O", "O", "O", "O", "O", "O", "O"],
    "광합성": ["X", "O", "X", "O", "X", "X", "X", "X", "X", "X"],
    "먹이 섭취": ["O", "X", "O", "X", "X", "X", "X", "X", "O", "O"],
    "흡수 영양": ["X", "X", "X", "X", "O", "O", "X", "X", "X", "X"],
    "균사": ["X", "X", "X", "X", "O", "O", "X", "X", "X", "X"],
    "기관 발달": ["X", "X", "X", "X", "X", "X", "O", "O", "O", "O"],
    "세포벽": ["O", "O", "X", "O", "O", "O", "O", "O", "X", "X"],
    "계": ["원핵생물계", "원핵생물계", "원생생물계", "원생생물계", "균계", "균계", "식물계", "식물계", "동물계", "동물계"]
}
df = pd.DataFrame(data)

# ---------------------------
# 🌟 Streamlit UI 구성
# ---------------------------
st.set_page_config(page_title="생물 특징 탐색", layout="wide")
st.title("🧪 생물 특징 탐색기")
st.markdown("아이콘을 클릭해서 생물의 특징을 강조해보세요! 💡")

# ---------------------------
# 🧩 계 필터 선택
# ---------------------------
selected_kingdom = st.multiselect("🌱 보고 싶은 생물의 계를 선택하세요 (복수 선택 가능)", options=df["계"].unique(), default=df["계"].unique())
filtered_df = df[df["계"].isin(selected_kingdom)]

# ---------------------------
# 🔍 특징 선택 및 O/X 버튼
# ---------------------------
feature_columns = df.columns.drop(["이름", "계"])
selected_feature = st.selectbox("🔎 강조할 생물의 특징을 선택하세요:", feature_columns)

cols = st.columns(2)
selected_value = None
if cols[0].button("⭕ 있음"):
    selected_value = "O"
if cols[1].button("❌ 없음"):
    selected_value = "X"

# ---------------------------
# 🎨 행 강조 함수
# ---------------------------
def highlight_rows(row):
    base_color = kingdom_colors.get(row["계"], "#FFFFFF")
    if selected_value and row[selected_feature] == selected_value:
        return [f'background-color: {base_color}'] * len(row)
    return [''] * len(row)

# ---------------------------
# 📊 데이터프레임 출력
# ---------------------------
st.markdown("### 🧬 생물 목록")
if selected_value:
    st.dataframe(filtered_df.style.apply(highlight_rows, axis=1), use_container_width=True)
else:
    st.dataframe(filtered_df, use_container_width=True)
