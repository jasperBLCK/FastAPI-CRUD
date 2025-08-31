from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Используем SQLite для простоты (будет файл test.db)
# Для PostgreSQL строка будет такая:
# "postgresql+psycopg2://myuser:mypassword@localhost/mydatabase"
DATABASE_URL = "sqlite:///test.db"

engine = create_engine(DATABASE_URL, echo=True)  # echo=True → показывает SQL-запросы
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
