import { Observable, fromEvent, of } from 'rxjs';
import { map, startWith } from 'rxjs/operators';

import { Injectable } from '@angular/core';
import { WindowService } from './window.service';

@Injectable({
    providedIn: 'root',
})
export class DisplaySizeService {
    constructor(private windowService: WindowService) {}

    get displaySize(): Observable<number> {
        const window = this.windowService.maybeWindow;
        return window ? this.watchWindowSize(window) : of(0);
    }

    watchWindowSize(window: Window): Observable<number> {
        return fromEvent(window, 'resize').pipe(
            map((_) => window.screen.width),
            startWith(window.screen.width)
        );
    }
}
