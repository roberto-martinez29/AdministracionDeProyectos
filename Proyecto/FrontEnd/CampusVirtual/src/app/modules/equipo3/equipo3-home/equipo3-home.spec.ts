import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Equipo3Home } from './equipo3-home';

describe('Equipo3Home', () => {
  let component: Equipo3Home;
  let fixture: ComponentFixture<Equipo3Home>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Equipo3Home]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Equipo3Home);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
