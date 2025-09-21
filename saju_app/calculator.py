# saju_web_app.py
import streamlit as st
from datetime import datetime
from saju_app.calculator import compute_bazi

ELEMENT_MAPPING = {
    "목": {"color": "청색 (동쪽)", "numbers": [3, 8]},
    "화": {"color": "적색 (남쪽)", "numbers": [2, 7]},
    "토": {"color": "황색 (중앙)", "numbers": [5, 10]},
    "금": {"color": "백색 (서쪽)", "numbers": [4, 9]},
    "수": {"color": "흑색 (북쪽)", "numbers": [1, 6]},
}

def recommend(five_elements):
    weakest = min(five_elements, key=five_elements.get)
    data = ELEMENT_MAPPING.get(weakest, {})
    return weakest, data.get("color"), data.get("numbers", [])

def main():
    st.title("🧧 사주 오방색 & 숫자 추천기")
    st.write("사주팔자를 기반으로 부족한 오행을 보완할 색과 숫자를 추천합니다.")

    col1, col2 = st.columns(2)
    with col1:
        birth_date = st.date_input("생년월일")
    with col2:
        birth_time = st.time_input("출생 시간")

    timezone_str = st.selectbox("시간대", ["Asia/Seoul", "UTC", "America/New_York"])

    if st.button("추천받기"):
        try:
            import pytz
            tz = pytz.timezone(timezone_str)
            dt = datetime.combine(birth_date, birth_time).astimezone(tz)
            result = compute_bazi(dt)
            weakest, color, numbers = recommend(result.five_elements)

            st.subheader("결과 요약")
            st.write(f"부족한 오행: **{weakest}**")
            st.write(f"추천 오방색: **{color}**")
            st.write(f"추천 숫자: **{numbers}**")

        except Exception as e:
            st.error(f"에러 발생: {e}")

if __name__ == "__main__":
    main()
