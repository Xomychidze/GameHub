import { GameService } from './../../core/services/game-service';
import { Component } from '@angular/core';
import { Footer } from '../../shared/footer/footer';
import { Header } from '../../shared/header/header';
import { Game } from '../../core/models/game';
import { HttpErrorResponse } from '@angular/common/http';
import { GameCardComponent } from '../../shared/game-card/game-card';
@Component({
  selector: 'app-store',
  imports: [Footer, Header, GameCardComponent],
  templateUrl: './store.html',
  styleUrl: './store.css',
})
export class Store {
  games: Game[] = [];
  loading = true;

  constructor(private gameService: GameService) {}

  ngOnInit(){
    this.gameService.getGames().subscribe({
      next: (data: Game[]) => {
        this.games = data;
        this.loading = false;
      },
      error: (err: HttpErrorResponse) => console.error(err.message)
    });
  }
}
