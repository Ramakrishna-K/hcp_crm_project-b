

from sqlalchemy import create_engine ,text
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

try:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("      MySQL Database Connected Successfully")

except Exception as e:
    print("       Database Connection Failed")
    print(e)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()