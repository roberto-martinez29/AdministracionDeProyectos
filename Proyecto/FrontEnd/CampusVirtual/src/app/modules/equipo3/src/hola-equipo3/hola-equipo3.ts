import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { Equipo3Service, GameSummary, GameTrackingResponse } from '../../../../equipo3/equipo3';

@Component({
  selector: 'app-hola-equipo3',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './hola-equipo3.html',
  styleUrls: ['./hola-equipo3.css']
})
export class HolaEquipo3Component implements OnInit {

  juegos: GameSummary[] = [];
  juego!: GameTrackingResponse;
  selectedGameId: number | null = null;

  loading = false;
  error = '';

  constructor(private equipo3Service: Equipo3Service) { }

  ngOnInit(): void {
    this.cargarListaJuegos();
  }

  cargarListaJuegos(): void {
    this.loading = true;
    this.error = '';

    this.equipo3Service.getGames().subscribe({
      next: (lista) => {
        this.juegos = lista;
        this.loading = false;

        // Si hay juegos, cargamos el primero por defecto
        if (this.juegos.length > 0) {
          this.cargarJuego(this.juegos[0].game_id);
        }
      },
      error: (err) => {
        console.error(err);
        this.error = 'Ocurrió un error al obtener la lista de juegos.';
        this.loading = false;
      }
    });
  }

  cargarJuego(gameId: number): void {
    this.loading = true;
    this.error = '';
    this.selectedGameId = gameId;

    this.equipo3Service.getGameDetail(gameId).subscribe({
      next: (data) => {
        this.juego = data;
        this.loading = false;
      },
      error: (err) => {
        console.error(err);
        this.error = 'Ocurrió un error al cargar el seguimiento del juego.';
        this.loading = false;
      }
    });
  }

  refrescarJuegoActual(): void {
    if (this.selectedGameId !== null) {
      this.cargarJuego(this.selectedGameId);
    }
  }
}
