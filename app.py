import streamlit as st

st.set_page_config(
    page_title="선후배 매칭",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 선후배 매칭 서비스")

st.markdown("""
### 환영합니다!

왼쪽 메뉴에서 **매칭 테스트**를 시작해주세요.
""")

import streamlit as st

st.title("🎯 선후배 매칭 테스트")

if "page" not in st.session_state:
    st.session_state.page = 1

if "answers" not in st.session_state:
    st.session_state.answers = {}

# -------------------
# Q1
# -------------------

if st.session_state.page == 1:

    answer = st.radio(
        "Q1. 어떤 도움을 받고 싶나요?",
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

# -------------------
# Q1-1
# -------------------

elif st.session_state.page == 2:

    answer = st.text_area(
        "Q1-1. 현재 가장 고민되는 것은 무엇인가요?"
    )

    if st.button("다음"):
        st.session_state.answers["Q1-1"] = answer
        st.session_state.page = 3
        st.rerun()

# -------------------
# Q2
# -------------------

elif st.session_state.page == 3:

    answer = st.radio(
        "Q2. 관심 분야는?",
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

# -------------------
# Q3
# -------------------

elif st.session_state.page == 4:

    answer = st.radio(
        "Q3. 어떤 선배를 만나고 싶나요?",
        [
            "친절한 선배",
            "꼼꼼한 선배",
            "친구 같은 선배",
            "경험이 많은 선배"
        ]
    )

    if st.button("다음"):
        st.session_state.answers["Q3"] = answer
        st.session_state.page = 5
        st.rerun()

# -------------------
# Q4
# -------------------

elif st.session_state.page == 5:

    answer = st.radio(
        "Q4. 나를 가장 잘 표현하는 것은?",
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

# -------------------
# Q5
# -------------------

elif st.session_state.page == 6:

    answer = st.radio(
        "Q5. 멘토링 가능한 시간은?",
        [
            "평일",
            "주말",
            "저녁",
            "상관없음"
        ]
    )

    if st.button("결과 보기"):
        st.session_state.answers["Q5"] = answer
        st.switch_page("pages/2_결과.py")

import streamlit as st

st.title("🌱 매칭 결과")

st.header("당신의 유형은")

st.success("🔥 열정송이")

st.write("""
목표를 세우면 끝까지 도전하는 열정적인 유형입니다.
""")

if st.button("추천 멘토 보기"):
    st.switch_page("pages/3_멘토목록.py")

import streamlit as st

st.title("추천 멘토")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("assets/mentor1.jpg", use_container_width=True)
    st.subheader("김송이")
    st.caption("열정송이")

    if st.button("프로필 보기"):
        st.switch_page("pages/4_멘토프로필.py")

import streamlit as st

col1, col2 = st.columns([1, 2])

with col1:
    st.image("assets/mentor1.jpg", use_container_width=True)

with col2:

    st.title("김송이")

    st.write("컴퓨터과학과")

    st.write("20학번")

    st.write("관심 분야")
    st.write("AI · 웹개발 · 프로젝트")

    st.write("멘토링 가능 시간")
    st.write("평일 저녁")

    if st.button("매칭 신청"):
        st.switch_page("pages/5_신청완료.py")

import streamlit as st

st.success("매칭 신청이 완료되었습니다! 🎉")

st.balloons()

st.write("멘토가 수락하면 채팅을 시작할 수 있습니다.")

