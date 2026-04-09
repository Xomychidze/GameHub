import { Component, Input } from '@angular/core';
import { Game } from '../../core/models/game';
import { Router } from '@angular/router';
@Component({
  selector: 'app-game-card',
  standalone: true,
  templateUrl: './game-card.html',
  styleUrl: './game-card.css',
})
export class GameCardComponent {
  @Input() game!: Game;

  constructor(private router: Router){}

  goToGame(id : number){
    this.router.navigate(['/games', id]);
  }

}
