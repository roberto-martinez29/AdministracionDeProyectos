import { TestBed } from '@angular/core/testing';

import { Equipo3 } from './equipo3';

describe('Equipo3', () => {
  let service: Equipo3;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Equipo3);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
