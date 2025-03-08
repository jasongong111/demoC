import gradio as gr


examples = ["The quick brown fox jumps over the lazy dog"]
with gr.Blocks() as demo:
    gr.Markdown("""# Tadreamk Create Demo 🖼️
                ### Try out our latest Logo Generation Model!""")
    with gr.Row():
        prompt = gr.Text(max_lines=1,
                         placeholder="Enter your prompt here",
                         container=False,
                         show_label=False)
        gr.Button("Generate")
    with gr.Row():
        gr.Image("demo.jpg", height=300, width=300)
    with gr.Accordion("Advanced Options", open=False):
        temperature = gr.Slider(minimum=0,
                                maximum=1,
                                step=0.01,
                                value=0.5,
                                label="Temperature")
        with gr.Row():
            width = gr.Slider(minimum=256,
                              maximum=1024,
                              step=32,
                              value=1024,
                              label="Width")
            height = gr.Slider(minimum=256,
                               maximum=1024,
                               step=32,
                               value=1024,
                               label="Height")
        with gr.Row():
            style = gr.CheckboxGroup(["Typography", "Icon", "Illustration"],
                                     label="Style")
        with gr.Row():
            color = gr.CheckboxGroup(["Red", "Green", "Blue"],
                                     label="Colors")
    gr.Examples(
        examples=examples,
        inputs=[prompt]
        )


demo.launch()
