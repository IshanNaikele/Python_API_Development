from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:23062004%23Ishan@localhost/FastAPI"



engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base =  declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Consume the generator once
db_gen = get_db()
db = next(db_gen)   # This triggers the function up to yield
print("DB session:", db)

# Close it properly
db_gen.close()
