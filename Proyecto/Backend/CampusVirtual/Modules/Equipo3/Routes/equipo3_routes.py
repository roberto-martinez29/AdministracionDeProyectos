from typing import List
from fastapi import APIRouter, HTTPException
from pathlib import Path
import json

from Modules.Equipo3.models import (
    GameSummary,
    GameTrackingResponse,
    TournamentSummary,
    StandingRow,
    Score,
)

router = APIRouter(tags=["Equipo 3 - Deportes"])
BASE_DIR = Path(__file__).resolve().parent.parent  # -> Modules/Equipo3
DB_PATH = BASE_DIR / "deportes.db"

import sqlite3
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
# -----------------------
#   ENDPOINTS JUEGOS
# -----------------------

@router.get("/juegos", response_model=List[GameSummary])
def listar_juegos() -> List[GameSummary]:
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT
                j.id AS game_id,
                j.deporte AS sport,
                el.nombre AS home_team,
                ev.nombre AS away_team,
                j.fecha AS start_time,
                j.estatus AS status
            FROM juegos j
            JOIN equipos el ON j.equipo_local_id = el.id
            JOIN equipos ev ON j.equipo_visitante_id = ev.id
            ORDER BY j.fecha ASC, j.id ASC;
            """
        )
        rows = cur.fetchall()

    return [GameSummary(**dict(row)) for row in rows]


@router.get("/juegos/{game_id}", response_model=GameTrackingResponse)
def obtener_seguimiento_juego(game_id: int) -> GameTrackingResponse:
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT
                j.id AS game_id,
                j.deporte AS sport,
                el.nombre AS home_team,
                ev.nombre AS away_team,
                j.ubicacion AS location,
                j.fecha AS start_time,
                j.estatus AS status,
                j.periodo AS current_period,      -- 👈 CAMBIA ESTO
                j.tiempo_restante AS time_remaining,
                j.marcador_local AS home_score,
                j.marcador_visitante AS away_score
            FROM juegos j
            JOIN equipos el ON j.equipo_local_id = el.id
            JOIN equipos ev ON j.equipo_visitante_id = ev.id
            WHERE j.id = ?;
            """,
            (game_id,),
        )
        row = cur.fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail="Juego no encontrado")

    score = Score(home=row["home_score"], away=row["away_score"])

    return GameTrackingResponse(
        game_id=row["game_id"],
        sport=row["sport"],
        home_team=row["home_team"],
        away_team=row["away_team"],
        location=row["location"],
        start_time=row["start_time"],
        status=row["status"],
        current_period=row["current_period"],
        time_remaining=str(row["time_remaining"]) if row["time_remaining"] is not None else None,
        score=score,
    )


# -----------------------
#   ENDPOINTS TORNEOS
# -----------------------

@router.get("/torneos", response_model=List[TournamentSummary])
def listar_torneos() -> List[TournamentSummary]:
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT
                id          AS tournament_id,
                nombre      AS name,
                deporte     AS sport,
                fecha_inicio AS start_date,
                fecha_fin   AS end_date,
                estatus     AS status,
                total_equipos AS total_teams
            FROM torneos
            ORDER BY fecha_inicio ASC, id ASC;
            """
        )
        rows = cur.fetchall()

    return [TournamentSummary(**dict(row)) for row in rows]


@router.get("/torneos/{tournament_id}/standing",
            response_model=List[StandingRow])
def obtener_standing(tournament_id: int) -> List[StandingRow]:
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT
                s.posicion      AS position,
                e.nombre        AS team_name,
                s.juegos_juegos AS games_played,
                s.ganados       AS wins,
                s.perdidos      AS losses,
                s.puntos_favor  AS points_for,
                s.puntos_contra AS points_against,
                s.diferencia    AS points_diff
            FROM standings s
            JOIN equipos e ON s.equipo_id = e.id
            WHERE s.torneo_id = ?
            ORDER BY s.posicion ASC;
            """,
            (tournament_id,),
        )
        rows = cur.fetchall()

    if not rows:
        # puede ser 404 o lista vacía; yo dejo 404 para que se note
        raise HTTPException(status_code=404, detail="Standing no encontrado")

    return [StandingRow(**dict(row)) for row in rows]

equipo3_router = router
