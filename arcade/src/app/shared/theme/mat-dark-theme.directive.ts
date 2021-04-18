import {
    Directive,
    HostBinding,
    OnDestroy,
    OnInit,
} from '@angular/core';

import { Subscription } from 'rxjs';
import { ThemeService } from './theme.service';

@Directive({
    selector: '[appMatDarkTheme]',
})
export class MatDarkThemeDirective implements OnInit, OnDestroy {
    @HostBinding('class.dark-theme') darkTheme: boolean;

    themeSubscription: Subscription;

    constructor(private themeService: ThemeService) {}

    ngOnInit(): void {
        this.themeSubscription = this.themeService.isDarkTheme.subscribe(
            (darkTheme: boolean) => {
                this.darkTheme = darkTheme;
            }
        );
    }

    ngOnDestroy(): void {
        if (this.themeSubscription) {
            this.themeSubscription.unsubscribe();
        }
    }
}
