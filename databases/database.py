import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
load_dotenv()
#
# Establece la configuración inicial a la base de datos.
#
DATABASE_URL = os.getenv("DB_URL")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
