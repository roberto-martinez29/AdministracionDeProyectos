from pydantic import BaseModel
from typing import Optional, List


class Score(BaseModel):
    home: int
    away: int


class GameSummary(BaseModel):
    game_id: int
    sport: str
    home_team: str
    away_team: str
    start_time: str
    status: str


class GameTrackingResponse(BaseModel):
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


class StandingRow(BaseModel):
    position: int
    team_name: str
    games_played: int
    wins: int
    losses: int
    points_for: int
    points_against: int
    points_diff: int


class TournamentSummary(BaseModel):
    tournament_id: int
    name: str
    sport: str
    start_date: str
    end_date: str
    status: str
    total_teams: int
    standing: Optional[List[StandingRow]] = None
