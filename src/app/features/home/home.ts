import { Component } from '@angular/core';
import {Footer} from './../../shared/footer/footer';
import {Header} from './../../shared/header/header';
import { Game } from '../../core/models/game';
import { GameService } from './../../core/services/game-service';
import { HttpErrorResponse } from '@angular/common/http';
import { GameCardComponent } from '../../shared/game-card/game-card';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-home',
  imports: [Header, Footer, GameCardComponent, RouterModule],
  templateUrl: './home.html',
  styleUrls: ['./home.css'],
  standalone: true
})
export class Home {
  games: Game[] = [];
  displayedGames: Game[] = [];
  loading = true;

  constructor(private gameService: GameService) {}

  ngOnInit() {
    this.gameService.getGames().subscribe({
      next: (data: Game[]) => {
        this.games = data;
        this.displayedGames = this.games; // ← было slice(0, 5)
        this.loading = false;
      },
      error: (err: HttpErrorResponse) => console.error(err.message)
    });
  }

  trackByGameId(index: number, game: Game) {
    return game.id;
  }

  loadMore() {
    const next = this.displayedGames.length + 5;
    this.displayedGames = this.games.slice(0, next);
  }
}
