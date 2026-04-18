import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { Game } from '../../core/models/game';
import { CartService } from '../../core/services/cart.service';

@Component({
  selector: 'app-game-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './game-card.html',
  styleUrl: './game-card.css',
})
export class GameCardComponent {
  @Input() game!: Game;

  constructor(private router: Router, public cartService: CartService) {}

  goToGame() { this.router.navigate(['/games', this.game.id]); }

  addToCart(e: Event) {
    e.stopPropagation();
    this.cartService.add(this.game);
  }
}
