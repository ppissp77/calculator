import streamlit as st
import math

st.set_page_config(page_title="다기능 계산기", page_icon="🧮")

st.title("🧮 다기능 계산기")

# 탭 구성
tab1, tab2 = st.tabs(["기본/지수/모듈러", "로그 연산"])

# -----------------------------
# 1️⃣ 기본 + 지수 + 모듈러
# -----------------------------
with tab1:
    st.subheader("기본 연산 / 지수 / 모듈러")

    num1 = st.number_input("첫 번째 숫자", value=0.0)
    num2 = st.number_input("두 번째 숫자", value=1.0)

    operation = st.selectbox(
        "연산 선택",
        ["+", "-", "*", "/", "% (모듈러)", "** (지수)"]
    )

    if st.button("계산하기", key="calc1"):
        try:
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    result = "❌ 0으로 나눌 수 없음"
                else:
                    result = num1 / num2
            elif operation == "% (모듈러)":
                result = num1 % num2
            elif operation == "** (지수)":
                result = num1 ** num2

            st.success(f"결과: {result}")

        except Exception as e:
            st.error(f"오류 발생: {e}")

# -----------------------------
# 2️⃣ 로그 연산
# -----------------------------
with tab2:
    st.subheader("로그 계산")

    number = st.number_input("로그 값 (양수만)", value=1.0)
    base = st.number_input("밑 (기본값 e)", value=math.e)

    if st.button("로그 계산", key="calc2"):
        try:
            if number <= 0:
                st.error("❌ 로그는 0보다 큰 값만 가능")
            elif base <= 0 or base == 1:
                st.error("❌ 밑은 0보다 크고 1이 아니어야 함")
            else:
                result = math.log(number, base)
                st.success(f"결과: {result}")

        except Exception as e:
            st.error(f"오류 발생: {e}")
