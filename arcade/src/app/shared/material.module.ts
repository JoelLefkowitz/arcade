import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatToolbarModule } from '@angular/material/toolbar';
import { NgModule } from '@angular/core';

const material = [
  MatIconModule,
  MatToolbarModule,
  MatButtonModule
];

@NgModule({
  declarations: [],
  imports: [].concat([CommonModule], material),
  exports: [].concat(material),
})
export class MaterialModule {}
