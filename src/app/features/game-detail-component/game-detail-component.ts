import { Component } from '@angular/core';
import { Footer } from '../../shared/footer/footer';
import { Header } from '../../shared/header/header';

@Component({
  selector: 'app-game-detail-component',
  imports: [Footer, Header],
  templateUrl: './game-detail-component.html',
  styleUrl: './game-detail-component.css',
})
export class GameDetailComponent {

}
