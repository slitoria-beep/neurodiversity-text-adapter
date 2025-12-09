import streamlit as st

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="AI Accessibility Adapter",
    page_icon="✨",
    layout="centered"
)

# ---------------------- GLOBAL FONT STYLE ----------------------
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;500;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Open Sans', sans-serif !important;
            letter-spacing: 1px;
        }

        /* ✅ Soft Blue Background */
        .main {
            background-color: #EAF3FF !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------- TOP BANNER ----------------------
st.markdown("""
<div style='background-color:#DCEBFF; padding: 25px; border-radius: 10px; margin-bottom: 20px;'>
    <h1 style='text-align:center; color:#2A6DB0; margin:0; font-weight:700;'>
        Welcome to our AI Capstone Project
    </h1>
    <p style='text-align:center; color:#555; margin-top:8px; font-size:16px;'>
        AI Accessibility Adapter — CBSE AI Capstone Project, DPSBE
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------- SIDEBAR NAVIGATION ----------------------
st.sidebar.title("📌 Navigation")
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

page = st.sidebar.radio("Go to:", ["Home", "About Us", "Text Adapter"])

# ---------------------- HOME PAGE ----------------------
if page == "Home":
    st.markdown("""
        <div style='background-color:#E2F7E1; padding: 30px; border-radius: 15px; margin-bottom: 20px;'>
            <h1 style='text-align: center; color: #2A6DB0; margin-bottom: 5px;'>
                Welcome to our AI Capstone Project
            </h1>
            <p style='text-align: center; font-size: 18px; color: #3A3A3A;'>
                A calm, comfortable space designed for neurodiverse learners
            </p>
        </div>

        <div style='background-color: #DFF5D8; padding: 25px; border-radius: 15px;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.05);'>
            <h3 style='color:#2A6DB0; margin-bottom:10px;'>👥 Team Members</h3>
            <p style='font-size: 17px; color:#333; line-height:1.6;'>
                Swasti<br>
                Mritika<br>
                Deepshikha<br>
                Madhav<br>
            </p>
        </div>
    """, unsafe_allow_html=True)

# ---------------------- ABOUT US PAGE ----------------------
elif page == "About Us":
    st.markdown("""
        <div style='background-color:#E2F7E1; padding: 30px; border-radius: 15px; margin-bottom: 20px;'>
            <h1 style='text-align: center; color: #2A6DB0;'>
                About Us
            </h1>
        </div>

        <div style='background-color:#DFF5D8; padding: 25px; border-radius: 15px;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.05);'>
            <p style='font-size: 17px; color:#333; text-align: justify;'>
                We are a student team from DPSBE working on an AI-powered accessibility tool 
                for neurodiverse learners. Our goal is to make school content easier 
                to read, understand, and engage with for students with ADHD, Dyslexia, 
                and Autism.
                <br><br>
                This project is part of our CBSE AI Capstone initiative, where we aim 
                to use artificial intelligence to solve real-world educational challenges.
            </p>

            <h3 style='color:#2A6DB0;'>Our Mission</h3>
            <p style='font-size: 17px; color:#333;'>
                To build inclusive, accessible, and supportive learning tools for every student.
            </p>
        </div>
    """, unsafe_allow_html=True)

# ---------------------- TEXT ADAPTER PAGE ----------------------
elif page == "Text Adapter":

    st.title("AI Accessibility Adapter for Neurodiverse Students")

    text = st.text_area("Enter your school text here:")

    profile = st.selectbox("Choose a profile:", ["ADHD", "Dyslexia", "Autism"])

    if st.button("Adapt Text"):

        # -----------------------------
        # ✅ ADHD MODE (UNCHANGED)
        # -----------------------------
        if profile == "ADHD":
            import re

            sentences = re.split(r'(?<=[.!?]) +', text)

            chunks = []
            chunk = []

            for s in sentences:
                if len(chunk) < 3:
                    chunk.append(s)
                else:
                    chunks.append(chunk)
                    chunk = [s]
            if chunk:
                chunks.append(chunk)

            final_output = ""

            for i, ch in enumerate(chunks, start=1):

                final_output += f"### Idea {i}\n\n"

                topic = ch[0].strip()
                final_output += f"**{topic}**\n\n"

                for s in ch[1:]:
                    s = s.strip()

                    s = re.sub(
                        r'\b(run|make|create|explain|show|write|analyze|compare|identify|describe|solve|use|build|apply|observe|record|calculate|demonstrate|investigate|summarize)\b',
                        r'**\1**',
                        s,
                        flags=re.IGNORECASE
                    )

                    final_output += f"- {s}\n"

                final_output += "\n"
                final_output += "**Try this:** Turn this idea into a short activity, diagram, or quick discussion.\n\n"
                final_output += f"**Summary:** {topic}\n\n"
                final_output += "---\n\n"

            st.markdown(
                f"""
                <div style='background-color:#DFF5D8; padding:20px; border-radius:12px;'>
                    {final_output}
                </div>
                """,
                unsafe_allow_html=True
            )

        # -----------------------------
        # ✅ DYSLEXIA MODE (UNCHANGED)
        # -----------------------------
        elif profile == "Dyslexia":
            import re

            sentences = re.split(r'(?<=[.!?]) +', text)

            def break_long_words(word):
                return re.sub(r'(\w{6})(\w+)', r'\1&shy;\2', word)

            processed_sentences = []
            for s in sentences:
                words = s.split()
                broken_words = [break_long_words(w) for w in words]
                processed_sentences.append(" ".join(broken_words))

            adapted = "<br><br>".join(processed_sentences)

            st.markdown(
                f"""
                <div style='background-color:#DFF5D8; padding:20px; border-radius:12px;'>
                    {adapted}
                </div>
                """,
                unsafe_allow_html=True
            )

        # -----------------------------
        # ✅ AUTISM MODE (UNCHANGED)
        # -----------------------------
        elif profile == "Autism":
            import re

            sentences = re.split(r'(?<=[.!?]) +', text.strip())

            chunks = []
            chunk = []
            for s in sentences:
                s = s.strip()
                if not s:
                    continue
                if len(chunk) < 3:
                    chunk.append(s)
                else:
                    chunks.append(chunk)
                    chunk = [s]
            if chunk:
                chunks.append(chunk)

            final_output = "## Autism-friendly version\n\n"
            final_output += "**What this section explains:** The text is broken into small, clear parts with one idea in each part.\n\n"

            for i, ch in enumerate(chunks, start=1):
                final_output += f"### Part {i}\n\n"
                main_idea = ch[0]
                final_output += "**Main idea:** " + main_idea + "\n\n"

                if len(ch) > 1:
                    final_output += "**Details:**\n"
                    for s in ch[1:]:
                        final_output += f"- {s}\n"
                    final_output += "\n"

                final_output += "**Example task:** Write one simple sentence that explains this part in your own words.\n\n"
                final_output += "---\n\n"

            st.markdown(
                f"""
                <div style='background-color:#DFF5D8; padding:20px; border-radius:12px;'>
                    {final_output}
                </div>
                """,
                unsafe_allow_html=True
            )

# ---------------------- FOOTER ----------------------
st.markdown("""
<hr>
<p style='text-align:center; color: grey;'>
CBSE AI Capstone Project — DPSBE
</p>
""", unsafe_allow_html=True)
