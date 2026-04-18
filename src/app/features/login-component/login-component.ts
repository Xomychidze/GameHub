import { Component } from '@angular/core';
import { RouterLink, Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { AuthService } from '../../core/services/auth.service';

@Component({
  selector: 'app-login-component',
  standalone: true,
  imports: [FormsModule, RouterLink, CommonModule],
  templateUrl: './login-component.html',
  styleUrl: './login-component.css',
})
export class LoginComponent {
  username = '';
  password = '';
  errorMessage = '';
  isLoading = false;

  constructor(private authService: AuthService, private router: Router) {}

  onLogin() {
    if (!this.username.trim() || !this.password) return;
    this.isLoading = true;
    this.errorMessage = '';
    this.authService.login({ username: this.username, password: this.password }).subscribe({
      next: () => { this.isLoading = false; this.router.navigate(['/']); },
      error: err => {
        this.isLoading = false;
        this.errorMessage = err.error?.error || err.error?.detail || 'Invalid username or password.';
      },
    });
  }
}
