import { PastelService } from './pastel.service';
import { TestBed } from '@angular/core/testing';
import { UnitTestingModule } from 'src/app/shared/tests.unit.module';

describe('PastelService', () => {
  let service: PastelService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [UnitTestingModule],
    });
    service = TestBed.inject(PastelService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
