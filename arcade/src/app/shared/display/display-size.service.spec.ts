import { DisplaySizeService } from './display-size.service';
import { TestBed } from '@angular/core/testing';
import { UnitTestingModule } from 'src/app/shared/tests.unit.module';

describe('DisplaySizeService', () => {
  let service: DisplaySizeService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [UnitTestingModule],
    });
    service = TestBed.inject(DisplaySizeService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
