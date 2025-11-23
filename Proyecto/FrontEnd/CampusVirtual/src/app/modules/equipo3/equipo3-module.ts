import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Equipo3RoutingModule } from './equipo3-routing-module';
import { HolaEquipo3Component } from './src/seguimiento/seguimiento';
import { Equipo3Home } from './equipo3-home/equipo3-home';
import { TorneosStandingComponent } from './src/torneos-standing/torneos-standing';

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    Equipo3RoutingModule,
    HolaEquipo3Component,
    Equipo3Home,
    TorneosStandingComponent,
  ],
})
export class Equipo3Module {}
