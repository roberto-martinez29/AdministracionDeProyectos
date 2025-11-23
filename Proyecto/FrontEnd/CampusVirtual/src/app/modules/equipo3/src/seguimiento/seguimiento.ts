import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import {
  Equipo3Service,
  GameSummary,
  GameTrackingResponse,
} from '../../equipo3';

@Component({
  selector: 'app-seguimiento',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './seguimiento.html',
  styleUrls: ['./seguimiento.css'],
})
export class HolaEquipo3Component implements OnInit {
  juegos: GameSummary[] = [];

  selectedGameId: number | null = null;

  juego!: GameTrackingResponse;

  loading = false;
  error: string | null = null;

  constructor(private equipo3Service: Equipo3Service) {}

  ngOnInit(): void {
    this.cargarListaJuegos();
  }

  // Cargar lista de juegos desde el backend
  cargarListaJuegos(): void {
    this.loading = true;
    this.error = null;

    this.equipo3Service.getListaJuegos().subscribe({
      next: (data: GameSummary[]) => {
        this.juegos = data;
        this.loading = false;
      },
      error: (err) => {
        console.error(err);
        this.error = 'Ocurrió un error al obtener la lista de juegos.';
        this.loading = false;
      },
    });
  }

  // Cuando haces click en un juego de la lista
  cargarJuego(gameId: number): void {
    this.selectedGameId = gameId;
    this.loading = true;
    this.error = null;

    this.equipo3Service.getSeguimientoJuego(gameId).subscribe({
      next: (data: GameTrackingResponse) => {
        this.juego = data;
        this.loading = false;
      },
      error: (err) => {
        console.error(err);
        this.error = 'Ocurrió un error al cargar el seguimiento del juego.';
        this.loading = false;
      },
    });
  }

  // Botón "Refrescar juego actual"
  refrescarJuegoActual(): void {
    if (this.selectedGameId !== null) {
      this.cargarJuego(this.selectedGameId);
    }
  }
}
