# import streamlit as st
# import base64

# # from pyngrok import ngrok
# # run_tts
# from chatbot import ask, run_stt, run_tts
# from audio_recorder_streamlit import audio_recorder
# from streamlit_float import *
# import logging
# import time
# import os

# logging.basicConfig(
#     level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
# )

# # Float feature initialization
# float_init()

# # Create footer container and add content
# footer_container = st.container()

# # Streamlit UI
# st.title("VNU-IS Virtual Assistant")


# # c = st.container()
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# prompt = st.chat_input(placeholder="Mời bạn nhập câu hỏi...")
# text_from_audio = None
# # -----Set footer--------------------

# if prompt is not None and prompt != "":
#     with st.chat_message("user"):
#         st.markdown(prompt)
#     st.session_state.messages.append({"role": "user", "content": prompt})

#     with st.chat_message("assistant"):
#         response = st.write_stream(ask(query=prompt))
#         logging.info(response)
#         logging.info("Gen normal text")

#     st.session_state.messages.append({"role": "assistant", "content": response})

# with footer_container:
#     # prompt = st.chat_input(placeholder="Mời bạn nhập câu hỏi...")
#     audio_bytes = audio_recorder(
#         text="",
#         icon_size="1x",
#         neutral_color="#a3a8b8",
#         recording_color="#de1212",
#     )
#     if audio_bytes is not None:
#         text_from_audio = run_stt(audio_bytes)
#         print("Done run STT")
#         audio_bytes = None

# if text_from_audio is not None and text_from_audio != "":
#     with st.chat_message("user"):
#         st.markdown(text_from_audio)
#     st.session_state.messages.append({"role": "user", "content": text_from_audio})

#     with st.chat_message("assistant"):
#         response = st.write_stream(ask(query=text_from_audio))
#         logging.info(response)

#     st.session_state.messages.append({"role": "assistant", "content": response})

#     text_from_audio = None

# if len(st.session_state.messages) >= 1:
#     if st.button("📢 Play Audio"):
#         logging.info("Button clicked: Play Audio")

#         # Retrieve the last "assistant" response from the session state
#         last_assistant_message = None
#         for message in reversed(st.session_state.messages):
#             if message["role"] == "assistant":
#                 last_assistant_message = message["content"]
#                 break

#         if last_assistant_message:
#             try:
#                 audio_base64 = run_tts(text=last_assistant_message, lang="vi")
#                 logging.info("TTS generation completed")

#                 if audio_base64:
#                     # Decode the audio from base64
#                     audio_bytes = base64.b64decode(audio_base64)
#                     logging.info(f"Audio bytes length: {len(audio_bytes)}")

#                     # Play the audio using st.audio and specify the correct format
#                     st.audio(audio_bytes, format="audio/wav", autoplay=True)
#                     # else:
#                     #     st.error("Failed to generate valid audio data.")
#                 else:
#                     st.error("Failed to generate audio.")
#             except Exception as e:
#                 logging.error(f"Error during TTS or audio playback: {e}")
#                 st.error(f"Error processing audio: {e}")
#         else:
#             st.error("No response available to generate audio.")
# footer_container.float(
#     "position: fixed;bottom: 100px;right: -95px;background-color: white;padding-top: 0px"
# )import streamlit as st

# -----------------------------------------------------------------------------------------------------------
# import base64

# # from pyngrok import ngrok
# # run_tts
# from chatbot import ask, run_stt, run_tts
# from audio_recorder_streamlit import audio_recorder
# from streamlit_float import *
# import logging
# import time
# import os

# logging.basicConfig(
#     level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
# )
# # Float feature initialization
# # float_init()


# # Create footer container and add content
# # footer_container = st.container()


# # Streamlit UI
# st.title("VNU-IS Virtual Assistant")

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# text_from_audio = None

# audio_bytes = st.audio_input("Record a voice message", label_visibility="hidden")
# if audio_bytes is not None:
#     # Check if TTS is running
#     try:
#         text_from_audio = run_stt(audio_bytes)
#         print("Done run STT")
#         audio_bytes = None
#     except Exception as e:
#         logging.error(f"Error during STT: {e}")
# #     st.session_state.messages.append({"role": "assistant", "content": response})
# prompt = st.chat_input(placeholder="Mời bạn nhập câu hỏi...")
# if (prompt and prompt.strip()) or (text_from_audio and text_from_audio.strip()):
#     # Prioritize `text_from_audio` if available
#     if text_from_audio and text_from_audio.strip():
#         prompt = text_from_audio
#         text_from_audio = None

#     # Display user's message
#     with st.chat_message("user"):
#         st.markdown(prompt)
#     st.session_state.messages.append({"role": "user", "content": prompt})

#     # Assistant's response
#     with st.chat_message("assistant"):
#         logging.info("Generating response to user input...")
#         response = st.write_stream(
#             ask(query=prompt)
#         )  # Assuming `ask()` returns a response string
#         logging.info(f"Response generated: {response}")

#     st.session_state.messages.append({"role": "assistant", "content": response})
#     prompt = ""


# if len(st.session_state.messages) >= 1:
#     if st.button(" Play Audio"):
#         logging.info("Button clicked: Play Audio")

#         # Retrieve the last "assistant" response from the session state
#         last_assistant_message = None
#         for message in reversed(st.session_state.messages):
#             if message["role"] == "assistant":
#                 last_assistant_message = message["content"]
#                 break

#         if last_assistant_message:
#             try:
#                 audio_base64 = run_tts(text=last_assistant_message, lang="vi")
#                 logging.info("TTS generation completed")

#                 if audio_base64:
#                     # Decode the audio from base64
#                     audio_bytes = base64.b64decode(audio_base64)
#                     logging.info(f"Audio bytes length: {len(audio_bytes)}")

#                     # Play the audio using st.audio and specify the correct format
#                     st.audio(audio_bytes, format="audio/wav", autoplay=True)
#                 else:
#                     st.error("Failed to generate audio.")
#             except Exception as e:
#                 logging.error(f"Error during TTS or audio playback: {e}")
#                 st.error(f"Error processing audio: {e}")
#         else:
#             st.error("No response available to generate audio.")


# -------------------------------------------------------------------------------------------------
import base64
from chatbot import ask, run_stt, run_tts
from audio_recorder_streamlit import audio_recorder
from streamlit_float import *
import logging
import time
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
st.set_page_config(page_title="VNU-IS Virtual Assistant", page_icon="🤖")

# Float feature initialization
float_init()

chat_container = st.container(height=760, border=False)

# Create footer container and add content
footer_container = st.container()
# Streamlit UI

# Initialize session state for messages, audio input, and audio playback
if "messages" not in st.session_state:
    st.session_state.messages = []
if "audio_input_active" not in st.session_state:
    st.session_state.audio_input_active = False
if "audio_playback_active" not in st.session_state:
    st.session_state.audio_playback_active = False
if "text_from_audio_active" not in st.session_state:
    st.session_state.text_from_audio_active = False
if "gen_answer_active" not in st.session_state:
    st.session_state.gen_answer_active = False
if "previous_audio_bytes" not in st.session_state:
    st.session_state.previous_audio_bytes = None
# Display previous chat messages


text_from_audio = None
prompt = st.chat_input(placeholder="Mời bạn nhập câu hỏi...")

with footer_container:
    audio_bytes = st.audio_input("Record a voice message", label_visibility="hidden")

    logging.info(f"audio_bytes: {audio_bytes}")
    # Handle audio input
    if audio_bytes and audio_bytes != st.session_state.previous_audio_bytes:
        logging.info("audio_bytes appear.")
        st.session_state.audio_input_active = True
        st.session_state.audio_playback_active = False
        st.session_state.gen_answer_active = False

        if st.session_state.audio_input_active:
            try:
                text_from_audio = run_stt(audio_bytes)
                if text_from_audio is not None and text_from_audio != "":
                    st.session_state.text_from_audio_active = True
                    logging.info("STT completed successfully.")

                else:
                    st.session_state.text_from_audio_active = False
                st.session_state.audio_input_active = (
                    False  # Prevent further recording until processed
                )
                st.session_state.previous_audio_bytes = audio_bytes

            except Exception as e:
                logging.error(f"Error during STT: {e}")
                st.error(f"Error processing audio input: {e}")

with chat_container:
    # Handle text input
    st.markdown(
        "<h1 style='text-align: center; color: black;'>VNU-IS Virtual Assistant</h1>",
        unsafe_allow_html=True,
    )
    # st.title("VNU-IS Virtual Assistant")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if (prompt and prompt.strip()) or st.session_state.text_from_audio_active:
        logging.info(f"Gia Tri cua prompt {prompt}")
        if prompt and prompt.strip():
            st.session_state.gen_answer_active = True
        if st.session_state.text_from_audio_active:
            prompt = text_from_audio
            text_from_audio = None
            st.session_state.gen_answer_active = True
            logging.info(f"Gia Tri cua prompt speech to text {prompt}")

            # text_from_audio = None
            # prompt = None
        # Display user's message
        if st.session_state.gen_answer_active:
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})

            # Generate assistant response
            with st.chat_message("assistant"):
                try:
                    logging.info("Generating response...")
                    st.session_state.audio_playback_active = False
                    st.session_state.audio_input_active = False
                    st.session_state.gen_answer_active = False
                    st.session_state.text_from_audio_active = False
                    response = st.write_stream(ask(query=prompt))
                    st.session_state.messages.append(
                        {"role": "assistant", "content": response}
                    )

                except Exception as e:
                    logging.error(f"Error generating response: {e}")
                    st.error(f"Error generating assistant response: {e}")
    if len(st.session_state.messages) >= 1:
        play_audio = st.button("🔊 Play Audio")
        if play_audio:
            st.session_state.audio_playback_active = True
            st.session_state.audio_input_active = False
            st.session_state.text_from_audio_active = False
            if st.session_state.audio_playback_active:
                # Retrieve the last assistant response
                last_assistant_message = None
                for message in reversed(st.session_state.messages):
                    if message["role"] == "assistant":
                        last_assistant_message = message["content"]
                        break

                if last_assistant_message:
                    try:
                        audio_base64 = run_tts(text=last_assistant_message, lang="vi")
                        logging.info("TTS completed successfully.")

                        if audio_base64:
                            audio_bytes = base64.b64decode(audio_base64)
                            st.audio(audio_bytes, format="audio/wav", autoplay=True)
                            st.session_state.audio_playback_active = False
                            st.session_state.audio_input_active = False
                            st.session_state.text_from_audio_active = False
                            st.session_state.gen_answer_active = False

                        else:
                            st.error("Failed to generate audio.")
                    except Exception as e:
                        logging.error(f"Error during TTS or playback: {e}")
                        st.error(f"Error processing audio playback: {e}")
                else:
                    st.error("No assistant response available to play audio.")
                    st.session_state.audio_playback_active = False
                    st.session_state.audio_input_active = False
                    st.session_state.text_from_audio_active = False
                    st.session_state.gen_answer_active = False
# Handle audio playback
# chat_container_css = float_css_helper(top="10px")
footer_container_css = float_css_helper(bottom="90px")

footer_container.float(
    # "position: fixed; bottom: 90px;padding-top: -10px, padding-bottom: -100px"
    footer_container_css
)
# background-color: white
#
# -------------------------------------------
