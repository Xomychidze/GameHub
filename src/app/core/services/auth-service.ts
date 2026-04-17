import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { BehaviorSubject, Observable, tap, catchError, throwError } from 'rxjs';
import { User } from '../models/user';
import { AuthResponse } from '../models/authResponse';
import { LoginRequest } from '../models/loginRequest';
import { LoggerService } from './logger-service';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private readonly API = 'http://localhost:8000/api/auth';
  private readonly TOKEN_KEY = 'access_token';
  private readonly REFRESH_KEY = 'refresh_token';

  private currentUserSubject = new BehaviorSubject<User | null>(null);
  public currentUser$ = this.currentUserSubject.asObservable();

  constructor(
    private http: HttpClient,
    private router: Router,
    private logger: LoggerService,
  ) {
    this.restoreSession();
  }

  get currentUser(): User | null {
    return this.currentUserSubject.value;
  }

  get isLoggedIn(): boolean {
    return !!this.getToken();
  }

  login(credentials: LoginRequest): Observable<AuthResponse> {
    this.logger.info('Попытка входа', credentials.username);

    return this.http.post<AuthResponse>(`${this.API}/login/`, credentials).pipe(
      tap(response => {
        this.saveTokens(response.accessToken, response.refreshToken);
        this.currentUserSubject.next(response.user);
        this.logger.info('Успешный вход', response.user.username);
      }),
      catchError(err => {
        this.logger.error('Ошибка входа', err.message);
        return throwError(() => err);
      }),
    );
  }

  register(data: { username: string; email: string; password: string }): Observable<AuthResponse> {
    return this.http.post<AuthResponse>(`${this.API}/register/`, data).pipe(
      tap(response => {
        this.saveTokens(response.accessToken, response.refreshToken);
        this.currentUserSubject.next(response.user);
        this.logger.info('Регистрация успешна', response.user.username);
      }),
      catchError(err => throwError(() => err)),
    );
  }

  logout(): void {
    const refreshToken = localStorage.getItem(this.REFRESH_KEY);
    if (refreshToken) {
      this.http.post(`${this.API}/logout/`, { refreshToken }).subscribe();
    }
    this.logger.info('Выход из системы');
    localStorage.removeItem(this.TOKEN_KEY);
    localStorage.removeItem(this.REFRESH_KEY);
    this.currentUserSubject.next(null);
    this.router.navigate(['/login']);
  }

  getToken(): string | null {
    return localStorage.getItem(this.TOKEN_KEY);
  }

  private saveTokens(access: string, refresh: string): void {
    localStorage.setItem(this.TOKEN_KEY, access);
    localStorage.setItem(this.REFRESH_KEY, refresh);
  }

  private restoreSession(): void {
    const token = this.getToken();
    if (token) {
      this.logger.debug('Сессия восстановлена из localStorage');
    }
  }
}
