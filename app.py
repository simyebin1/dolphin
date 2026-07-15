import streamlit as st

st.set_page_config(
    page_title="선후배 매칭",
    layout="wide"
)

st.title("🎓 선후배 매칭 서비스")

st.write("왼쪽 메뉴에서 매칭을 시작하세요.")

import streamlit as st

st.set_page_config(page_title="매칭 테스트", layout="centered")

# ------------------------
# Session State 초기화
# ------------------------
if "page" not in st.session_state:
    st.session_state.page = 1

if "answers" not in st.session_state:
    st.session_state.answers = {}

# ------------------------
# 제목
# ------------------------

st.title("🎯 선후배 매칭 테스트")

# ------------------------
# Q1
# ------------------------

if st.session_state.page == 1:

    st.subheader("Q1")

    answer = st.radio(
        "어떤 도움을 원하시나요?",
        [
            "수강신청 / 학점 관리 / 전공 공부",
            "진로 고민 / 취업 준비 / 대학원",
            "대외활동 / 공모전 / 자격증 / 교환학생",
            "인간관계 / 기타"
        ]
    )

    if st.button("다음"):
        st.session_state.answers["Q1"] = answer
        st.session_state.page = 2
        st.rerun()

# ------------------------
# Q1-1
# ------------------------

elif st.session_state.page == 2:

    st.subheader("Q1-1")

    answer = st.text_area(
        "현재 가장 고민되는 것은?",
        placeholder="자유롭게 작성해주세요."
    )

    if st.button("다음"):
        st.session_state.answers["Q1-1"] = answer
        st.session_state.page = 3
        st.rerun()

# ------------------------
# Q2
# ------------------------

elif st.session_state.page == 3:

    st.subheader("Q2")

    answer = st.radio(
        "관심 분야는?",
        [
            "AI / 데이터분석",
            "웹 개발",
            "디자인",
            "창업 / 마케팅"
        ]
    )

    if st.button("다음"):
        st.session_state.answers["Q2"] = answer
        st.session_state.page = 4
        st.rerun()

# ------------------------
# Q3
# ------------------------

elif st.session_state.page == 4:

    st.subheader("Q3")

    answer = st.radio(
        "선호하는 멘토(멘티) 유형은?",
        [
            "친절한",
            "꼼꼼한",
            "빠르게 핵심만",
            "친구처럼 편한"
        ]
    )

    if st.button("다음"):
        st.session_state.answers["Q3"] = answer
        st.session_state.page = 5
        st.rerun()

# ------------------------
# Q4
# ------------------------

elif st.session_state.page == 5:

    st.subheader("Q4")

    answer = st.radio(
        "나의 성향은?",
        [
            "외향적",
            "내향적",
            "계획형",
            "즉흥형"
        ]
    )

    if st.button("다음"):
        st.session_state.answers["Q4"] = answer
        st.session_state.page = 6
        st.rerun()

# ------------------------
# Q5
# ------------------------

elif st.session_state.page == 6:

    st.subheader("Q5")

    answer = st.radio(
        "채팅 가능한 시간은?",
        [
            "평일 오전",
            "평일 오후",
            "주말 오전",
            "주말 오후"
        ]
    )

    if st.button("결과 보기"):
        st.session_state.answers["Q5"] = answer

        # 결과 페이지 이동
        st.switch_page("pages/result.py")

import streamlit as st

st.title("당신의 유형은")

st.header("🔥 열정송이")

st.write(
"""
목표가 분명하고
새로운 도전을 즐기는 유형입니다.
"""
)

if st.button("매칭 시작"):

    st.switch_page("pages/3_멘토목록.py")

import streamlit as st

st.title("추천 멘토")

col1,col2,col3=st.columns(3)

with col1:

    st.image("assets/mentor1.jpg")

    st.subheader("김송이")

    st.caption("열정송이")

    if st.button("프로필 보기"):

        st.switch_page("pages/4_멘토프로필.py")

  import streamlit as st

col1,col2=st.columns([1,1])

with col1:

    st.image("assets/mentor1.jpg")

with col2:

    st.title("김송이")

    st.write("컴퓨터과학과")

    st.write("20학번")

    st.write("관심분야")

    st.write("AI · 웹개발 · 프로젝트")

    st.write("멘토링 가능")

    st.write("평일 저녁")

    if st.button("매칭 신청"):

        st.switch_page("pages/5_신청완료.py")

  import streamlit as st

st.success("멘토에게 요청을 보냈습니다!")

st.balloons()

st.write("곧 채팅방이 생성됩니다.")
