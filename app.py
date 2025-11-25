import streamlit as st
import requests
import subprocess
import os
import sys
import time

st.title("AI-Powered App/Game Generator")

prompt = st.text_area("Describe the app or game you want:", height=150)

generate_app = st.button("Generate App")
generate_game = st.button("Generate Game")

# ========== GENERATE CODE FROM N8N/AI AGENT ==========
if generate_app or generate_game:
    mode = "app" if generate_app else "game"

    st.info("Generating your " + mode + "… Please wait.")

    response = requests.post(
        url="https://prakharnew.app.n8n.cloud/webhook-test/fcc82c90-340e-44a4-a74e-4b808edba4c1",
        json={"prompt": prompt, "mode": mode}
    )

    if response.status_code == 200:
        code_text = response.json()['output']

        clean_code = (
            code_text.replace("```python", "")
                     .replace("```", "")
                     .strip()
        )

        with open("app1.py", "w", encoding="utf-8") as f:
            f.write(clean_code)

        st.success("Code generated successfully!")
        st.code(clean_code, language="python")

    else:
        st.error("❌ Failed to get response from N8N webhook.")

# ========== RUN THE GENERATED APP/GAME ==========
if os.path.exists("app1.py"):
    if st.button("Launch Generated App/Game"):

        with open("app1.py", "r", encoding="utf-8") as f:
            file_data = f.read()

        # ----------------------------
        #     LAUNCH PROGRESS UI
        # ----------------------------
        with st.spinner("Launching the app… 🔄\nThis usually takes 5–10 seconds…"):
            time.sleep(1)

            # Detect Streamlit or normal Python game/app
            if "streamlit" in file_data.lower():
                launch_type = "Streamlit App"
                st.info("Detected: Streamlit App 🚀\nOpening in browser…")
                process = subprocess.Popen(
                    [sys.executable, "-m", "streamlit", "run", "app1.py"],
                    shell=True
                )
            else:
                launch_type = "Python Game"
                st.info("Detected: Python Game 🎮\nLaunching window…")
                process = subprocess.Popen(
                    [sys.executable, "app1.py"],
                    shell=True
                )

            time.sleep(2)

        st.success(f"✅ {launch_type} Launched Successfully!")

        st.info("If nothing opens:\n\n- Wait 5 more seconds\n- Check taskbar for a running app/game\n- Check terminal output")










