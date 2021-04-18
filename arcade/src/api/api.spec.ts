import { TestBed, async } from '@angular/core/testing';

import { HttpClient } from '@angular/common/http';
import { IntegrationTestingModule } from 'src/app/shared/tests.integration.module';

describe('API', () => {
  let http: HttpClient;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [IntegrationTestingModule],
      providers: [],
    });

    http = TestBed.inject(HttpClient);
    spyOn(http, 'get').and.callThrough();
  });
});
