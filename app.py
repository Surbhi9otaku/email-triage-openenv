import streamlit as st
from env import EmailEnv
from models import EmailAction

env = EmailEnv()

if "email" not in st.session_state:
    st.session_state.email = env.reset()

st.title("Email Triage System")

st.write("Email:", st.session_state.email)

response = st.text_input("Your response")

if st.button("Submit"):
    action = EmailAction(response=response)
    email, reward, done, _ = env.step(action)

    st.write("Reward:", reward)

    if done:
        st.write("Finished!")
    else:
        st.session_state.email = email