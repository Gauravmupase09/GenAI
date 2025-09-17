# app/image_utils.py
from fastapi import UploadFile
from PIL import Image
from io import BytesIO


def read_upload_file_as_image(upload_file: UploadFile) -> Image.Image:
    """
    Converts FastAPI UploadFile to PIL Image object.
    """
    image_bytes = upload_file.file.read()
    image = Image.open(BytesIO(image_bytes)).convert("RGB")
    return image