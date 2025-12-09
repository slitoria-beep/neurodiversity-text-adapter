import streamlit as st

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;500;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Open Sans', sans-serif !important;
            letter-spacing: 1px;  /* adjust spacing here */
        }
    </style>
""", unsafe_allow_html=True)



st.title("AI Accessibility Adapter for Neurodiverse Students")

text = st.text_area("Enter your school text here:")

profile = st.selectbox("Choose a profile:", ["ADHD", "Dyslexia", "Autism"])

if st.button("Adapt Text"):

    # -----------------------------
    # ✅ ADHD MODE
    # -----------------------------
    if profile == "ADHD":
        import re

        # Split text into sentences
        sentences = re.split(r'(?<=[.!?]) +', text)

        chunks = []
        chunk = []

        # Group into 2–4 sentence chunks
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

            # Mini‑heading
            final_output += f"### Idea {i}\n\n"

            # Topic sentence (bold)
            topic = ch[0].strip()
            final_output += f"**{topic}**\n\n"

            # Bullet points for supporting sentences
            for s in ch[1:]:
                s = s.strip()

                # Highlight action verbs
                s = re.sub(
                    r'\b(run|make|create|explain|show|write|analyze|compare|identify|describe|solve|use|build|apply|observe|record|calculate|demonstrate|investigate|summarize)\b',
                    r'**\1**',
                    s,
                    flags=re.IGNORECASE
                )

                final_output += f"- {s}\n"

            final_output += "\n"

            # Try this (bold)
            final_output += "**Try this:** Turn this idea into a short activity, diagram, or quick discussion.\n\n"

            # Summary (bold)
            final_output += f"**Summary:** {topic}\n\n"

            # Divider
            final_output += "---\n\n"

        st.markdown(final_output)

    # -----------------------------
    # ✅ DYSLEXIA MODE + TTS
    # -----------------------------
    elif profile == "Dyslexia":
        import re

        # Split into shorter, clearer sentences
        sentences = re.split(r'(?<=[.!?]) +', text)

        # Break long words using soft hyphens
        def break_long_words(word):
            return re.sub(r'(\w{6})(\w+)', r'\1&shy;\2', word)

        processed_sentences = []
        for s in sentences:
            words = s.split()
            broken_words = [break_long_words(w) for w in words]
            processed_sentences.append(" ".join(broken_words))

        # Join with extra spacing between sentences
        adapted = "<br><br>".join(processed_sentences)

        # ✅ Dyslexia‑friendly styled text container
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
    elif profile == "Autism":
        import re

        # 1. Split into sentences
        sentences = re.split(r'(?<=[.!?]) +', text.strip())

        # 2. Group sentences into small logical chunks (2–3 sentences each)
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

        # 3. Build structured, predictable output
        final_output = "## Autism-friendly version\n\n"
        final_output += "**What this section explains:** The text is broken into small, clear parts with one idea in each part.\n\n"

        for i, ch in enumerate(chunks, start=1):
            # Subheading for each chunk
            final_output += f"### Part {i}\n\n"

            # First sentence as main idea
            main_idea = ch[0]

            final_output += "**Main idea:** " + main_idea + "\n\n"

            # Remaining sentences as clear bullet points
            if len(ch) > 1:
                final_output += "**Details:**\n"
                for s in ch[1:]:
                    final_output += f"- {s}\n"
                final_output += "\n"

            # Simple example prompt (not metaphorical)
            final_output += "**Example task:** Write one simple sentence that explains this part in your own words.\n\n"

            # Separator
            final_output += "---\n\n"

        # Calm, minimal styling
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

    # -----------------------------
    # ✅ FALLBACK
    # -----------------------------
    else:
        st.write("Adaptation for this profile is coming soon.")
