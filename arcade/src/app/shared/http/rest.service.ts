import { HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class RestService {
  constructor() {}

  paginationBuilder(limit?: number, offset?: number): string {
    if (limit && offset) {
      return `?limit=${limit}&offset=${offset}`;
    }

    if (limit) {
      return `?limit=${limit}`;
    }

    if (offset) {
      return `?offset=${offset}`;
    }

    return '';
  }

  errorMsg(error: HttpErrorResponse): string {
    if (error.error instanceof ErrorEvent) {
      return `Error: ${error.error.message}`;
    }

    switch (error.status) {
      case 404: {
        return `Not Found: ${error.message}`;
      }
      case 403: {
        return `Access Denied: ${error.message}`;
      }
      case 500: {
        return `Internal Server Error: ${error.message}`;
      }
      default: {
        return `Unknown Server Error: ${error.message}`;
      }
    }
  }
}
