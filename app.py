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

    # -------------------
    # 유형 판별
    # -------------------

    if st.session_state.answers["Q4"] == "도전형":
        result = "열정송이"

    elif st.session_state.answers["Q1"] == "학교생활":
        result = "새싹송이"

    elif st.session_state.answers["Q2"] == "AI":
        result = "탐구송이"

    else:
        result = "소통송이"

    st.session_state.type = result

    st.title("🎉 매칭 결과")

    st.success(f"당신의 유형은 **{result}** 입니다!")

    if result == "열정송이":
        st.write("목표가 생기면 끝까지 도전하는 열정적인 유형입니다.")

    elif result == "새싹송이":
        st.write("학교생활을 하나씩 배워가며 성장하는 유형입니다.")

    elif result == "탐구송이":
        st.write("새로운 기술을 배우는 것을 좋아하는 유형입니다.")

    elif result == "소통송이":
        st.write("사람들과 함께 성장하는 것을 좋아합니다.")

    if st.button("선배 매칭하기"):

        st.session_state.page = 8

        st.rerun()

elif st.session_state.page == 8:

    mentor_data = {

        "열정송이":{
            "name":"김송이",
            "major":"컴퓨터과학과",
            "student_id":"20학번",
            "interest":"AI · 웹개발 · 프로젝트"
        },

        "새싹송이":{
            "name":"이송이",
            "major":"컴퓨터과학과",
            "student_id":"21학번",
            "interest":"학교생활 · 수강신청"
        },

        "탐구송이":{
            "name":"박송이",
            "major":"컴퓨터과학과",
            "student_id":"19학번",
            "interest":"AI · 데이터사이언스"
        },

        "소통송이":{
            "name":"최송이",
            "major":"컴퓨터과학과",
            "student_id":"22학번",
            "interest":"동아리 · 인간관계"
        }

    }

    mentor = mentor_data[st.session_state.type]

    st.title("🎉 매칭 완료!")

    st.success(f"{mentor['name']} 선배와 매칭되었습니다!")

    st.write(f"**학과** : {mentor['major']}")

    st.write(f"**학번** : {mentor['student_id']}")

    st.write(f"**관심 분야** : {mentor['interest']}")

    if st.button("프로필 보기"):

        st.session_state.page = 9

        st.rerun()
elif st.session_state.page == 9:

    mentor = mentor_data[st.session_state.type]

    st.title(mentor["name"])

    st.subheader(mentor["major"])

    st.write(mentor["student_id"])

    st.write("관심 분야")

    st.write(mentor["interest"])

    st.write("### 한마디")

    st.info("궁금한 것이 있다면 언제든 편하게 질문해주세요!")

    if st.button("매칭 신청"):

        st.session_state.page = 10

        st.rerun()

elif st.session_state.page == 10:

    st.success("매칭 신청이 완료되었습니다!")

    st.balloons()

