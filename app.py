import streamlit as st
from PIL import Image
from itertools import cycle


def main():
    st.markdown(
        """
        <h1 style='text-align: center; color: black; padding-top:10px'>Composed image retrieval on
            <a href="https://cirr.cecs.anu.edu.au/">CIRR</a> dataset
        </h1>
        """,
        unsafe_allow_html=True,
    )

    input_section, output_section = st.columns([1, 2], gap="medium")

    with input_section:
        # Add a textbox
        user_input = st.text_input("Enter textual description:")

        # Add an image uploader
        uploaded_image = st.file_uploader(
            "Choose an image", type=["jpg", "jpeg", "png"], accept_multiple_files=False
        )

        if uploaded_image is not None:
            # Display uploaded image
            st.image(
                transform_input_image(uploaded_image),
                caption="Uploaded Image",
            )

        # Add a slider for grid size
        n_images = st.slider("Select number of output images", 5, 100, 5)

        submitted = st.button("Search")

    with output_section:
        if submitted and uploaded_image is not None:
            st.write(f"Your input: {user_input}")
            cols = cycle(st.columns(4))

            # Display processed images in a grid
            img_indices = range(n_images)
            for i, col in zip(img_indices, cols):
                processed_image = process_image(uploaded_image)
                col.image(
                    processed_image, caption=f"Dummy image {i}", use_column_width=True
                )


def transform_input_image(image):
    pil_image = Image.open(image)
    processed_image = pil_image.resize((128, 128))
    return processed_image


def process_image(uploaded_image):
    # Open the uploaded image using PIL
    pil_image = Image.open(uploaded_image)

    # Process the image (e.g., resize)
    processed_image = pil_image.resize((224, 224))

    return processed_image


if __name__ == "__main__":
    st.set_page_config(
        page_title="Pic2Word",
        page_icon="🔍",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    main()
