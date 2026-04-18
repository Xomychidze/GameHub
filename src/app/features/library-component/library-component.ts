import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { Header } from '../../shared/header/header';
import { Footer } from '../../shared/footer/footer';
import { ProfileService } from '../../core/services/profile.service';
import { Purchase } from '../../core/models/purchase';

@Component({
  selector: 'app-library-component',
  standalone: true,
  imports: [CommonModule, RouterModule, FormsModule, Header, Footer],
  templateUrl: './library-component.html',
  styleUrl: './library-component.css',
})
export class LibraryComponent implements OnInit {
  purchases: Purchase[] = [];
  filtered: Purchase[] = [];
  loading = true;
  search = '';

  constructor(private profileService: ProfileService) {}

  ngOnInit() {
    this.profileService.getProfile().subscribe({
      next: profile => {
        this.purchases = profile.purchasedGames;
        this.filtered = this.purchases;
        this.loading = false;
      },
      error: () => this.loading = false,
    });
  }

  onSearch() {
    const q = this.search.toLowerCase();
    this.filtered = this.purchases.filter(p => p.game.title.toLowerCase().includes(q));
  }
}
