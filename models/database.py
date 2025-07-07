
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime

Base = declarative_base()

class Evento(Base):
    __tablename__ = 'eventos'
    id = Column(Integer, primary_key=True)
    municipio = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.datetime.utcnow)

engine = create_engine('sqlite:///eventos.db', echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
