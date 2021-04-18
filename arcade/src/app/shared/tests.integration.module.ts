import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { BrowserModule } from '@angular/platform-browser';
import { CookieService } from 'ngx-cookie-service';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { RouterTestingModule } from '@angular/router/testing';

const unitTests = [RouterTestingModule];

const integrationTests = [
  BrowserModule,
  BrowserAnimationsModule,
  HttpClientModule,
];

@NgModule({
  declarations: [],
  providers: [CookieService],
  imports: [].concat(unitTests, integrationTests),
  exports: [].concat(unitTests, integrationTests),
})
export class IntegrationTestingModule {}
