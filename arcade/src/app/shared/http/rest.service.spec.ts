import { RestService } from './rest.service';
import { TestBed } from '@angular/core/testing';
import { UnitTestingModule } from 'src/app/shared/tests.unit.module';

describe('RestService', () => {
    let service: RestService;

    beforeEach(() => {
        TestBed.configureTestingModule({
            imports: [UnitTestingModule],
        });
        service = TestBed.inject(RestService);
    });

    it('should be created', () => {
        expect(service).toBeTruthy();
    });
});
