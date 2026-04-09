import { Component } from '@angular/core';
import { Footer } from '../../shared/footer/footer';
import { Header } from '../../shared/header/header';
import { ActivatedRoute } from '@angular/router';
import { HttpErrorResponse } from '@angular/common/http';
import { Game } from '../../core/models/game';
import { GameService } from '../../core/services/game-service';

@Component({
  selector: 'app-game-detail-component',
  imports: [Footer, Header],
  templateUrl: './game-detail-component.html',
  styleUrls: ['./game-detail-component.css'],
})
export class GameDetailComponent {
  id: number = 0;
  game?: Game;
  loading = true;

  constructor(
    private route: ActivatedRoute,
    private gameService: GameService
  ) {}

  ngOnInit() {
    // Получаем id из роутера
    this.route.paramMap.subscribe(params => {
      const idParam = params.get('id');
      if (idParam) {
        this.id = Number(idParam);
        this.loadGame();
      }
    });
  }

  // Метод для загрузки одной игры
  loadGame() {
    this.gameService.getGames().subscribe({
      next: (data: Game[]) => {
        this.game = data.find(g => g.id === this.id);
        this.loading = false;
      },
      error: (err: HttpErrorResponse) => {
        console.error(err.message);
        this.loading = false;
      }
    });
  }


  getStars(rating: number): number[] {
  return Array(Math.floor(rating)).fill(0);
  }

  getEmptyStars(rating: number): number[] {
    return Array(5 - Math.floor(rating)).fill(0);
  }
}
