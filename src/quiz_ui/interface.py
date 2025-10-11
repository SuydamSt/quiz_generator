import streamlit as st

from quiz_core.quiz_manager import QuizManager as qm

class QuizInterface:
    """streamlit interface"""

    def __init__(self):
        if "manager" not in st.session_state:
            st.session_state.manager = qm()

    def render(self):
        st.title("[quiz title]")
        st.write("V[0.1.1]")

        manager = st.session_state.manager
        question = manager.get_question()
        st.subheader(question["question"])

        user_input = st.text_input("answer here...")
        if st.button("submit"):
            correct = manager.submit_answer(user_input)
            if correct:
                st.success("correct")
            else:
                st.error("wrong")
            
        score_data = manager.get_score()
        st.write(f"score = {score_data["score"]}/{score_data["total"]}")

        if st.button("reset quiz"):
            manager.reset()
