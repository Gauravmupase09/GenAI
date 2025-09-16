# app/routes.py
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from app.services.huggingface_service import HuggingFaceService
from app.services.image_search_service import ImageSearchService
from app.models.response_model import ImageResponseModel, ImageInfo
from config.config import Config

router = APIRouter()

# Initialize services
hf_service = HuggingFaceService()
image_search_service = ImageSearchService()

# Session store (in-memory, simple version)
SESSIONS = {}


@router.post("/explore", response_model=ImageResponseModel)
async def explore_image(file: UploadFile = File(...)):
    """
    User uploads an image → Generate caption → Fetch 3 similar images.
    """
    try:
        # Step 1: Generate caption from uploaded image
        caption = hf_service.generate_caption_from_file(file)

        # Step 2: Search for first 3 images using that caption
        similar_urls = image_search_service.search_images(query=caption, max_results=3)

        # Step 3: Generate captions for these similar images
        similar_images = []
        for url in similar_urls:
            img_caption = hf_service.generate_caption_from_url(url)
            similar_images.append(ImageInfo(url=url, caption=img_caption))

        # Step 4: Create session
        session_id = str(uuid.uuid4())
        SESSIONS[session_id] = {
            "last_caption": caption,
            "iteration": 1
        }

        return ImageResponseModel(
            session_id=session_id,
            original_caption=caption,
            similar_images=similar_images
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image exploration failed: {e}")


@router.post("/explore/next", response_model=ImageResponseModel)
async def explore_next_image(session_id: str = Form(...), selected_caption: str = Form(...)):
    """
    User selects an image → Take that image's caption as input → Fetch next 3 images → Generate captions.
    """
    try:
        if session_id not in SESSIONS:
            raise HTTPException(status_code=404, detail="Session not found")

        session = SESSIONS[session_id]

        if session["iteration"] >= Config.MAX_RECURSION_DEPTH:
            return ImageResponseModel(
                session_id=session_id,
                original_caption=selected_caption,
                similar_images=[]
            )

        # Search next 3 images using selected caption
        similar_urls = image_search_service.search_images(query=selected_caption, max_results=3)

        similar_images = []
        for url in similar_urls:
            img_caption = hf_service.generate_caption_from_url(url)
            similar_images.append(ImageInfo(url=url, caption=img_caption))

        # Update session
        session["last_caption"] = selected_caption
        session["iteration"] += 1
        SESSIONS[session_id] = session

        return ImageResponseModel(
            session_id=session_id,
            original_caption=selected_caption,
            similar_images=similar_images
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Next image exploration failed: {e}")