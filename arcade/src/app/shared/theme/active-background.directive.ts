import { Directive, ElementRef, Input, OnDestroy, OnInit } from '@angular/core';

import { Subscription } from 'rxjs';
import { ThemeService } from './theme.service';

@Directive({
  selector: '[appActiveBackground]',
})
export class ActiveBackgroundDirective implements OnInit, OnDestroy {
  @Input() dark = 'black';
  @Input() light = 'white';

  themeSubscription: Subscription;

  constructor(
    private element: ElementRef,
    private themeService: ThemeService
  ) {}

  ngOnInit(): void {
    this.themeSubscription = this.themeService.isDarkTheme.subscribe(
      (darkTheme: boolean) => {
        this.element.nativeElement.style.backgroundColor = darkTheme
          ? this.light
          : this.dark;

        this.element.nativeElement.style.color = darkTheme ? 'white' : 'black';
      }
    );
  }

  ngOnDestroy(): void {
    if (this.themeSubscription) {
      this.themeSubscription.unsubscribe();
    }
  }
}
