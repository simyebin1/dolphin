import streamlit as st

st.set_page_config(
    page_title="선후배 매칭",
    layout="centered"
)

if "page" not in st.session_state:
    st.session_state.page = 1

if "answers" not in st.session_state:
    st.session_state.answers = {}

if st.session_state.page == 1:

    st.title("Q1")

    answer = st.radio(
        "어떤 도움을 받고 싶나요?",
        [
            "학교생활",
            "전공",
            "취업",
            "대외활동"
        ]
    )

    if st.button("다음"):

        st.session_state.answers["Q1"] = answer

        st.session_state.page = 2

        st.rerun()

elif st.session_state.page == 2:

    st.title("Q1-1")

    answer = st.text_area(
        "현재 가장 고민되는 것은?"
    )

    if st.button("다음"):

        st.session_state.answers["Q1-1"] = answer

        st.session_state.page = 3

        st.rerun()


elif st.session_state.page == 3:

    st.title("Q2")

    answer = st.radio(
        "관심 분야는?",
        [
            "AI",
            "웹개발",
            "앱개발",
            "디자인"
        ]
    )

    if st.button("다음"):

        st.session_state.answers["Q2"] = answer

        st.session_state.page = 4

        st.rerun()

elif st.session_state.page == 4:

    st.title("Q3")

    answer = st.radio(
        "어떤 선배를 만나고 싶나요?",
        [
            "친절한",
            "친구 같은",
            "경험 많은",
            "꼼꼼한"
        ]
    )

    if st.button("다음"):

        st.session_state.answers["Q3"] = answer

        st.session_state.page = 5

        st.rerun()

elif st.session_state.page == 5:

    st.title("Q4")

    answer = st.radio(
        "나의 성향은?",
        [
            "도전형",
            "계획형",
            "신중형",
            "사교형"
        ]
    )

    if st.button("다음"):

        st.session_state.answers["Q4"] = answer

        st.session_state.page = 6

        st.rerun()

elif st.session_state.page == 6:

    st.title("Q5")

    answer = st.radio(
        "멘토링 가능한 시간은?",
        [
            "평일",
            "주말",
            "저녁",
            "상관없음"
        ]
    )

    if st.button("결과 보기"):

        st.session_state.answers["Q5"] = answer

        st.session_state.page = 7

        st.rerun()

elif st.session_state.page == 7:

    st.title("✨ 결과")

    st.success("당신의 유형은 열정송이입니다!")

    st.write(
        "목표를 세우면 끝까지 도전하는 열정적인 유형입니다."
    )

    if st.button("추천 멘토 보기"):

        st.session_state.page = 8

        st.rerun()

elif st.session_state.page == 8:

    st.title("추천 멘토")

    st.subheader("👩 김송이")

    st.write("컴퓨터과학과")

    st.write("20학번")

    if st.button("프로필 보기"):

        st.session_state.page = 9

        st.rerun()

elif st.session_state.page == 9:

    st.title("김송이")

    st.write("컴퓨터과학과")

    st.write("20학번")

    st.write("관심 분야")

    st.write("AI · 웹개발")

    st.write("가능 시간")

    st.write("평일 저녁")

    if st.button("매칭 신청"):

        st.session_state.page = 10

        st.rerun()

elif st.session_state.page == 10:

    st.success("매칭 신청이 완료되었습니다!")

    st.balloons()

