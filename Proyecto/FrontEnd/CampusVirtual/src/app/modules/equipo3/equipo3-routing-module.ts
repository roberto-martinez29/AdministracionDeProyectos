import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HolaEquipo3Component } from './src/hola-equipo3/hola-equipo3';
import { Equipo3Home } from './equipo3-home/equipo3-home';

const routes: Routes = [
    {
        path: '',
    component: Equipo3Home,
  },
  {
    path: 'seguimiento',
    component: HolaEquipo3Component,
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class Equipo3RoutingModule { }