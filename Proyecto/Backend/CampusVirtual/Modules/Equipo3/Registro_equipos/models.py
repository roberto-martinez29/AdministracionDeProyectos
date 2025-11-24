from sqlmodel import SQLModel, Field
from typing import Optional

class EquipoDeportivo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre_equipo: str
    deporte: str
    categoria: str
    entrenador: str

class RegistroParticipante(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    matricula: str
    nombre: str
    equipo_id: int = Field(foreign_key="equipodeportivo.id")