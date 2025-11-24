from typing import Optional, List
from fastapi import APIRouter, HTTPException
from sqlmodel import SQLModel


class Score(SQLModel):
    home: int
    away: int

class GameSummary(SQLModel):
    game_id: int
    sport: str
    home_team: str
    away_team: str
    start_time: str
    status: str

class GameTrackingResponse(SQLModel):
    game_id: int
    sport: str
    home_team: str
    away_team: str
    location: str
    start_time: str
    status: str
    current_period: str
    time_remaining: Optional[str]
    score: Score


seguimiento_router = APIRouter(
    prefix="/equipo3",
    tags=["Equipo 3 - Deportes y seguimiento de juegos"],
)

FAKE_GAMES = {
    1: GameTrackingResponse(
        game_id=1,
        sport="Básquetbol",
        home_team="Lobos Ingeniería",
        away_team="Halcones Administración",
        location="Gimnasio Campus Arteaga",
        start_time="2024-11-18T18:00:00",
        status="EN_JUEGO",
        current_period="3er cuarto",
        time_remaining="04:32",
        score=Score(home=45, away=39),
    ),
    2: GameTrackingResponse(
        game_id=2,
        sport="Fútbol",
        home_team="Tigres Campus",
        away_team="Leones Contaduría",
        location="Campo 3",
        start_time="2024-11-19T20:30:00",
        status="PROGRAMADO",
        current_period="",
        time_remaining=None,
        score=Score(home=0, away=0),
    ),
}

@seguimiento_router.get(
    "/juegos",
    response_model=List[GameSummary],
    summary="Obtener lista de juegos",
    description="Devuelve un listado resumen de los juegos disponibles para seguimiento."
)

def get_games() -> list[GameSummary]:
    games: list[GameSummary] = []
    for game in FAKE_GAMES.values():
        games.append(
            GameSummary(
                game_id=game.game_id,
                sport=game.sport,
                home_team=game.home_team,
                away_team=game.away_team,
                start_time=game.start_time,
                status=game.status,
            )
        )
    return games

@seguimiento_router.get(
    "/juegos/{game_id}",
    response_model=GameTrackingResponse,
    summary="Obtener detalle de un juego",
    description="Devuelve la información detallada de un juego para seguimiento en tiempo real."
)
def get_game_detail(game_id: int) -> GameTrackingResponse:
    game = FAKE_GAMES.get(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    return game

@seguimiento_router.get(
    "/seguimiento-demo",
    response_model=GameTrackingResponse,
    summary="Ejemplo de seguimiento de un juego",
    description="Devuelve información de ejemplo de un partido para probar la integración."
)
def get_demo_tracking() -> GameTrackingResponse:
    return FAKE_GAMES[1]