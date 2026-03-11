import streamlit as st

# Sidebar Setup
with st.sidebar:
    st.title("HONRAAI")
    st.write("one step at a time")
    st.divider()
    
    st.subheader("Session Stats")
    col1, col2 = st.columns(2)
    col1.metric("Messages", "1")
    col2.metric("Total", "1")
    st.divider()
    
    st.subheader("Controls")
    accent = st.selectbox("Accent", ["Cameroon", "Nigeria", "USA", "UK"])
    temp = st.slider("Model Temperature", 0.0, 2.0, 1.20)

# Main Chat Interface
st.header("Chat with HonraAI")

with st.chat_message("user"):
    st.write("Hello")
with st.chat_message("assitant"):
    st.write("Hello there! I'm HonraAI, your friendly and informative assistant specializing in heart disease. i'm here to help you with questions about heart health, conditions, and riskfactors. How can i assist you today?")
    if st.button("Read aloud"):
        st.info("Playing audio...")
st.divider()

# Chat Input
prompt = st.chat_input("Message HonraAI")