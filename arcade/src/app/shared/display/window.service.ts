import { isPlatformBrowser } from '@angular/common';
import { Inject, Injectable, PLATFORM_ID } from '@angular/core';

@Injectable({
    providedIn: 'root',
})
export class WindowService {
    isBrowser: boolean;

    constructor(
        @Inject(PLATFORM_ID) platformId: Record<string, unknown>
    ) {
        this.isBrowser = isPlatformBrowser(platformId);
    }

    get maybeWindow(): Window | null {
        return this.isBrowser ? window : null;
    }
}
