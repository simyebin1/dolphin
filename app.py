import streamlit as st
from supabase import create_client

url = "https://rujorlkjtuiutpsgxgrt.supabase.co/rest/v1/"
key = "sb_publishable_04v1jR8Vn--8KisCrknPEw_veaGfG3a"

supabase = create_client(url, key)

mentor_data = {
    "열정송이": {
        "name": "김송이",
        "major": "컴퓨터과학과",
        "student_id": "20학번",
        "interest": "AI · 웹개발 · 프로젝트"
    },
    "새싹송이": {
        "name": "이송이",
        "major": "컴퓨터과학과",
        "student_id": "21학번",
        "interest": "학교생활 · 수강신청"
    },
    "탐구송이": {
        "name": "박송이",
        "major": "컴퓨터과학과",
        "student_id": "19학번",
        "interest": "AI · 데이터사이언스"
    },
    "소통송이": {
        "name": "최송이",
        "major": "컴퓨터과학과",
        "student_id": "22학번",
        "interest": "동아리 · 인간관계"
    }
}

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

# -------------------
# 결과 페이지
# -------------------

elif st.session_state.page == 7:

    # 유형 판별
    if st.session_state.answers["Q4"] == "도전형":
        result = "열정송이"

    elif st.session_state.answers["Q1"] == "학교생활":
        result = "새싹송이"

    elif st.session_state.answers["Q2"] == "AI":
        result = "탐구송이"

    else:
        result = "소통송이"

    # 결과 저장
    st.session_state.type = result

    descriptions = {
        "열정송이": "목표가 생기면 끝까지 도전하는 열정적인 유형입니다.",
        "새싹송이": "새로운 환경에 적응하며 차근차근 성장하는 유형입니다.",
        "탐구송이": "새로운 기술과 지식을 배우는 것을 좋아하는 유형입니다.",
        "소통송이": "사람들과 함께 배우고 성장하는 것을 좋아하는 유형입니다."
    }

    st.title("🎉 매칭 결과")

    st.header(f"당신은 **{result}** 입니다!")

    st.write(descriptions[result])

    st.divider()

    st.subheader("🌱 나와 잘 맞는 선배를 찾았습니다!")

    # -------------------------------
    # Supabase에서 멘토 조회
    # -------------------------------
    response = (
        supabase.table("users")
        .select("*")
        .eq("user_type", "mentor")
        .eq("personality", result)
        .execute()
    )

    if response.data:

        mentor = response.data[0]

        st.success(f"{mentor['name']} 선배에게 매칭 신청하시겠습니까?")

        st.write(f"**학과** : {mentor['major']}")
        st.write(f"**학번** : {mentor['student_id']}")

        # 다음 페이지에서도 사용
        st.session_state.mentor = mentor

        col1, col2 = st.columns(2)

        with col1:
            if st.button("프로필 보기"):
                st.session_state.page = 9
                st.rerun()

        with col2:
            if st.button("매칭 신청"):

                supabase.table("match_requests").insert({

                    "mentor_email": mentor["email"],

                    "mentee_email": "yebin@sook.ac.kr",

                    "status": "pending"

                }).execute()

                st.success("🎉 매칭 신청이 완료되었습니다!")

    else:

        st.warning("현재 조건에 맞는 선배가 없습니다.")
elif st.session_state.page == 9:

    mentor = st.session_state.mentor

    st.title("👩‍🎓 선배 프로필")

    st.header(mentor["name"])

    st.write(f"**학과** : {mentor['major']}")
    st.write(f"**학번** : {mentor['student_id']}")
    st.write(f"**이메일** : {mentor['email']}")

    st.divider()

    st.subheader("소개")

    st.write(
        "안녕하세요! 😊\n\n"
        "후배들과 편하게 소통하고 학교생활, 전공, 진로에 대해 "
        "도움을 드리고 싶습니다!"
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("← 결과로"):
            st.session_state.page = 7
            st.rerun()

    with col2:
        if st.button("매칭 신청"):

            supabase.table("match_requests").insert({

                "mentor_email": mentor["email"],

                "mentee_email": "yebin@sook.ac.kr",   # 테스트용

                "status": "pending"

            }).execute()

            st.success("🎉 매칭 신청이 완료되었습니다!")


elif st.session_state.page == 10:

    st.success("✅ 매칭 신청이 완료되었습니다!")

    st.write("선배의 수락을 기다리는 중입니다...")

    if st.button("수락 결과 확인"):

        st.session_state.page = 11

        st.rerun()

elif st.session_state.page == 11:

    mentor = mentor_data[st.session_state.type]

    st.balloons()

    st.success(f"🎉 {mentor['name']} 선배가 매칭을 수락했습니다!")

    st.write("이제 채팅을 시작할 수 있습니다.")

    if st.button("채팅 시작하기 💬"):

        st.session_state.page = 12

        st.rerun()

elif st.session_state.page == 12:

    mentor = mentor_data[st.session_state.type]

    st.title("💬 채팅")

    st.info(f"{mentor['name']} 선배와 대화 중")

    st.chat_message("assistant").write(
        "안녕하세요! 😊 궁금한 것이 있다면 편하게 질문해주세요."
    )

    message = st.chat_input("메시지를 입력하세요")

    if message:

        st.chat_message("user").write(message)

        st.chat_message("assistant").write(
            "안녕하세요 ^_^"
        )
