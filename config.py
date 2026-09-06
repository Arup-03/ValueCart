import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


class Config:

    # ==============================
    # Amazon Creators API
    # ==============================

    AMAZON_CLIENT_ID = os.getenv(
        "AMAZON_CLIENT_ID",
        ""
    )

    AMAZON_CLIENT_SECRET = os.getenv(
        "AMAZON_CLIENT_SECRET",
        ""
    )

    AMAZON_PARTNER_TAG = os.getenv(
        "AMAZON_PARTNER_TAG",
        ""
    )

    AMAZON_MARKETPLACE = os.getenv(
        "AMAZON_MARKETPLACE",
        "www.amazon.in"
    )