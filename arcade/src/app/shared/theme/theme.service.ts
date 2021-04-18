import { BehaviorSubject, Observable } from 'rxjs';

import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class ThemeService {
  isDarkTheme: Observable<boolean>;

  private isDarkThemeSource = new BehaviorSubject<boolean>(true);

  constructor() {
    this.isDarkTheme = this.isDarkThemeSource.asObservable();
  }

  setDarkTheme(): void {
    this.isDarkThemeSource.next(true);
  }

  unsetDarkTheme(): void {
    this.isDarkThemeSource.next(false);
  }

  toggleDarkTheme(): void {
    this.isDarkThemeSource.next(!this.isDarkThemeSource.getValue());
  }
}
