import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable, forkJoin, of } from 'rxjs';
import { Game } from '../models/game';
import { Purchase } from '../models/purchase';

@Injectable({ providedIn: 'root' })
export class CartService {
  private readonly API = 'http://localhost:8000/api';
  private itemsSubject = new BehaviorSubject<Game[]>(this.load());
  public items$ = this.itemsSubject.asObservable();

  constructor(private http: HttpClient) {}

  get items(): Game[] { return this.itemsSubject.value; }
  get count(): number { return this.items.length; }
  get total(): number { return this.items.reduce((s, g) => s + g.price, 0); }

  add(game: Game): void {
    if (this.has(game.id)) return;
    const updated = [...this.items, game];
    this.save(updated);
    this.itemsSubject.next(updated);
  }

  remove(gameId: number): void {
    const updated = this.items.filter(g => g.id !== gameId);
    this.save(updated);
    this.itemsSubject.next(updated);
  }

  has(gameId: number): boolean { return this.items.some(g => g.id === gameId); }

  clear(): void { this.save([]); this.itemsSubject.next([]); }

  purchaseAll(): Observable<Purchase[]> {
    if (this.items.length === 0) return of([]);
    const reqs = this.items.map(g =>
      this.http.post<Purchase>(`${this.API}/purchases/`, { game_id: g.id })
    );
    return forkJoin(reqs);
  }

  private load(): Game[] {
    try { return JSON.parse(localStorage.getItem('cart') ?? '[]'); } catch { return []; }
  }
  private save(items: Game[]): void { localStorage.setItem('cart', JSON.stringify(items)); }
}
