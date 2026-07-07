from pathlib import Path

PROJECT_ROOT = Path("/home/kadac/projects/local_rag/data")


DEFAULT_HISOTRY_DB_PATH = PROJECT_ROOT / "history.db"
DEFAULT_PDF_PATH = PROJECT_ROOT / "user_pdf.pdf"
DEFAULT_VECTOR_STORE_PATH = PROJECT_ROOT / "vector_store.db"
DEFAULT_USAGE_PATH = PROJECT_ROOT / "usage.db"


PROFILE_PATH = PROJECT_ROOT / "profile.json"
LATEST_USER_ID_STORE_PATH = PROJECT_ROOT / "latest_user_id_store.json"
