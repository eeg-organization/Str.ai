import gradio as gr
from chatbot.text_chat import TextChatApp
from chatbot.audio_chat import AudioChatApp

class ChatApp:
    def __init__(self):
        self.text_chat_app = TextChatApp()
        self.audio_chat_app = AudioChatApp()

    def chat(self, user_input, audio):
        if audio is not None:
            return self.audio_chat_app.transcribe(audio)
        else:
            return self.text_chat_app.chat(user_input)

app = ChatApp()

input_textbox = gr.components.Textbox(label="User")
output_textbox = gr.components.Textbox(label="AI")
audio_input = gr.inputs.Audio(source="microphone", type="filepath")

ui = gr.Interface(fn=app.chat, inputs=[input_textbox, audio_input], 
                  outputs=output_textbox, 
                  title="Str.ai- A GPT powered text and audio based chat assistant", 
                  description="Engaging in heartfelt conversations with empathetic and non-judgmental friends can have an immediate positive impact on your well-being. This is the concept behind Stranger's Therapy, where you discover solace through meaningful connections.")
ui.launch()
