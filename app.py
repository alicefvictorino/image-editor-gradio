import gradio as gr

from controller import process_image


def main():
    def update_operation_visibility(operation):
        return (
            gr.update(visible=(operation == "Geometric Transformations")),
            gr.update(visible=(operation == "Color Space Operations")),
            gr.update(visible=(operation == "Gamma Correction")),
        )

    with gr.Blocks(title="Image Processor") as app:
        gr.Markdown("# Image Processing Application")

        image_state = gr.State(value=None)
        original_image_state = gr.State(value=None)

        with gr.Row():
            with gr.Column():
                input_image = gr.Image(label="Original Image")
            with gr.Column():
                output_image = gr.Image(label="Processed Image")

        reset_btn = gr.Button("Reset Image")

        operation = gr.Radio(
            ["Geometric Transformations", "Color Space Operations", "Gamma Correction"],
            label="Select Operation",
            value="Geometric Transformations"
        )

        with gr.Group() as transf_geo_group:
            with gr.Row():
                with gr.Column():
                    trans_x = gr.Slider(-100, 100, value=0, step=1, label="Horizontal Translation (X)")
                with gr.Column():
                    trans_y = gr.Slider(-100, 100, value=0, step=1, label="Vertical Translation (Y)")
            with gr.Row():
                rotation_angle = gr.Slider(0, 360, value=0, step=1, label="Rotation Angle (°)")
            with gr.Row():
                with gr.Column():
                    scale_factor_x = gr.Slider(0.1, 3.0, value=1.0, step=0.1, label="Scale Factor (Width)")
                with gr.Column():
                    scale_factor_y = gr.Slider(0.1, 3.0, value=1.0, step=0.1, label="Scale Factor (Height)")
            
        with gr.Group(visible=False) as colors_group:
            color_space = gr.Dropdown(["RGB", "Grayscale", "HSV", "LAB"], label="Color Space", value="RGB")
            contrast_factor = gr.Slider(0.1, 3.0, value=1.0, step=0.1, label="Contrast Factor")

        with gr.Group(visible=False) as gamma_group:
            gamma_value = gr.Slider(0.1, 3.0, value=1.0, step=0.1, label="Gamma Value")

        operation.change(update_operation_visibility, [operation], [transf_geo_group, colors_group, gamma_group])

        process_btn = gr.Button("Process Image")
        process_btn.click(
            fn=process_image,
            inputs=[
                input_image, image_state, operation,
                trans_x, trans_y, rotation_angle,
                scale_factor_x, scale_factor_y,
                color_space, contrast_factor,
                gamma_value
            ],
            outputs=[output_image, image_state]
        )

        reset_btn.click(fn=lambda original: (original, original), inputs=[original_image_state], outputs=[output_image, image_state])
        input_image.change(fn=lambda img: (img, img, img), inputs=[input_image], outputs=[output_image, original_image_state, image_state])

    app.launch()

if __name__ == "__main__":
    main()
