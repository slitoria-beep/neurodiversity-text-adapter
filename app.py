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
    </style>
""", unsafe_allow_html=True)

# ---------------------- SIDEBAR NAVIGATION ----------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to:", ["Home", "About Us", "Text Adapter"])

# ---------------------- HOME PAGE ----------------------
if page == "Home":
    st.markdown("""
        <h1 style='text-align: center; color: #2A6DB0; margin-bottom: -10px;'>
            Welcome to Our AI Capstone Project
        </h1>
        <p style='text-align: center; font-size: 18px; color: #555;'>
            Supporting neurodiverse learners with ADHD, Dyslexia, and Autism
        </p>
        <br>
        <div style='background-color: #F5F9FF; padding: 20px; border-radius: 12px;'>
            <h3 style='color:#2A6DB0;'>👥 Team Members</h3>
            <p style='font-size: 17px; color:#333;'>
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
        <h1 style='text-align: center; color: #2A6DB0;'>
            About Us
        </h1>
        <p style='font-size: 17px; color:#333; text-align: justify;'>
            We are a student team from DPS Bangalore East working on an AI-powered accessibility tool 
            for neurodiverse learners. Our goal is to make school content easier 
            to read, understand, and engage with for students with ADHD, Dyslexia, 
            and Autism.
            <br><br>
            This project is part of our CBSE AI Capstone initiative, where we aim 
            to use artificial intelligence to solve real-world educational challenges.
        </p>
        <br>
        <div style='background-color: #F5F9FF; padding: 20px; border-radius: 12px;'>
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

            st.markdown(final_output)

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
                <div id="dyslexiaText" style="
                    font-family: 'Lexend', sans-serif;
                    font-size: 22px;
                    line-height: 1.9;
                    letter-spacing: 0.8px;
                    text-align: left;
                    color: #222;
                    background-color: #f5f5f5;
                    padding: 22px;
                    border-radius: 10px;
                    border-left: 8px solid #4a90e2;
                    margin-top: 15px;
                ">
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
                <div style="
                    font-family: 'Open Sans', sans-serif;
                    font-size: 18px;
                    line-height: 1.7;
                    letter-spacing: 0.4px;
                    text-align: left;
                    color: #202124;
                    background-color: #f8f9fa;
                    padding: 18px;
                    border-radius: 8px;
                    border: 1px solid #e0e0e0;
                ">
                    {final_output}
                </div>
                """,
                unsafe_allow_html=True
            )

# ---------------------- FOOTER ----------------------
st.markdown("""
<hr>
<p style='text-align:center; color: grey;'>
Built by Swasti, Mritika, Deepshikha, Madhav of DPSBE — CBSE AI Capstone Project
</p>
""", unsafe_allow_html=True)
