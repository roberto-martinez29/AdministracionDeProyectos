from sqlmodel import Session, select
from .models import RegistroParticipante, EquipoDeportivo

def registrar_participante(data: dict, session: Session):
    equipo = session.get(EquipoDeportivo, data["equipo_id"])
    if not equipo:
        raise ValueError("Equipo no encontrado")

    nuevo = RegistroParticipante(
        matricula=data["matricula"],
        nombre=data["nombre"],
        equipo_id=equipo.id
    )
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    return nuevo

def obtener_info_equipo(equipo_id: int, session: Session):
    return session.get(EquipoDeportivo, equipo_id)

def obtener_alumnos_por_equipo(equipo_id: int, session: Session):
    registros = session.exec(
        select(RegistroParticipante).where(RegistroParticipante.equipo_id == equipo_id)
    ).all()
    return registros

def obtener_lista_equipos(session: Session):
    equipos = session.exec(select(EquipoDeportivo)).all()
    return equipos
