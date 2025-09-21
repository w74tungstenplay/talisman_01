import streamlit as st
from datetime import datetime
from calculator import calculate_five_elements, recommend

st.set_page_config(page_title="사주 오방색 추천기", layout="centered")

def main():
    st.title("🧧 사주 오방색 & 숫자 추천기")
    st.write("사주팔자를 기반으로, 당신에게 부족한 오행을 보완할 오방색과 숫자를 추천합니다.")

    # 사용자 입력 받기
    col1, col2 = st.columns(2)
    with col1:
        birth_date = st.date_input("생년월일", value=datetime(1990, 1, 1))
    with col2:
        birth_time = st.time_input("출생 시간", value=datetime.now().time())

    if st.button("🔍 추천받기"):
        try:
            five_elements = calculate_five_elements(birth_date, birth_time)
            result = recommend(five_elements)

            st.subheader("🪐 분석 결과")
            st.write("👉 오행 구성:")
            st.json(five_elements)

            st.markdown("### 🧭 부족한 오행 및 추천 항목")
            for item in result['추천']:
                st.markdown(f"""
                - 부족한 오행: **{item['오행']}**
                - 오방색 추천: 🎨 **{item['오방색']}**
                - 숫자 추천: 🔢 {item['추천 숫자']}
                """)

        except Exception as e:
            st.error(f"⚠️ 오류 발생: {e}")

if __name__ == "__main__":
    main()
