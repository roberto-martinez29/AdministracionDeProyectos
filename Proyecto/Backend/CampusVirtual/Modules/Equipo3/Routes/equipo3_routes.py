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

class TournamentSummary(SQLModel):
    tournament_id: int
    name: str
    sport: str
    start_date: str
    end_date: str
    status: str 
    total_teams: int


class StandingRow(SQLModel):
    position: int
    team_name: str
    games_played: int
    wins: int
    losses: int
    points_for: int
    points_against: int
    points_diff: int


equipo3_router = APIRouter(
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

FAKE_TOURNAMENTS: dict[int, TournamentSummary] = {
    1: TournamentSummary(
        tournament_id=1,
        name="Torneo Interfacultades 2024",
        sport="Básquetbol",
        start_date="2024-10-01",
        end_date="2024-11-30",
        status="EN_CURSO",
        total_teams=8,
    ),
    2: TournamentSummary(
        tournament_id=2,
        name="Liga de Futbol Nocturna",
        sport="Fútbol",
        start_date="2024-09-15",
        end_date="2024-12-10",
        status="PROGRAMADO",
        total_teams=10,
    ),
}

FAKE_STANDINGS: dict[int, list[StandingRow]] = {
    1: [
        StandingRow(
            position=1,
            team_name="Lobos Ingeniería",
            games_played=5,
            wins=5,
            losses=0,
            points_for=380,
            points_against=320,
            points_diff=60,
        ),
        StandingRow(
            position=2,
            team_name="Halcones Administración",
            games_played=5,
            wins=3,
            losses=2,
            points_for=350,
            points_against=340,
            points_diff=10,
        ),
        StandingRow(
            position=3,
            team_name="Jaguares Arquitectura",
            games_played=5,
            wins=2,
            losses=3,
            points_for=330,
            points_against=345,
            points_diff=-15,
        ),
    ],
    2: [
        StandingRow(
            position=1,
            team_name="Tigres Campus",
            games_played=0,
            wins=0,
            losses=0,
            points_for=0,
            points_against=0,
            points_diff=0,
        ),
        StandingRow(
            position=2,
            team_name="Leones Contaduría",
            games_played=0,
            wins=0,
            losses=0,
            points_for=0,
            points_against=0,
            points_diff=0,
        ),
    ],
}

@equipo3_router.get(
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

@equipo3_router.get(
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

@equipo3_router.get(
    "/seguimiento-demo",
    response_model=GameTrackingResponse,
    summary="Ejemplo de seguimiento de un juego",
    description="Devuelve información de ejemplo de un partido para probar la integración."
)
def get_demo_tracking() -> GameTrackingResponse:
    return FAKE_GAMES[1]

@equipo3_router.get(
    "/torneos",
    response_model=list[TournamentSummary],
    summary="Obtener lista de torneos",
    description="Devuelve todos los torneos."
)
def get_torneos() -> list[TournamentSummary]:
    return list(FAKE_TOURNAMENTS.values())

@equipo3_router.get(
    "/torneos/{tournament_id}",
    response_model=TournamentSummary,
    summary="Obtener detalle de torneo",
    description="Devuelve la información del torneo."
)
def get_torneo_detail(tournament_id: int) -> TournamentSummary:
    torneo = FAKE_TOURNAMENTS.get(tournament_id)
    if not torneo:
        raise HTTPException(status_code=404, detail="Torneo no encontrado")
    return torneo

@equipo3_router.get(
    "/torneos/{tournament_id}/standing",
    response_model=list[StandingRow],
    summary="Standing de torneo",
    description="Devuelve la tabla de posiciones del torneo."
)
def get_torneo_standing(tournament_id: int) -> list[StandingRow]:
    standing = FAKE_STANDINGS.get(tournament_id)
    if standing is None:
        raise HTTPException(status_code=404, detail="Standing no encontrado")
    return standing