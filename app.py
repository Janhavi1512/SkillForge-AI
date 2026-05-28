import streamlit as st
from recommender import get_gap
from data import skills_db

st.title("SkillForge AI 🚀")
st.subheader("Personalized Learning Path Generator")

user_input = st.text_input("Enter your skills (comma separated)")

role = st.selectbox("Select Target Role", list(skills_db.keys()))

if st.button("Generate Roadmap"):

    user_skills = [x.strip() for x in user_input.split(",")]

    missing_skills = get_gap(user_skills, role)

    st.write("### Missing Skills")
    st.write(missing_skills)

    st.write("### Learning Roadmap")

    for i, skill in enumerate(missing_skills):
        st.write(f"Week {i+1}: Learn {skill}")