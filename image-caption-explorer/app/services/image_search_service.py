# app/services/image_search_service.py
import requests
import re
from config.config import Config


class ImageSearchService:
    """Service to search images using SerpAPI and return valid image URLs."""

    def __init__(self):
        Config.validate()
        self.api_key = Config.SERPAPI_API_KEY
        self.base_url = "https://serpapi.com/search.json"

    def search_images(self, query: str, max_results: int = 3) -> list[str]:
        """
        Search images using SerpAPI and return a list of direct image URLs (jpeg/jpg/png).

        Args:
            query (str): The search query (caption).
            max_results (int): Max number of image URLs to return.

        Returns:
            list[str]: List of valid image URLs.
        """
        params = {
            "q": query,
            "tbm": "isch",  # image search
            "ijn": "0",
            "api_key": self.api_key
        }

        try:
            response = requests.get(self.base_url, params=params, timeout=Config.DEFAULT_TIMEOUT)
            response.raise_for_status()
            data = response.json()

            image_urls = []

            if "images_results" in data:
                for image_result in data["images_results"]:
                    image_url = image_result.get("original") or image_result.get("thumbnail")
                    if image_url and self.is_valid_image_url(image_url):
                        image_urls.append(image_url)
                    if len(image_urls) >= max_results:
                        break

            return image_urls

        except requests.exceptions.RequestException as e:
            print(f"[ImageSearchService] Request Error: {e}")
            return []
        except Exception as e:
            print(f"[ImageSearchService] Unexpected Error: {e}")
            return []

    @staticmethod
    def is_valid_image_url(url: str) -> bool:
        """Check if URL ends with a valid image extension (jpg, jpeg, png)."""
        url = url.lower().split("?")[0]  # remove query parameters
        return bool(re.search(r'\.(jpg|jpeg|png)$', url))