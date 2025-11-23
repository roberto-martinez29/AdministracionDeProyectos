import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import {
  Equipo3Service,
  TournamentSummary,
  StandingRow,
} from '../../equipo3';

@Component({
  selector: 'app-torneos-standing',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './torneos-standing.html',
  styleUrls: ['./torneos-standing.css'],
})
export class TorneosStandingComponent implements OnInit {
  torneos: TournamentSummary[] = [];
  torneoSeleccionado?: TournamentSummary;
  standing: StandingRow[] = [];

  loading = false;
  error = '';

  constructor(private equipo3Service: Equipo3Service) {}

  ngOnInit(): void {
    this.cargarTorneos();
  }

  cargarTorneos(): void {
    this.loading = true;
    this.error = '';

    this.equipo3Service.getTorneos().subscribe({
      next: (data) => {
        this.torneos = data;
        this.loading = false;

        if (this.torneos.length > 0) {
          this.seleccionarTorneo(this.torneos[0]);
        }
      },
      error: (err) => {
        console.error(err);
        this.error = 'Ocurrió un error al cargar los torneos.';
        this.loading = false;
      },
    });
  }

  seleccionarTorneo(torneo: TournamentSummary): void {
    this.torneoSeleccionado = torneo;
    this.loading = true;
    this.error = '';

    this.equipo3Service.getStanding(torneo.tournament_id).subscribe({
      next: (data) => {
        this.standing = data;
        this.loading = false;
      },
      error: (err) => {
        console.error(err);
        this.error = 'Ocurrió un error al cargar el standing.';
        this.loading = false;
      },
    });
  }
}
