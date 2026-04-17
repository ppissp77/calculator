import streamlit as st
import math

st.set_page_config(page_title="다기능 계산기", page_icon="🧮")

st.title("🧮 다기능 계산기")
st.write("연산을 먼저 선택하면 필요한 값을 입력할 수 있습니다.")

# -----------------------------
# 1️⃣ 연산 선택
# -----------------------------
operation = st.selectbox(
    "연산 종류 선택",
    [
        "덧셈",
        "뺄셈",
        "곱셈",
        "나눗셈",
        "모듈러 연산 (%)",
        "지수 연산 (거듭제곱)",
        "로그 연산"
    ]
)

st.divider()

# -----------------------------
# 2️⃣ 연산별 입력 UI
# -----------------------------

try:
    # 덧셈
    if operation == "덧셈":
        a = st.number_input("첫 번째 숫자")
        b = st.number_input("두 번째 숫자")

        if st.button("계산"):
            st.success(f"결과: {a + b}")

    # 뺄셈
    elif operation == "뺄셈":
        a = st.number_input("첫 번째 숫자")
        b = st.number_input("두 번째 숫자")

        if st.button("계산"):
            st.success(f"결과: {a - b}")

    # 곱셈
    elif operation == "곱셈":
        a = st.number_input("첫 번째 숫자")
        b = st.number_input("두 번째 숫자")

        if st.button("계산"):
            st.success(f"결과: {a * b}")

    # 나눗셈
    elif operation == "나눗셈":
        a = st.number_input("나누어지는 수 (피제수)")
        b = st.number_input("나누는 수 (제수)")

        if st.button("계산"):
            if b == 0:
                st.error("❌ 0으로 나눌 수 없습니다.")
            else:
                st.success(f"결과: {a / b}")

    # 모듈러
    elif operation == "모듈러 연산 (%)":
        a = st.number_input("나누어지는 수")
        b = st.number_input("나누는 수")

        if st.button("계산"):
            if b == 0:
                st.error("❌ 0으로 나눌 수 없습니다.")
            else:
                st.success(f"결과: {a % b}")

    # 지수
    elif operation == "지수 연산 (거듭제곱)":
        a = st.number_input("밑 (base)")
        b = st.number_input("지수 (exponent)")

        if st.button("계산"):
            st.success(f"결과: {a ** b}")

    # 로그
    elif operation == "로그 연산":
        x = st.number_input("진수 (0보다 커야 함)")
        base = st.number_input("밑 (0보다 크고 1이 아니어야 함)", value=math.e)

        if st.button("계산"):
            if x <= 0:
                st.error("❌ 진수는 0보다 커야 합니다.")
            elif base <= 0 or base == 1:
                st.error("❌ 밑은 0보다 크고 1이 아니어야 합니다.")
            else:
                st.success(f"결과: {math.log(x, base)}")

except Exception as e:
    st.error(f"오류 발생: {e}")
