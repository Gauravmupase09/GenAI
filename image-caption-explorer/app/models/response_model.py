# app/models/response_model.py
from pydantic import BaseModel
from typing import List


class ImageInfo(BaseModel):
    url: str
    caption: str


class ImageResponseModel(BaseModel):
    session_id: str
    original_caption: str
    similar_images: List[ImageInfo]