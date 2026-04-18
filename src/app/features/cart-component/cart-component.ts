import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { Header } from '../../shared/header/header';
import { Footer } from '../../shared/footer/footer';
import { CartService } from '../../core/services/cart.service';
import { Game } from '../../core/models/game';

@Component({
  selector: 'app-cart-component',
  standalone: true,
  imports: [CommonModule, RouterModule, Header, Footer],
  templateUrl: './cart-component.html',
  styleUrl: './cart-component.css',
})
export class CartComponent {
  purchasing = false;
  success = false;
  error = '';

  constructor(public cartService: CartService) {}

  remove(game: Game) { this.cartService.remove(game.id); }

  checkout() {
    if (this.cartService.items.length === 0) return;
    this.purchasing = true;
    this.error = '';
    this.cartService.purchaseAll().subscribe({
      next: () => {
        this.cartService.clear();
        this.success = true;
        this.purchasing = false;
      },
      error: err => {
        this.error = err.error?.error || 'Purchase failed. Please try again.';
        this.purchasing = false;
      },
    });
  }
}
