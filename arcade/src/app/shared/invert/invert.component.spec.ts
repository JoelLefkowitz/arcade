import { ComponentFixture, TestBed, async } from '@angular/core/testing';

import { InvertComponent } from './invert.component';
import { UnitTestingModule } from 'src/app/shared/tests.unit.module';

describe('InvertComponent', () => {
  let component: InvertComponent;
  let fixture: ComponentFixture<InvertComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [UnitTestingModule],
      declarations: [InvertComponent],
    }).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InvertComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
