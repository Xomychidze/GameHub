import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Game } from '../models/game';
import { Genre } from '../models/genre';
import { Review } from '../models/purchase';

@Injectable({ providedIn: 'root' })
export class GameService {
  private readonly API = 'http://localhost:8000/api';
  constructor(private http: HttpClient) {}

  getGames(filters?: { genre?: number; search?: string; sort?: string }): Observable<Game[]> {
    let params = new HttpParams();
    if (filters?.genre)  params = params.set('genre',  String(filters.genre));
    if (filters?.search) params = params.set('search', filters.search);
    if (filters?.sort)   params = params.set('sort',   filters.sort);
    return this.http.get<Game[]>(`${this.API}/games/`, { params });
  }

  getGameById(id: number): Observable<Game> {
    return this.http.get<Game>(`${this.API}/games/${id}/`);
  }

  getGenres(): Observable<Genre[]> {
    return this.http.get<Genre[]>(`${this.API}/genres/`);
  }

  getReviews(gameId: number): Observable<Review[]> {
    return this.http.get<Review[]>(`${this.API}/games/${gameId}/reviews/`);
  }

  postReview(gameId: number, data: { rating: number; text: string }): Observable<Review> {
    return this.http.post<Review>(`${this.API}/games/${gameId}/reviews/`, data);
  }

  reviewAction(reviewId: number, action: 'like' | 'dislike'): Observable<Review> {
    return this.http.post<Review>(`${this.API}/reviews/${reviewId}/action/`, { action });
  }
}
