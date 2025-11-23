import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

import { Equipo3RoutingModule } from './equipo3-routing-module';
import { Equipo3Home } from './equipo3-home/equipo3-home';
import { HolaEquipo3Component } from './src/hola-equipo3/hola-equipo3';
import { TorneosStandingComponent } from './src/torneos-standing/torneos-standing';

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule,
    Equipo3RoutingModule,
    Equipo3Home,
    HolaEquipo3Component,
    TorneosStandingComponent,
  ],
})
export class Equipo3Module {}
