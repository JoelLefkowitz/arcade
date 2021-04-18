import { TestBed } from '@angular/core/testing';
import { ThemeService } from './theme.service';
import { UnitTestingModule } from 'src/app/shared/tests.unit.module';

describe('ThemeService', () => {
  let service: ThemeService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [UnitTestingModule],
    });
    service = TestBed.inject(ThemeService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
