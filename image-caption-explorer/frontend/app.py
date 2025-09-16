import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/api"
MAX_DEPTH = 5

st.set_page_config(page_title="Image Caption Explorer", layout="centered")

st.title("📸 Image Caption Explorer")
st.write("Upload an image → Get caption + similar images → Select one → Explore next")

# Initialize session state
if "session_id" not in st.session_state:
    st.session_state.session_id = None
if "current_caption" not in st.session_state:
    st.session_state.current_caption = None
if "iteration_count" not in st.session_state:
    st.session_state.iteration_count = 0
if "history" not in st.session_state:
    st.session_state.history = []  # Track displayed images
if "similar_images" not in st.session_state:
    st.session_state.similar_images = []


def display_similar_images(images):
    """Show radio buttons with preview images + captions."""
    options = []
    for idx, img in enumerate(images):
        if img["url"] not in st.session_state.history:
            options.append(f"{idx}_{img['caption']}|{img['url']}")

    if options:
        selected = st.radio("Select an image to explore next", options=options, key=f"radio_{st.session_state.iteration_count}")

        if st.button("Explore Next", key=f"btn_{st.session_state.iteration_count}"):
            caption_part = selected.split("|")[0]
            selected_caption = caption_part.split("_", 1)[1]  # Remove index
            selected_url = selected.split("|")[1]

            st.session_state.current_caption = selected_caption
            st.session_state.history.append(selected_url)
            st.session_state.iteration_count += 1
            fetch_next_images()
    else:
        st.info("✅ No new images to show.")


def fetch_next_images():
    """Fetch next set of similar images from backend."""
    if st.session_state.iteration_count > MAX_DEPTH:
        st.success("✅ Reached max exploration depth!")
        return

    payload = {
        "session_id": st.session_state.session_id,
        "selected_caption": st.session_state.current_caption
    }

    try:
        response = requests.post(f"{API_URL}/explore/next", data=payload)
        data = response.json()

        if "similar_images" in data and data["similar_images"]:
            st.session_state.session_id = data.get("session_id", st.session_state.session_id)
            st.session_state.current_caption = data["original_caption"]
            st.session_state.similar_images = data["similar_images"]

            st.info(f"Iteration: {st.session_state.iteration_count} / {MAX_DEPTH}")
            st.write(f"Current Caption: {st.session_state.current_caption}")

            for img in st.session_state.similar_images:
                st.image(img["url"], width=300, caption=img["caption"])

            display_similar_images(st.session_state.similar_images)
        else:
            st.success("✅ No more similar images found or max depth reached.")

    except Exception as e:
        st.error(f"Failed to fetch next images: {e}")


# Step 1: Initial Image Upload
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file and st.button("Generate Caption & Explore Images"):
    st.session_state.iteration_count = 1
    st.session_state.history = []
    st.session_state.similar_images = []

    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
    try:
        response = requests.post(f"{API_URL}/explore", files=files)
        data = response.json()

        st.session_state.session_id = data["session_id"]
        st.session_state.current_caption = data["original_caption"]
        st.session_state.similar_images = data["similar_images"]

        st.success(f"Generated Caption: {st.session_state.current_caption}")
        st.info(f"Iteration: {st.session_state.iteration_count} / {MAX_DEPTH}")

        for img in st.session_state.similar_images:
            st.image(img["url"], width=300, caption=img["caption"])

        display_similar_images(st.session_state.similar_images)

    except Exception as e:
        st.error(f"Failed to explore image: {e}")

# Step 2: Continue Exploration if session ongoing
elif st.session_state.session_id and st.session_state.similar_images:
    st.info(f"Iteration: {st.session_state.iteration_count} / {MAX_DEPTH}")
    st.write(f"Current Caption: {st.session_state.current_caption}")

    for img in st.session_state.similar_images:
        st.image(img["url"], width=300, caption=img["caption"])

    display_similar_images(st.session_state.similar_images)
