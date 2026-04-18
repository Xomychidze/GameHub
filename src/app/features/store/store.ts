import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Header } from '../../shared/header/header';
import { Footer } from '../../shared/footer/footer';
import { GameCardComponent } from '../../shared/game-card/game-card';
import { GameService } from '../../core/services/game.service';
import { Game } from '../../core/models/game';
import { Genre } from '../../core/models/genre';

@Component({
  selector: 'app-store',
  standalone: true,
  imports: [CommonModule, FormsModule, Header, Footer, GameCardComponent],
  templateUrl: './store.html',
  styleUrl: './store.css',
})
export class Store implements OnInit {
  games: Game[] = [];
  genres: Genre[] = [];
  loading = true;

  selectedGenre: number | null = null;
  searchQuery = '';
  sortBy = 'title';

  constructor(private gameService: GameService) {}

  ngOnInit() {
    this.gameService.getGenres().subscribe(g => this.genres = g);
    this.loadGames();
  }

  loadGames() {
    this.loading = true;
    this.gameService.getGames({
      genre:  this.selectedGenre ?? undefined,
      search: this.searchQuery || undefined,
      sort:   this.sortBy,
    }).subscribe({
      next: data => { this.games = data; this.loading = false; },
      error: () => this.loading = false,
    });
  }

  onGenreChange(genreId: number | null) {
    this.selectedGenre = genreId;
    this.loadGames();
  }

  onSearch() { this.loadGames(); }
  onSort()   { this.loadGames(); }
}
