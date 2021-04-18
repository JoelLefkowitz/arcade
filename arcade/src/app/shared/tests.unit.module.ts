import { CommonModule } from '@angular/common';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { NgModule } from '@angular/core';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';
import { RouterTestingModule } from '@angular/router/testing';
import { SharedModule } from './shared.module';

const unitTests = [
  HttpClientTestingModule,
  RouterTestingModule,
  NoopAnimationsModule,
];

const reExports = [SharedModule];

@NgModule({
  declarations: [],
  imports: [].concat([CommonModule], unitTests, reExports),
  exports: [].concat(unitTests, reExports),
})
export class UnitTestingModule {}
