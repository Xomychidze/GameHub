import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { Header } from '../../shared/header/header';
import { Footer } from '../../shared/footer/footer';
import { GameService } from '../../core/services/game.service';
import { CartService } from '../../core/services/cart.service';
import { AuthService } from '../../core/services/auth.service';
import { Game } from '../../core/models/game';
import { Review } from '../../core/models/purchase';

@Component({
  selector: 'app-game-detail-component',
  standalone: true,
  imports: [CommonModule, FormsModule, Header, Footer],
  templateUrl: './game-detail-component.html',
  styleUrl: './game-detail-component.css',
})
export class GameDetailComponent implements OnInit {
  game?: Game;
  reviews: Review[] = [];
  loading = true;
  reviewText = '';
  reviewRating = 5;
  reviewError = '';
  reviewSubmitting = false;

  constructor(
    private route: ActivatedRoute,
    private gameService: GameService,
    public cartService: CartService,
    public authService: AuthService,
  ) {}

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      const id = Number(params.get('id'));
      if (id) this.loadGame(id);
    });
  }

  loadGame(id: number) {
    this.loading = true;
    this.gameService.getGameById(id).subscribe({
      next: game => {
        this.game = game;
        this.loading = false;
        // ← лог теперь внутри коллбэка, где game уже загружен
        console.log('game loaded:', this.game);
        this.gameService.getReviews(id).subscribe(r => this.reviews = r);
      },
      error: () => this.loading = false,
    });
  }

  addToCart() {
    if (this.game) this.cartService.add(this.game);
  }

  // Math.round + clamp [0..5] — защита от дробных и выходящих за диапазон значений
  stars(n: number): number[] {
    const count = Math.min(5, Math.max(0, Math.round(n)));
    return Array(count).fill(0);
  }

  emptyStars(n: number): number[] {
    const filled = Math.min(5, Math.max(0, Math.round(n)));
    return Array(5 - filled).fill(0);
  }

  submitReview() {
    if (!this.game || !this.reviewText.trim()) return;
    this.reviewSubmitting = true;
    this.reviewError = '';
    this.gameService.postReview(this.game.id, { rating: this.reviewRating, text: this.reviewText }).subscribe({
      next: review => {
        this.reviews = [review, ...this.reviews];
        this.reviewText = '';
        this.reviewRating = 5;
        this.reviewSubmitting = false;
      },
      error: err => {
        this.reviewError = err.error?.error || err.error?.non_field_errors?.[0] || 'Failed to submit review.';
        this.reviewSubmitting = false;
      },
    });
  }

  likeReview(review: Review) {
    this.gameService.reviewAction(review.id, 'like').subscribe(updated => {
      this.reviews = this.reviews.map(r => r.id === updated.id ? updated : r);
    });
  }

  dislikeReview(review: Review) {
    this.gameService.reviewAction(review.id, 'dislike').subscribe(updated => {
      this.reviews = this.reviews.map(r => r.id === updated.id ? updated : r);
    });
  }
}
