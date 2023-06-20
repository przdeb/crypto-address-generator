from sqlalchemy import create_engine

from src.settings import PROJECT_ROOT

TEST_DATABASE_URL = f"sqlite:///{PROJECT_ROOT}/test_database.db"

engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
