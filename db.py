
import os
from sqlalchemy import create_engine, text

from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv('DB_URL')




def connect_db():
    engine = create_engine(DB_URL)
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1;"))
            print("Conexión exitosa a la base de datos:", result.scalar())
        return engine
    except Exception as e:
        print("Error de conexión:", e)
        return None



def crear_tablas():

    from models.base import Base
    import models.usuario
    import models.competiciones_favoritas
    import models.equipos_favoritos
    import models.jugadores_favoritos
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)
    print("Tablas creadas en la base de datos.")
