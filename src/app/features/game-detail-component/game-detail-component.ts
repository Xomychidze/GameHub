import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Footer } from '../../shared/footer/footer';
import { Header } from '../../shared/header/header';
import { ActivatedRoute } from '@angular/router';
import { HttpErrorResponse } from '@angular/common/http';
import { Game } from '../../core/models/game';
import { GameService } from '../../core/services/game-service';

@Component({
  selector: 'app-game-detail-component',
  standalone: true,
  imports: [Footer, Header, CommonModule],
  templateUrl: './game-detail-component.html',
  styleUrls: ['./game-detail-component.css'],
})
export class GameDetailComponent {
  id: number = 0;
  game?: Game;
  loading = true;
  error = '';

  constructor(
    private route: ActivatedRoute,
    private gameService: GameService,
  ) {}

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      const idParam = params.get('id');
      if (idParam) {
        this.id = Number(idParam);
        this.loadGame();
      }
    });
  }

  loadGame() {
    this.loading = true;
    this.gameService.getGameById(this.id).subscribe({
      next: (data: Game) => {
        this.game = data;
        this.loading = false;
      },
      error: (err: HttpErrorResponse) => {
        this.error = 'Game not found.';
        this.loading = false;
        console.error(err.message);
      },
    });
  }

  getStars(rating: number): number[] {
    return Array(Math.floor(rating)).fill(0);
  }

  getEmptyStars(rating: number): number[] {
    return Array(5 - Math.floor(rating)).fill(0);
  }
}
