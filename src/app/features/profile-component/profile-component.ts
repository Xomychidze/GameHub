import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { Header } from '../../shared/header/header';
import { Footer } from '../../shared/footer/footer';
import { ProfileService } from '../../core/services/profile.service';
import { Profile } from '../../core/models/profile';

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule, Header, Footer],
  templateUrl: './profile-component.html',
  styleUrl: './profile-component.css',
})
export class ProfileComponent implements OnInit {
  profile?: Profile;
  loading = true;
  editing = false;
  bioEdit = '';
  saving = false;
  saveMsg = '';

  constructor(private profileService: ProfileService) {}

  ngOnInit() {
    this.profileService.getProfile().subscribe({
      next: p => { this.profile = p; this.bioEdit = p.bio; this.loading = false; },
      error: () => this.loading = false,
    });
  }

  startEdit() { this.editing = true; this.saveMsg = ''; }

  saveBio() {
    this.saving = true;
    this.profileService.updateProfile({ bio: this.bioEdit }).subscribe({
      next: p => {
        this.profile = p;
        this.editing = false;
        this.saving = false;
        this.saveMsg = 'Saved!';
        setTimeout(() => this.saveMsg = '', 3000);
      },
      error: () => { this.saving = false; },
    });
  }
}
