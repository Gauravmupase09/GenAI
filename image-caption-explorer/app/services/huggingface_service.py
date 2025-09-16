# app/services/huggingface_service.py
from transformers import pipeline
from config.config import Config
from PIL import Image
from app.utils.image_utils import read_upload_file_as_image
import requests
from io import BytesIO


class HuggingFaceService:
    """Service for generating image captions using Salesforce/blip-image-captioning-large."""

    def __init__(self):
        Config.validate()
        self.caption_pipe = pipeline(
            "image-to-text",
            model="Salesforce/blip-image-captioning-large"
        )

    def generate_caption_from_file(self, file) -> str:
        """
        Generate caption from UploadFile.
        """
        try:
            image = read_upload_file_as_image(file)
            return self.generate_caption(image)
        except Exception as e:
            raise RuntimeError(f"Failed to process image file: {e}")

    def generate_caption_from_url(self, url: str) -> str:
        """
        Generate caption from an image URL.
        """
        try:
            response = requests.get(url, timeout=Config.DEFAULT_TIMEOUT)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content)).convert("RGB")
            return self.generate_caption(image)
        except Exception as e:
            raise RuntimeError(f"Failed to fetch or process image from URL {url}: {e}")

    def generate_caption(self, image: Image.Image) -> str:
        """
        Generate caption from a PIL Image.
        """
        try:
            result = self.caption_pipe(image)
            caption = result[0].get("generated_text", "")
            if not caption:
                raise ValueError("No caption generated.")
            return caption
        except Exception as e:
            raise RuntimeError(f"Caption generation failed: {e}")