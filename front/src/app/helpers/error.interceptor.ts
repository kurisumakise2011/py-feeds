import {Injectable} from '@angular/core';
import {HttpRequest, HttpHandler, HttpEvent, HttpInterceptor} from '@angular/common/http';
import {Observable, throwError} from 'rxjs';
import {catchError} from 'rxjs/operators';

import {AuthenticationService} from '../services';

@Injectable()
export class ErrorInterceptor implements HttpInterceptor {
  constructor(private authenticationService: AuthenticationService) {
  }

  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    try {
      return next.handle(request).pipe(catchError(err => {
        let e = err.error.error || err.error || 'Service is unavailable';
        if (e && typeof e == 'string') {
          return throwError(e);
        } else {
          return throwError('Service is unavailable')
        }
      }))
    } catch (e) {
      return throwError(e.message)
    }
  }
}
