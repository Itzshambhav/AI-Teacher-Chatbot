import streamlit as st
from chatbot import get_ai_response
from styles import load_css

# ----------------------------------------------------
# PAGE CONFIGURATION
# ----------------------------------------------------

st.set_page_config(
    page_title="AI Teacher Chatbot",
    page_icon="🎓",
    layout="wide"
)

# Load Custom CSS
st.markdown(load_css(), unsafe_allow_html=True)

# ----------------------------------------------------
# SESSION STATE
# ----------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------

with st.sidebar:

    st.title("🎓 AI Teacher")

    st.markdown("---")

    st.subheader("📚 Select Subject")

    subject = st.selectbox(
        "Choose Subject",
        [
            "Programming",
            "Mathematics",
            "Science",
            "General Knowledge",
            "Interview Preparation"
        ]
    )

    st.markdown("---")

    st.subheader("📊 Chat Statistics")

    st.metric("Messages", len(st.session_state.messages))
    st.metric("Model", "Llama 3.3")

    st.markdown("---")

    st.subheader("ℹ️ About")

    st.info("""
This chatbot is powered by

✅ Groq API

🤖 Llama 3.3 70B

Built using

• Python

• Streamlit

• Groq

• Prompt Engineering
""")

    st.markdown("---")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.caption("❤️ Developed by Shambhav Kumar")

# ----------------------------------------------------
# HERO SECTION
# ----------------------------------------------------

st.markdown("""
<div class="hero-card">

<div class="hero-title">

🎓 AI Teacher Chatbot

</div>

<div class="hero-subtitle">

Learn Programming, Mathematics, Science and prepare for interviews with your AI Teacher powered by Groq.

</div>

</div>
""", unsafe_allow_html=True)


# ----------------------------------------------------
# SUGGESTED QUESTIONS
# ----------------------------------------------------

st.subheader("💡 Suggested Questions")

col1, col2 = st.columns(2)

suggested_prompt = None

with col1:

    if st.button("🐍 Explain Python OOP"):
        suggested_prompt = "Explain Python Object Oriented Programming."

    if st.button("📘 Explain DBMS"):
        suggested_prompt = "Explain DBMS in detail."

with col2:

    if st.button("💻 Explain Binary Search"):
        suggested_prompt = "Explain Binary Search."

    if st.button("📊 Stack vs Queue"):
        suggested_prompt = "Difference between Stack and Queue."

st.markdown("---")

# ----------------------------------------------------
# DISPLAY CHAT HISTORY
# ----------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------------------------------
# CHAT INPUT
# ----------------------------------------------------

user_prompt = st.chat_input("Ask your question...")

if suggested_prompt:
    user_prompt = suggested_prompt

if user_prompt:

    with st.chat_message("user"):
        st.markdown(user_prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    with st.spinner("🤖 AI Teacher is thinking..."):

        response = get_ai_response(
            st.session_state.messages,
            subject
        )

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

st.markdown("---")

st.markdown(
"""
<center>

Built with ❤️ using

**Python • Streamlit • Groq API • Llama 3.3 70B**

</center>
""",
unsafe_allow_html=True
)