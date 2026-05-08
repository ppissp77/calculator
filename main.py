# main.py

import streamlit as st
import pandas as pd
import plotly.express as px
import random

# -----------------------------------
# 기본 설정
# -----------------------------------
st.set_page_config(
    page_title="다기능 웹앱",
    page_icon="🧮",
    layout="wide"
)

# -----------------------------------
# 사이드바
# -----------------------------------
st.sidebar.title("📌 메뉴")

page = st.sidebar.radio(
    "앱 선택",
    ["계산기", "확률 시뮬레이터"]
)

# =====================================================
# 계산기 페이지
# =====================================================
if page == "계산기":

    st.title("🧮 계산기")

    operation = st.selectbox(
        "연산 종류를 선택하세요",
        ["덧셈", "뺄셈", "곱셈", "나눗셈"]
    )

    # 연산별 입력 UI
    if operation == "덧셈":
        num1 = st.number_input("첫 번째 숫자", value=0.0)
        num2 = st.number_input("두 번째 숫자", value=0.0)
        result = num1 + num2

    elif operation == "뺄셈":
        num1 = st.number_input("빼지는 수", value=0.0)
        num2 = st.number_input("빼는 수", value=0.0)
        result = num1 - num2

    elif operation == "곱셈":
        num1 = st.number_input("첫 번째 숫자", value=0.0)
        num2 = st.number_input("두 번째 숫자", value=0.0)
        result = num1 * num2

    elif operation == "나눗셈":
        num1 = st.number_input("나누어지는 수", value=0.0)
        num2 = st.number_input("나누는 수", value=1.0)

        if num2 != 0:
            result = num1 / num2
        else:
            result = "0으로 나눌 수 없습니다."

    # 계산 버튼
    if st.button("계산하기"):
        st.success(f"결과: {result}")

# =====================================================
# 확률 시뮬레이터 페이지
# =====================================================
elif page == "확률 시뮬레이터":

    st.title("🎲 확률 시뮬레이터")

    sim_type = st.selectbox(
        "시뮬레이션 종류 선택",
        ["주사위", "동전"]
    )

    trial_count = st.number_input(
        "시행 횟수 입력",
        min_value=1,
        max_value=100000,
        value=100,
        step=1
    )

    if st.button("시뮬레이션 시작"):

        # -----------------------------------
        # 주사위 시뮬레이션
        # -----------------------------------
        if sim_type == "주사위":

            results = [
                random.randint(1, 6)
                for _ in range(trial_count)
            ]

            counts = (
                pd.Series(results)
                .value_counts()
                .sort_index()
            )

            df = pd.DataFrame({
                "주사위 눈": counts.index,
                "횟수": counts.values
            })

            fig = px.bar(
                df,
                x="주사위 눈",
                y="횟수",
                text="횟수",
                title="주사위 결과 분포"
            )

            st.plotly_chart(fig, use_container_width=True)

            st.dataframe(df, use_container_width=True)

        # -----------------------------------
        # 동전 시뮬레이션
        # -----------------------------------
        elif sim_type == "동전":

            results = [
                random.choice(["앞면", "뒷면"])
                for _ in range(trial_count)
            ]

            counts = pd.Series(results).value_counts()

            df = pd.DataFrame({
                "결과": counts.index,
                "횟수": counts.values
            })

            fig = px.pie(
                df,
                names="결과",
                values="횟수",
                title="동전 결과 비율"
            )

            st.plotly_chart(fig, use_container_width=True)

            st.dataframe(df, use_container_width=True)
