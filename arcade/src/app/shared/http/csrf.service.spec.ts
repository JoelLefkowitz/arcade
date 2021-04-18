import { CsrfService } from './csrf.service';
import { TestBed } from '@angular/core/testing';
import { UnitTestingModule } from 'src/app/shared/tests.unit.module';

describe('CsrfService', () => {
    let service: CsrfService;

    beforeEach(() => {
        TestBed.configureTestingModule({
            imports: [UnitTestingModule],
        });
        service = TestBed.inject(CsrfService);
    });

    it('should be created', () => {
        expect(service).toBeTruthy();
    });
});
