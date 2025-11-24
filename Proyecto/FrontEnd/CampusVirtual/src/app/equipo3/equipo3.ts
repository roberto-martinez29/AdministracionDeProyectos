import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Score {
  home: number;
  away: number;
}
export interface GameSummary {
  game_id: number;
  sport: string;
  home_team: string;
  away_team: string;
  start_time: string;
  status: string;
}

export interface GameTrackingResponse {
  game_id: number;
  sport: string;
  home_team: string;
  away_team: string;
  location: string;
  start_time: string;
  status: string;
  current_period: string;
  time_remaining?: string;
  score: Score;
}

export interface TournamentSummary {
  tournament_id: number;
  name: string;
  sport: string;
  start_date: string;
  end_date: string;
  status: string;
  total_teams: number;
}

export interface StandingRow {
  position: number;
  team_name: string;
  games_played: number;
  wins: number;
  losses: number;
  points_for: number;
  points_against: number;
  points_diff: number;
}


@Injectable({
  providedIn: 'root'
})
export class Equipo3Service {

  private apiUrl = 'http://127.0.0.1:8000/equipo3';

  constructor(private http: HttpClient) { }

  getGames(): Observable<GameSummary[]> {
    return this.http.get<GameSummary[]>(`${this.apiUrl}/juegos`);
  }

  getGameDetail(gameId: number): Observable<GameTrackingResponse> {
    return this.http.get<GameTrackingResponse>(`${this.apiUrl}/juegos/${gameId}`);
  }

  getSeguimientoDemo(): Observable<GameTrackingResponse> {
    return this.http.get<GameTrackingResponse>(`${this.apiUrl}/seguimiento-demo`);
  }

  getTorneos(): Observable<TournamentSummary[]> {
    return this.http.get<TournamentSummary[]>(`${this.apiUrl}/torneos`);
  }

  getTorneoDetail(tournamentId: number): Observable<TournamentSummary> {
    return this.http.get<TournamentSummary>(`${this.apiUrl}/torneos/${tournamentId}`);
  }

  getTorneoStanding(tournamentId: number): Observable<StandingRow[]> {
    return this.http.get<StandingRow[]>(`${this.apiUrl}/torneos/${tournamentId}/standing`);
  }

}