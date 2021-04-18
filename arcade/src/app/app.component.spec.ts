import { TestBed, async } from '@angular/core/testing';

import { AppComponent } from './app.component';
import { UnitTestingModule } from 'src/app/shared/tests.unit.module';

describe('AppComponent', () => {
  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [UnitTestingModule],
      declarations: [AppComponent],
    }).compileComponents();
  }));

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });
});
