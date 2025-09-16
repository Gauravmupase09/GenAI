# config/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Central configuration class for API keys and default settings."""

    # ----------------------
    # API Keys
    # ----------------------
    SERPAPI_API_KEY: str = os.getenv("SERPAPI_API_KEY")
    HUGGINGFACE_API_KEY: str = os.getenv("HUGGINGFACE_API_KEY")

    # ----------------------
    # Default Settings
    # ----------------------
    DEFAULT_TIMEOUT: int = int(os.getenv("DEFAULT_TIMEOUT", 30))  # seconds
    MAX_RECURSION_DEPTH: int = 5  # max number of iterations for image exploration

    # ----------------------
    # Initialization Check
    # ----------------------
    @classmethod
    def validate(cls):
        """Validate essential configurations and raise errors if missing."""
        if not cls.SERPAPI_API_KEY:
            raise ValueError("SERPAPI_API_KEY is not set in the environment variables.")
        if not cls.HUGGINGFACE_API_KEY:
            raise ValueError("HUGGINGFACE_API_KEY is not set in the environment variables.")
