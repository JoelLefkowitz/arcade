import { Component, OnInit } from '@angular/core';

import { ThemeService } from 'src/app/shared/theme/theme.service';

@Component({
  selector: 'app-invert',
  templateUrl: './invert.component.html',
  styleUrls: ['./invert.component.scss']
})
export class InvertComponent implements OnInit {

  constructor(private themeService: ThemeService) { }

  ngOnInit() {
  }

  invert() {
    this.themeService.toggleDarkTheme();
  }

}
