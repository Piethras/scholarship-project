import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv("key.env")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# ── Page config ──────────────────────────────────────────
st.set_page_config(
    page_title="LangChain Playground",
    page_icon="⛓️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap');

/* ── base ── */
html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
}

/* ── dark background ── */
.stApp {
    background: #0d1117;
    color: #e6edf3;
}

/* ── sidebar ── */
[data-testid="stSidebar"] {
    background: #161b22 !important;
    border-right: 1px solid #21262d;
}
[data-testid="stSidebar"] .stRadio label {
    color: #8b949e !important;
    font-family: 'Syne', sans-serif;
    font-size: 0.9rem;
}

/* ── hide default streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem; padding-bottom: 2rem; }

/* ── headings ── */
h1, h2, h3 { font-family: 'Syne', sans-serif !important; }

/* ── hero banner ── */
.hero-banner {
    background: linear-gradient(135deg, #0d1117 0%, #161b22 50%, #0d1117 100%);
    border: 1px solid #21262d;
    border-radius: 16px;
    padding: 2rem 2.5rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 220px; height: 220px;
    background: radial-gradient(circle, rgba(35,134,54,0.18) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-banner::after {
    content: '';
    position: absolute;
    bottom: -40px; left: 30%;
    width: 160px; height: 160px;
    background: radial-gradient(circle, rgba(88,166,255,0.10) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    background: linear-gradient(90deg, #58a6ff, #3fb950);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0 0 0.3rem 0;
}
.hero-sub {
    color: #8b949e;
    font-size: 0.95rem;
    margin: 0;
}

/* ── exercise card ── */
.ex-card {
    background: #161b22;
    border: 1px solid #21262d;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1.2rem;
    transition: border-color 0.2s;
}
.ex-card:hover { border-color: #3fb950; }

/* ── badge ── */
.badge {
    display: inline-block;
    background: #1f6feb22;
    color: #58a6ff;
    border: 1px solid #1f6feb55;
    border-radius: 20px;
    padding: 2px 12px;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    margin-bottom: 0.6rem;
    font-family: 'JetBrains Mono', monospace;
}
.badge-green {
    background: #23863622;
    color: #3fb950;
    border-color: #23863655;
}

/* ── section title ── */
.sec-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: #e6edf3;
    margin: 0 0 0.3rem 0;
}
.sec-desc {
    color: #8b949e;
    font-size: 0.88rem;
    margin: 0 0 1rem 0;
    line-height: 1.5;
}

/* ── output box ── */
.output-box {
    background: #0d1117;
    border: 1px solid #21262d;
    border-left: 3px solid #3fb950;
    border-radius: 8px;
    padding: 1rem 1.2rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.82rem;
    color: #aff5b4;
    white-space: pre-wrap;
    word-break: break-word;
    line-height: 1.6;
}
.output-box-blue {
    border-left-color: #58a6ff;
    color: #cae8ff;
}

/* ── info tip ── */
.tip-box {
    background: #1f6feb11;
    border: 1px solid #1f6feb33;
    border-radius: 8px;
    padding: 0.7rem 1rem;
    color: #58a6ff;
    font-size: 0.82rem;
    margin: 0.5rem 0 1rem 0;
}
.tip-box-yellow {
    background: #e3b34111;
    border-color: #e3b34133;
    color: #e3b341;
}

/* ── divider ── */
.glow-divider {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, #21262d, transparent);
    margin: 1.5rem 0;
}

/* ── chat bubble ── */
.chat-human {
    background: #1f6feb22;
    border: 1px solid #1f6feb44;
    border-radius: 12px 12px 2px 12px;
    padding: 0.7rem 1rem;
    margin: 0.4rem 0;
    font-size: 0.88rem;
    color: #cae8ff;
    text-align: right;
}
.chat-ai {
    background: #23863622;
    border: 1px solid #23863644;
    border-radius: 12px 12px 12px 2px;
    padding: 0.7rem 1rem;
    margin: 0.4rem 0;
    font-size: 0.88rem;
    color: #aff5b4;
    text-align: left;
}
.chat-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: #8b949e;
    margin-bottom: 2px;
}

/* ── stButton ── */
.stButton > button {
    background: linear-gradient(135deg, #238636, #2ea043) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.9rem !important;
    padding: 0.5rem 1.4rem !important;
    transition: opacity 0.2s !important;
}
.stButton > button:hover { opacity: 0.85 !important; }

/* ── inputs ── */
.stTextInput > div > div > input,
.stTextArea textarea,
.stSelectbox > div > div {
    background: #0d1117 !important;
    border: 1px solid #30363d !important;
    border-radius: 8px !important;
    color: #e6edf3 !important;
    font-family: 'Syne', sans-serif !important;
}
.stTextInput > div > div > input:focus,
.stTextArea textarea:focus {
    border-color: #3fb950 !important;
    box-shadow: 0 0 0 2px rgba(63,185,80,0.15) !important;
}

/* ── sidebar nav ── */
.nav-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 14px;
    border-radius: 8px;
    margin: 4px 0;
    cursor: pointer;
    color: #8b949e;
    font-size: 0.88rem;
    font-weight: 600;
    transition: all 0.2s;
}
.nav-item:hover, .nav-item.active {
    background: #21262d;
    color: #e6edf3;
}
.nav-dot { width: 8px; height: 8px; border-radius: 50%; background: #3fb950; }

/* ── spinner override ── */
.stSpinner > div { border-top-color: #3fb950 !important; }

/* ── metrics ── */
[data-testid="metric-container"] {
    background: #161b22;
    border: 1px solid #21262d;
    border-radius: 10px;
    padding: 0.8rem 1rem;
}
</style>
""", unsafe_allow_html=True)


# ── Sidebar ───────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding: 1rem 0 0.5rem 0;'>
        <div style='font-family: Syne, sans-serif; font-size: 1.1rem; font-weight: 800;
                    background: linear-gradient(90deg, #58a6ff, #3fb950);
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                    background-clip: text;'>
            ⛓️ LangChain Playground
        </div>
        <div style='color: #8b949e; font-size: 0.75rem; margin-top: 4px;'>
            Week 3 · ChatPromptTemplate
        </div>
    </div>
    <hr style='border-color: #21262d; margin: 0.8rem 0;'>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        [
            "🏠  Home",
            "📝  Ex 1 · First Template",
            "🌐  Ex 2 · Message Roles",
            "⛓️  Ex 3 · Chain + Model",
            "🤖  Ex 4 · Reusable Function",
            "💬  Ex 5 · Conversation History",
        ],
        label_visibility="collapsed"
    )

    st.markdown("<hr style='border-color: #21262d; margin: 1rem 0;'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='color: #8b949e; font-size: 0.75rem; line-height: 1.6; padding: 0 0.2rem;'>
        <b style='color: #e6edf3;'>API Key</b><br>
        Add your key to <code style='color: #3fb950;'>key.env</code><br><br>
        <b style='color: #e6edf3;'>Model</b><br>
        <code style='color: #58a6ff;'>gemini-2.5-flash</code><br><br>
        <b style='color: #e6edf3;'>Tutor</b><br>
        Selamo Allen
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════
#  HOME
# ═══════════════════════════════════════════════════════
if page == "🏠  Home":
    st.markdown("""
    <div class='hero-banner'>
        <p class='hero-title'>LangChain ChatPromptTemplate</p>
        <p class='hero-sub'>Generative AI Scholarship Program · Week 3 · Interactive Playground</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)
    cards = [
        ("📝", "Ex 1", "First Template", "#58a6ff"),
        ("🌐", "Ex 2", "Message Roles",  "#e3b341"),
        ("⛓️", "Ex 3", "Chain + Model",  "#3fb950"),
        ("🤖", "Ex 4", "Reusable Fn",    "#f78166"),
        ("💬", "Ex 5", "Chat History",   "#d2a8ff"),
    ]
    for col, (icon, num, label, color) in zip([col1, col2, col3, col4, col5], cards):
        with col:
            st.markdown(f"""
            <div class='ex-card' style='text-align:center; padding: 1.2rem 0.8rem;'>
                <div style='font-size: 1.8rem; margin-bottom: 0.4rem;'>{icon}</div>
                <div style='font-family: JetBrains Mono, monospace; font-size: 0.7rem;
                            color: {color}; font-weight: 700; margin-bottom: 4px;'>{num}</div>
                <div style='font-size: 0.82rem; color: #8b949e;'>{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='glow-divider'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='ex-card'>
        <p class='sec-title'>What is this?</p>
        <p class='sec-desc'>
            This playground lets you run all 5 Week 3 exercises interactively.
            Each exercise has its own page where you can enter inputs, run the code, and see live results.
            Exercises 1 and 2 work without an API key. Exercises 3, 4, and 5 call the
            <span style='color: #58a6ff; font-family: JetBrains Mono, monospace;'>gemini-2.5-flash</span> model
            and require your Google API key in <code style='color: #3fb950;'>key.env</code>.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════
#  EXERCISE 1
# ═══════════════════════════════════════════════════════
elif page == "📝  Ex 1 · First Template":
    st.markdown("""
    <div class='hero-banner'>
        <div class='badge'>EXERCISE 1</div>
        <p class='hero-title' style='font-size: 1.6rem;'>Your First ChatPromptTemplate</p>
        <p class='hero-sub'>Enter a topic and see how LangChain formats a beginner-friendly prompt — no API key needed.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='tip-box'>
        💡 This exercise only <b>formats</b> the prompt locally. No AI model is called.
    </div>
    """, unsafe_allow_html=True)

    topic = st.text_input("Topic", value="Artificial Intelligence", placeholder="e.g. Machine Learning, Python, APIs...")

    if st.button("Format Prompt", key="ex1"):
        from langchain_core.prompts import ChatPromptTemplate

        prompt = ChatPromptTemplate.from_template(
            "Explain {topic} as if I am a complete beginner."
        )
        messages = prompt.format_messages(topic=topic)

        st.markdown("<div class='glow-divider'></div>", unsafe_allow_html=True)
        st.markdown("""<div class='badge badge-green'>OUTPUT</div>""", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class='ex-card'>
                <div style='color: #8b949e; font-size: 0.75rem; font-family: JetBrains Mono, monospace;
                            margin-bottom: 0.5rem;'>FORMATTED MESSAGE OBJECT</div>
                <div class='output-box'>{str(messages)}</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class='ex-card'>
                <div style='color: #8b949e; font-size: 0.75rem; font-family: JetBrains Mono, monospace;
                            margin-bottom: 0.5rem;'>EXTRACTED TEXT</div>
                <div class='output-box'>{messages[0].content}</div>
                <div style='margin-top: 0.8rem;'>
                    <span style='background:#23863622; color:#3fb950; border:1px solid #23863644;
                                 border-radius:6px; padding: 2px 10px; font-size: 0.75rem;
                                 font-family: JetBrains Mono, monospace;'>
                        type: {type(messages[0]).__name__}
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════
#  EXERCISE 2
# ═══════════════════════════════════════════════════════
elif page == "🌐  Ex 2 · Message Roles":
    st.markdown("""
    <div class='hero-banner'>
        <div class='badge'>EXERCISE 2</div>
        <p class='hero-title' style='font-size: 1.6rem;'>System & Human Message Roles</p>
        <p class='hero-sub'>Use from_messages() with a system role and a human role to build a translator prompt.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='tip-box'>
        💡 This exercise only <b>formats</b> the prompt locally. No AI model is called.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        text = st.text_input("Text to translate", value="Good morning, how are you?")
    with col2:
        language = st.selectbox("Target language", ["French", "Cameroonian Pidgin English", "Spanish", "German", "Arabic", "Japanese"])

    if st.button("Format Prompt", key="ex2"):
        from langchain_core.prompts import ChatPromptTemplate

        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a professional translator."),
            ("human", "Translate this text into {language}: {text}")
        ])
        result = prompt.format_messages(text=text, language=language)

        st.markdown("<div class='glow-divider'></div>", unsafe_allow_html=True)
        st.markdown("""<div class='badge badge-green'>OUTPUT</div>""", unsafe_allow_html=True)

        for msg in result:
            role = type(msg).__name__
            color = "#58a6ff" if "System" in role else "#3fb950"
            bg    = "#1f6feb11" if "System" in role else "#23863611"
            border= "#1f6feb33" if "System" in role else "#23863633"
            st.markdown(f"""
            <div style='background:{bg}; border:1px solid {border}; border-radius:10px;
                        padding: 0.8rem 1.1rem; margin-bottom: 0.6rem;'>
                <div style='font-family: JetBrains Mono, monospace; font-size: 0.7rem;
                            color: {color}; font-weight: 700; margin-bottom: 6px;'>
                    {role.upper()}
                </div>
                <div style='font-size: 0.88rem; color: #e6edf3;'>{msg.content}</div>
            </div>
            """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════
#  EXERCISE 3
# ═══════════════════════════════════════════════════════
elif page == "⛓️  Ex 3 · Chain + Model":
    st.markdown("""
    <div class='hero-banner'>
        <div class='badge'>EXERCISE 3</div>
        <p class='hero-title' style='font-size: 1.6rem;'>Chaining a Prompt with a Model</p>
        <p class='hero-sub'>Build a full LangChain chain: Prompt → Gemini Model → StrOutputParser.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='tip-box tip-box-yellow'>
        ⚠️ This exercise calls the Gemini model. Make sure your <code>key.env</code> file is set up.
    </div>
    """, unsafe_allow_html=True)

    question = st.text_area(
        "Your question",
        value="What is a large language model in one paragraph?",
        height=80
    )

    if st.button("Run Chain", key="ex3"):
        try:
            from langchain_core.prompts import ChatPromptTemplate
            from langchain_google_genai import ChatGoogleGenerativeAI
            from langchain_core.output_parsers import StrOutputParser

            prompt  = ChatPromptTemplate.from_template("Answer this question: {question}")
            model   = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
            parser  = StrOutputParser()
            chain   = prompt | model | parser

            with st.spinner("Running chain..."):
                response = chain.invoke({"question": question})

            st.markdown("<div class='glow-divider'></div>", unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("""<div class='ex-card' style='text-align:center;'>
                    <div style='font-size:1.6rem;'>📝</div>
                    <div style='color:#58a6ff; font-size:0.75rem; font-weight:700;
                                font-family: JetBrains Mono, monospace; margin-top:4px;'>PROMPT</div>
                    <div style='color:#8b949e; font-size:0.75rem;'>Template formatted</div>
                </div>""", unsafe_allow_html=True)
            with col2:
                st.markdown("""<div class='ex-card' style='text-align:center;'>
                    <div style='font-size:1.6rem;'>🤖</div>
                    <div style='color:#e3b341; font-size:0.75rem; font-weight:700;
                                font-family: JetBrains Mono, monospace; margin-top:4px;'>MODEL</div>
                    <div style='color:#8b949e; font-size:0.75rem;'>gemini-2.5-flash</div>
                </div>""", unsafe_allow_html=True)
            with col3:
                st.markdown("""<div class='ex-card' style='text-align:center;'>
                    <div style='font-size:1.6rem;'>✅</div>
                    <div style='color:#3fb950; font-size:0.75rem; font-weight:700;
                                font-family: JetBrains Mono, monospace; margin-top:4px;'>PARSER</div>
                    <div style='color:#8b949e; font-size:0.75rem;'>StrOutputParser</div>
                </div>""", unsafe_allow_html=True)

            st.markdown("<div class='glow-divider'></div>", unsafe_allow_html=True)
            st.markdown("""<div class='badge badge-green'>RESPONSE</div>""", unsafe_allow_html=True)
            st.markdown(f"""<div class='output-box'>{response}</div>""", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")


# ═══════════════════════════════════════════════════════
#  EXERCISE 4
# ═══════════════════════════════════════════════════════
elif page == "🤖  Ex 4 · Reusable Function":
    st.markdown("""
    <div class='hero-banner'>
        <div class='badge'>EXERCISE 4</div>
        <p class='hero-title' style='font-size: 1.6rem;'>Reusable Prompt Function</p>
        <p class='hero-sub'>Call ask_ai(role, question) with any role and question — the AI adapts its persona.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='tip-box tip-box-yellow'>
        ⚠️ This exercise calls the Gemini model. Make sure your <code>key.env</code> file is set up.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### Add up to 3 role-question pairs")

    pairs = []
    preset_roles = ["doctor", "lawyer", "teacher", "scientist", "chef", "engineer", "historian", "custom..."]
    preset_questions = {
        "doctor":    "What are the symptoms of malaria?",
        "lawyer":    "What should I do if I sign a bad contract?",
        "teacher":   "How do I stay focused while studying?",
        "scientist": "How does photosynthesis work?",
        "chef":      "What is the secret to a perfect omelette?",
        "engineer":  "How does the internet actually work?",
        "historian": "What caused World War I?",
    }

    for i in range(3):
        with st.expander(f"Pair {i+1}", expanded=(i == 0)):
            c1, c2 = st.columns([1, 2])
            with c1:
                role_sel = st.selectbox(f"Role", preset_roles, key=f"role_sel_{i}")
                if role_sel == "custom...":
                    role = st.text_input("Custom role", key=f"role_custom_{i}", placeholder="e.g. astronaut")
                else:
                    role = role_sel
            with c2:
                default_q = preset_questions.get(role, "Ask me anything.")
                question  = st.text_input(f"Question", value=default_q, key=f"q_{i}")
            pairs.append((role, question))

    if st.button("Run All Pairs", key="ex4"):
        try:
            from langchain_core.prompts import ChatPromptTemplate
            from langchain_google_genai import ChatGoogleGenerativeAI
            from langchain_core.output_parsers import StrOutputParser

            model  = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
            parser = StrOutputParser()

            def ask_ai(role, question):
                prompt = ChatPromptTemplate.from_messages([
                    ("system", "You are a helpful {role}."),
                    ("human", "{question}")
                ])
                chain = prompt | model | parser
                return chain.invoke({"role": role, "question": question})

            st.markdown("<div class='glow-divider'></div>", unsafe_allow_html=True)
            colors = ["#58a6ff", "#3fb950", "#e3b341"]

            for idx, (role, question) in enumerate(pairs):
                if not role or not question:
                    continue
                with st.spinner(f"Asking the {role}..."):
                    response = ask_ai(role, question)

                st.markdown(f"""
                <div class='ex-card' style='border-left: 3px solid {colors[idx % 3]};'>
                    <div style='display:flex; align-items:center; gap:10px; margin-bottom:0.7rem;'>
                        <span style='background:{colors[idx % 3]}22; color:{colors[idx % 3]};
                                     border:1px solid {colors[idx % 3]}44; border-radius:20px;
                                     padding: 2px 12px; font-size:0.75rem; font-weight:700;
                                     font-family: JetBrains Mono, monospace;'>
                            {role.upper()}
                        </span>
                        <span style='color:#8b949e; font-size:0.82rem;'>{question}</span>
                    </div>
                    <div class='output-box' style='border-left-color:{colors[idx % 3]};
                                                   color: #e6edf3;'>{response}</div>
                </div>
                """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")


# ═══════════════════════════════════════════════════════
#  EXERCISE 5
# ═══════════════════════════════════════════════════════
elif page == "💬  Ex 5 · Conversation History":
    st.markdown("""
    <div class='hero-banner'>
        <div class='badge'>EXERCISE 5</div>
        <p class='hero-title' style='font-size: 1.6rem;'>Multi-Turn Conversation History</p>
        <p class='hero-sub'>Chat with an AI study assistant that remembers the whole conversation using MessagesPlaceholder.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='tip-box tip-box-yellow'>
        ⚠️ This exercise calls the Gemini model. Make sure your <code>key.env</code> file is set up.
    </div>
    """, unsafe_allow_html=True)

    # session state for history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "raw_history" not in st.session_state:
        st.session_state.raw_history  = []

    # display chat
    if st.session_state.chat_history:
        st.markdown("#### Conversation")
        for entry in st.session_state.chat_history:
            if entry["role"] == "human":
                st.markdown(f"""
                <div style='text-align:right; margin: 0.3rem 0;'>
                    <div class='chat-label' style='text-align:right;'>YOU</div>
                    <div class='chat-human'>{entry["content"]}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style='text-align:left; margin: 0.3rem 0;'>
                    <div class='chat-label'>STUDY ASSISTANT</div>
                    <div class='chat-ai'>{entry["content"]}</div>
                </div>
                """, unsafe_allow_html=True)
        st.markdown("<div class='glow-divider'></div>", unsafe_allow_html=True)

    # input
    col1, col2 = st.columns([4, 1])
    with col1:
        user_input = st.text_input(
            "Your message",
            placeholder="Ask the study assistant anything...",
            label_visibility="collapsed",
            key="chat_input"
        )
    with col2:
        send = st.button("Send →", key="ex5_send")

    col3, col4 = st.columns([1, 4])
    with col3:
        if st.button("🗑️ Clear Chat", key="ex5_clear"):
            st.session_state.chat_history = []
            st.session_state.raw_history  = []
            st.rerun()

    if send and user_input:
        try:
            from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
            from langchain_google_genai import ChatGoogleGenerativeAI
            from langchain_core.output_parsers import StrOutputParser
            from langchain_core.messages import HumanMessage, AIMessage

            model  = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
            parser = StrOutputParser()

            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a helpful study assistant."),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{input}")
            ])
            chain = prompt | model | parser

            with st.spinner("Thinking..."):
                response = chain.invoke({
                    "history": st.session_state.raw_history,
                    "input": user_input
                })

            # update histories
            st.session_state.chat_history.append({"role": "human",  "content": user_input})
            st.session_state.chat_history.append({"role": "ai",     "content": response})
            st.session_state.raw_history.append(HumanMessage(content=user_input))
            st.session_state.raw_history.append(AIMessage(content=response))

            st.rerun()

        except Exception as e:
            st.error(f"Error: {e}")

    if not st.session_state.chat_history:
        st.markdown("""
        <div style='text-align:center; padding: 2rem; color: #8b949e;'>
            <div style='font-size: 2rem; margin-bottom: 0.5rem;'>💬</div>
            <div style='font-size: 0.9rem;'>Start a conversation — the assistant remembers everything you say.</div>
            <div style='font-size: 0.78rem; margin-top: 0.3rem; color: #484f58;'>
                Try: "What is Python?" then follow up with "What can I build with it?"
            </div>
        </div>
        """, unsafe_allow_html=True)

    # turn counter
    if st.session_state.chat_history:
        turns = len(st.session_state.chat_history) // 2
        st.markdown(f"""
        <div style='text-align:right; margin-top:0.5rem;'>
            <span style='background:#21262d; color:#8b949e; border-radius:20px;
                         padding: 2px 10px; font-size:0.72rem;
                         font-family: JetBrains Mono, monospace;'>
                {turns} turn{"s" if turns != 1 else ""} · {len(st.session_state.raw_history)} messages in history
            </span>
        </div>
        """, unsafe_allow_html=True)