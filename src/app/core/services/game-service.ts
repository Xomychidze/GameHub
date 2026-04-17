import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Game } from '../models/game';

@Injectable({ providedIn: 'root' })
export class GameService {
  private readonly API = 'http://localhost:8000/api';

  constructor(private http: HttpClient) {}

  getGames(): Observable<Game[]> {
    return this.http.get<Game[]>(`${this.API}/games/`);
  }

  getGameById(id: number): Observable<Game> {
    return this.http.get<Game>(`${this.API}/games/${id}/`);
  }

  createGame(game: Partial<Game>): Observable<Game> {
    return this.http.post<Game>(`${this.API}/games/`, game);
  }

  updateGame(id: number, game: Partial<Game>): Observable<Game> {
    return this.http.put<Game>(`${this.API}/games/${id}/`, game);
  }

  deleteGame(id: number): Observable<void> {
    return this.http.delete<void>(`${this.API}/games/${id}/`);
  }

  getGenres(): Observable<any[]> {
    return this.http.get<any[]>(`${this.API}/genres/`);
  }
}
