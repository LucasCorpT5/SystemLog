from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///systemlog.db"

engine = create_engine(CONN, echo=True) # Criando a engine e o echo=True porque eu quero que mostre os logs
Session = sessionmaker(bind=engine) # Passando a engine
session = Session()
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = "Pessoa"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(200))
    senha = Column(String(100))

Base.metadata.create_all(engine) # Criando todas as colunas