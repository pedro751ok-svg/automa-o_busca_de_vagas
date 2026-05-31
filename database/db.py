from sqlalchemy import create_engine, String, Integer, Column, DateTime, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///vagas.db')
Base = declarative_base()
session = sessionmaker(bind=engine)

class Vagas(Base):
    __tablename__ = "vagas"
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    requisitos = Column(String, nullable=False)
    beneficios = Column(String, nullable=True)
    localidade = Column(String, nullable=True)
    link = Column(String, nullable=False, unique=True)
    data_encontrada = Column(DateTime, nullable=True)
    notificado = Column(Boolean, default=False)

Base.metadata.create_all(engine)