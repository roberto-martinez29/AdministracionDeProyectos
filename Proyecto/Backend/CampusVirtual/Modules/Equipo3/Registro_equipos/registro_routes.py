from fastapi import APIRouter, Depends
from sqlmodel import Session
from .database import get_session
from .crud import registrar_participante, obtener_info_equipo, obtener_alumnos_por_equipo, obtener_lista_equipos

registro_router = APIRouter()

@registro_router.post("/registrar")
def registrar(data: dict, session: Session = Depends(get_session)):
    return registrar_participante(data, session)

@registro_router.get("/equipo/{equipo_id}")
def ver_equipo(equipo_id: int, session: Session = Depends(get_session)):
    return obtener_info_equipo(equipo_id, session)

@registro_router.get("/equipo/{equipo_id}/alumnos")
def ver_alumnos(equipo_id: int, session: Session = Depends(get_session)):
    return obtener_alumnos_por_equipo(equipo_id, session)

@registro_router.get("/equipo")
def get_equipos(session: Session = Depends(get_session)):
    return obtener_lista_equipos(session)