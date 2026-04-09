import { Injectable } from '@angular/core';
import { Game } from '../models/game';
import { of, Observable } from 'rxjs';
@Injectable({
  providedIn: 'root',
})
export class GameService {
    private mockGames: Game[] = [
      {id: 1,
        title: 'Cyberpunk 2077',
        price: 2999,
        image: "assets/image/cyberPunk2077.jpg",
        rating: 4.2,
        genre: { id: 1, name: 'RPG', slug: 'rpg', description: 'Role-playing games' },
        description: '...'},
        {id: 2,
        title: 'Minecraft',
        price: 10000,
        image: "assets/image/minecraft.jpg",
        rating: 5.0,
        genre: { id: 1, name: 'Survival', slug: 'survive', description: 'Sandbox survival indi game' },
        description: '...'}
    ];
  getGames(): Observable<Game[]> {
    return of(this.mockGames);
  }
}

