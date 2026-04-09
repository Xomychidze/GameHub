import { Component, Input } from '@angular/core';
import { Game } from '../../core/models/game';

@Component({
  selector: 'app-game-card',
  standalone: true,
  templateUrl: './game-card.html',
  styleUrl: './game-card.css',
})
export class GameCardComponent {
  @Input() game!: Game;
}
