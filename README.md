# Agentic-Based-APP-Generator-
AI-powered App/Game Generator using Streamlit + N8N Agents. Enter an idea and instantly generate and launch a working Streamlit app or Python game. Includes real-time code generation, automatic detection, and execution support. Built during Agentic AI Internship at Innomatics.

**Built using Streamlit + N8N + Agentic AI**  
Created during my **Agentic AI Internship at Innomatics Research Labs**

---

## 📌 Project Overview  
This project is an **AI-driven App/Game Generator** that allows users to simply describe an idea (e.g., *“create a calculator app”* or *“build a snake game”*) and instantly generate a fully working **Streamlit application or Python game file**.

It integrates **Streamlit**, **Python**, and **N8N AI Agents** to automatically:
1. Process the user prompt  
2. Generate complete functional code  
3. Save it into a Python file  
4. Launch it in real-time as an app or game  

💡 The system detects whether the generated code is a **Streamlit app** or a **normal Python game**, and launches it accordingly.

---

## ✨ Features  
- 🧠 **AI-powered code generation** using N8N agent  
- ⚡ **Real-time app/game execution**  
- 🔍 **Automatic detection** between Streamlit app & Python game  
- 📂 Saves generated code into `app1.py`  
- 🎮 Works with games (Pygame, Tkinter, etc.)  
- 🌐 Works with Streamlit web apps  
- 🔄 Clean UI built using Streamlit  
- 📡 Uses N8N webhook for prompt processing  

---

## 📁 Folder Structure  
project-folder/
│── app.py # Main Streamlit UI
│── app1.py # Auto-generated app/game file
│── README.md # Project documentation
│── n8n_workflow.json 
