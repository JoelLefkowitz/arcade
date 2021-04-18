import { ActiveBackgroundDirective } from './theme/active-background.directive';
import { CommonModule } from '@angular/common';
import { FlexLayoutModule } from '@angular/flex-layout';
import { HomeComponent } from './home/home.component';
import { InvertComponent } from './invert/invert.component';
import { MatDarkThemeDirective } from './theme/mat-dark-theme.directive';
import { MaterialModule } from './material.module';
import { NgMicroInteractModule } from 'ng-micro-interact';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';

const shared = [
  InvertComponent,
  HomeComponent,
  MatDarkThemeDirective,
  ActiveBackgroundDirective,
];

const reExports = [
  MaterialModule,
  NgMicroInteractModule,
  FlexLayoutModule.withConfig({ ssrObserveBreakpoints: ['xs'] }),
];

@NgModule({
  declarations: [].concat(shared),
  imports: [].concat([CommonModule, RouterModule], reExports),
  exports: [].concat(shared, reExports),
})
export class SharedModule {}
