import { Component, inject, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

interface Equipo {
  id: number;
  nombre_equipo: number;
  deporte: string;
  categoria: string;
  entrenador: number;
}
@Component({
  selector: 'app-registro',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './registro.html',
  styleUrls: ['./registro.css']
})
export class Registro {
  nombre: string = '';
  matricula: string = '';
  equipos: Equipo[] = [];
  private http = inject(HttpClient);
  private router = inject(Router);

  API_URL = 'http://127.0.0.1:8000/api/registro';

  constructor() { }

  ngOnInit(): void {

  }
  ngAfterViewInit() {
    this.getEquipos();
  }

  getEquipos() {
    this.http.get<any[]>(`${this.API_URL}/equipo`).subscribe(data => {
      this.equipos = data;
    });
  }

  registrar(id_equipo: number): void {
    const payload = {
      matricula: this.matricula,
      nombre: this.nombre,
      equipo_id: id_equipo
    };

    this.http.post<any>(`${this.API_URL}/registrar`, payload).subscribe({
      next: (res) => {
        console.log('Registro exitoso', res);
        // limpiar campos
        this.nombre = '';
        this.matricula = '';
        // refrescar datos si es necesario
        this.getEquipos();
        alert('Registro enviado correctamente');
      },
      error: (err) => {
        console.error('Error al registrar', err);
        alert('Error al registrar: ' + (err?.message ?? 'desconocido'));
      }
    });
  }
  listarParticipantes(equipo?: Equipo): void {
    if (!equipo) {
      console.warn('listarParticipantes: equipo no proporcionado');
      return;
    }
    this.router.navigate(['/equipo3/lista-alumnos', equipo.id]);
  }

  atras(): void {
    // Volver atrás; ajusta según tu enrutamiento
    window.history.back();
  }
}
