import { TestBed } from '@angular/core/testing';
import { UnitTestingModule } from 'src/app/shared/tests.unit.module';
import { WindowService } from './window.service';

describe('WindowService', () => {
  let service: WindowService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [UnitTestingModule],
    });
    service = TestBed.inject(WindowService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
