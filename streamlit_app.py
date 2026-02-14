import streamlit as st
from datetime import datetime

# ------------------------
# PAGE CONFIG
# ------------------------
st.set_page_config(
    page_title="KGL AI",
    page_icon="🤖",
    layout="wide"
)

# ------------------------
# DARK MODE TOGGLE
# ------------------------
dark_mode = st.sidebar.toggle("🌙 Dark Mode")

if dark_mode:
    st.markdown("""
        <style>
        body { background-color: #0e1117; color: white; }
        </style>
    """, unsafe_allow_html=True)

# ------------------------
# SIDEBAR NAVIGATION
# ------------------------
st.sidebar.title("KGL AI Navigation")

page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "🚀 Projects", "🏥 Healthcare AI", "💼 Careers", "📩 Contact"]
)

# ------------------------
# SESSION ANALYTICS
# ------------------------
if "visits" not in st.session_state:
    st.session_state.visits = 1
else:
    st.session_state.visits += 1

# ------------------------
# HOME PAGE
# ------------------------
if page == "🏠 Home":
    st.title("🤖 KGL AI – Africa’s AI Innovation Hub")
    st.write("Innovate. Collaborate. Impact.")

    col1, col2, col3 = st.columns(3)
    col1.metric("👥 Visitors (Session)", st.session_state.visits)
    col2.metric("👨‍💻 Contributors", "50+")
    col3.metric("🚀 Projects", "12+")

    st.markdown("---")

    st.subheader("🌍 About Us")
    st.write("""
    KGL AI is a community-driven platform connecting AI developers,
    researchers, and innovators to build impactful solutions in healthcare,
    education, and technology across Africa.
    """)

# ------------------------
# PROJECTS PAGE
# ------------------------
elif page == "🚀 Projects":
    st.title("🚀 AI Projects")

    projects = [
        "Healthcare Diagnostic Assistant",
        "AI Game Recommendation Engine",
        "Multilingual Chatbot (English + Kinyarwanda)",
        "Risk Assessment Flow System",
        "AI Analytics Dashboard"
    ]

    for project in projects:
        st.card = st.container()
        with st.card:
            st.subheader(project)
            st.write("Project description goes here.")
            st.button("View Project")

# ------------------------
# HEALTHCARE AI PAGE
# ------------------------
elif page == "🏥 Healthcare AI":
    st.title("🏥 Healthcare AI Diagnostic Tool")

    st.write("Select symptoms below:")

    fever = st.checkbox("Fever")
    headache = st.checkbox("Headache")
    vomiting = st.checkbox("Vomiting")
    abdominal_pain = st.checkbox("Abdominal Pain")
    fatigue = st.checkbox("Fatigue")

    if st.button("Analyze"):
        if fever and headache:
            st.error("🚨 Risk Level: Medium to High")
            st.write("Possible Condition: Malaria")
            st.write("Recommended Action: Visit nearest health center for testing.")
            st.write("Confidence: 75%")
        elif abdominal_pain and vomiting:
            st.warning("⚠ Risk Level: Medium")
            st.write("Possible Condition: Gastroenteritis")
            st.write("Recommended Action: Hydration & medical check if persistent.")
            st.write("Confidence: 65%")
        else:
            st.success("🟢 Risk Level: Low")
            st.write("Monitor symptoms and consult doctor if they persist.")
            st.write("Confidence: 50%")

    st.info("⚠ Disclaimer: This tool does NOT replace professional medical advice.")

# ------------------------
# CAREERS PAGE
# ------------------------
elif page == "💼 Careers":
    st.title("💼 Join KGL AI")

    st.write("We are building Africa’s AI innovation community.")

    st.subheader("Open Positions")
    st.write("""
    - HR Generalist Intern
    - Marketing & Social Media Intern
    - AI/ML Engineer
    - Frontend Developer
    """)

    st.success("""
    🌍 We are an equal opportunity platform.
    We DO NOT charge any application or recruitment fees.
    Everyone is welcome at KGL AI.
    """)

# ------------------------
# CONTACT PAGE
# ------------------------
elif page == "📩 Contact":
    st.title("📩 Contact Us")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send"):
        st.success("Thank you for contacting KGL AI!")

    st.write("Email: info@kgl.ai")
    st.write("GitHub: https://github.com/yourrepo")

# ------------------------
# FOOTER
# ------------------------
st.markdown("---")
st.markdown(
    f"© {datetime.now().year} KGL AI · Open · Africa-First · Community-Driven"
)
