from app.models import user_model
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)