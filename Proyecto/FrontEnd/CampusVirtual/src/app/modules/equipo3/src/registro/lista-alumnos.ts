import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';


interface Equipo {
  id: number;
  nombre_equipo: number;
  deporte: string;
  categoria: string;
  entrenador: number;
}
interface Alumno {
  id: number;
  nombre: string;
  matricula: string;
}
@Component({
  selector: 'app-lista-alumnos',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './lista-alumnos.html',
  styleUrls: ['./registro.css']
})
export class ListaAlumnos {
  private route = inject(ActivatedRoute);

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      const id = params.get('equipo_id');
      this.equipo_id = id ?? '';
    });
  }
  equipo_id: string = '';
  equipo!: Equipo;
  alumnos: Alumno[] = [];

  private http = inject(HttpClient);

  API_URL = 'http://127.0.0.1:8000/api/equipo3';

  ngAfterViewInit() {
    this.getEquipo();
    this.getAlumnos();
  }

  getEquipo() {
    this.http.get<any>(`${this.API_URL}/equipo/${this.equipo_id}`).subscribe(data => {
      this.equipo = data;
    });
  }
  getAlumnos() {
    this.http.get<any[]>(`${this.API_URL}/equipo/${this.equipo_id}/alumnos`).subscribe(data => {
      this.alumnos = data;
    });
  }
  atras(): void {
    // Volver atrás; ajusta según tu enrutamiento
    window.history.back();
  }
}
