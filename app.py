import streamlit as st
from ai_engine import AIBuddy
from audio_processor import transcribe_lecture
from PyPDF2 import PdfReader
import os
from dotenv import load_dotenv

load_dotenv(override=True)
HF_TOKEN = os.getenv('HF_TOKEN')

st.set_page_config(page_icon='🎓', page_title = 'LearnitAI')

st.title("🎓 LearnitAI: Your Personal AI Study Buddy")

if not HF_TOKEN:
    st.error("API Token not found! Please ensure your .env file contains HF_TOKEN.")


else:

    ai = AIBuddy(HF_TOKEN)

    tab1, tab2, tab3 = st.tabs(["PDF Notes", "Lecture Audio","General Query"])

    with tab1:
        st.header("📄 Simplify Your Notes")

        pdf_file = st.file_uploader("Upload Your PDF Notes", type='pdf')


        if pdf_file is not None:
            try:
                reader = PdfReader(pdf_file)

                raw_text = "".join([page.extract_text() for page in reader.pages])

                task = st.selectbox("What should LearnitAI do?",["Summarize","Simplify","Quiz"])

                if st.button("Proceed", key="pdf_btn"):
                    with st.spinner("LearnitAI is Thinking"):
                        result = ai.process_request(raw_text, task)
                        st.markdown(f"### {task} result:")
                        st.write(result)
            except Exception as e:
                st.error("Upload Failed. Error: {e}")

        with tab2:
            st.header("🎙️ Summarize Recorded Lectures")

            audio_file = st.file_uploader("Upload Lecture Audio", type=['mp3','wav','aac','m4a'])


            if st.button("Proceed", key="aud_btn"):
                try :
                    with st.spinner("LearnitAI is Thinking"):
                        with open("temp_rec.mp3","wb") as f:
                            f.write(audio_file.read())
                        
                        transcript = transcribe_lecture("temp_rec.mp3")
                        st.success("Transcription Complete!")

                        with st.spinner("Preparing Notes"):
                            summary = ai.process_request(transcript, "Summarize")
                            st.markdown("### 📝 Lecture Study Notes:")
                            st.write(summary) 
                    
                        os.remove("temp_rec.mp3")

                except Exception as e:
                    st.error("Upload Failed. Error: {e}")
        
        with tab3:
            st.header("💬 Ask Your AI Tutor")
    
            if "messages" not in st.session_state:
                st.session_state.messages = []

            chat_container = st.container()

            with chat_container:
                for message in st.session_state.messages:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])

            if prompt := st.chat_input("Explain the difference between TCP and UDP..."):
                
                with chat_container:
                    st.chat_message("user").markdown(prompt)
                st.session_state.messages.append({"role": "user", "content": prompt})

                with st.spinner("LearnitAI is thinking..."):
                    response = ai.process_request(prompt, "Chat")
                    
                    with chat_container:
                        with st.chat_message("assistant"):
                            st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})        


