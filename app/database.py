from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Replace username, password, and dbname if different
DATABASE_URL = "postgresql://postgres:Vansh%40Negi@localhost:5432/notesdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
