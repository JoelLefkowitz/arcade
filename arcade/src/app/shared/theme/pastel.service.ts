import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class PastelService {

  pastelColors = [
    '#ffb5e8',
    '#ff9cee',
    '#ffccf9',
    '#fcc2ff',
    '#ffa6ff',
    '#b28dff',
    '#cfa3ff',
    '#d5aaff',
    '#ecd4ff',
    '#fbe4ff',
    '#dcd3ff',
    '#a79aff',
    '#b5b9ff',
    '#97a2ff',
    '#afcbff',
    '#aff8db',
    '#c4faf8',
    '#85e3ff',
    '#ace7ff',
    '#6eb5ff',
    '#bffcc6',
    '#dbffd6',
    '#f3ffe3',
    '#e7ffac',
    '#ffffd1',
    '#ffc9de',
    '#ffabab',
    '#ffbebc',
    '#ffcbc1',
    '#fff5ba'
  ];

  constructor() { }

  getByName(name: string) {
    const ord = name.split('').reduce(
      (acc: number, i: string) => acc + i.charCodeAt(0), 0
    );
    return this.pastelColors[ord % this.pastelColors.length];
  }
}
