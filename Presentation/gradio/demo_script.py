import gradio as gr
from DataPresentation import DataToMessage,DiffInputs

def response(message, history):

    analyse = DiffInputs(message)
    if analyse == "None":
        return message
    message = DataToMessage(analyse)

    return message

demo = gr.ChatInterface(
    fn=response,
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder="Text Placeholder", container=False, scale=7),
    description="Description Placeholder",
    theme="soft",
    examples=["实例1", "实例2", "实例3"],
    cache_examples=False,
    retry_btn=None,
    undo_btn="UndoBtn",
    clear_btn="ClearBtn",
    title="政务语义引擎")
demo.launch()
