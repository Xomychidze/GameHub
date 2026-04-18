import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink, Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { AuthService } from '../../core/services/auth.service';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [FormsModule, RouterLink, CommonModule],
  templateUrl: './register-component.html',
  styleUrl: './register-component.css',
})
export class RegisterComponent {
  username = '';
  email = '';
  password = '';
  confirmPassword = '';
  errorMessage = '';
  isLoading = false;

  constructor(private authService: AuthService, private router: Router) {}

  onRegister() {
    if (this.password !== this.confirmPassword) {
      this.errorMessage = 'Passwords do not match.';
      return;
    }
    if (this.password.length < 8) {
      this.errorMessage = 'Password must be at least 8 characters.';
      return;
    }
    this.isLoading = true;
    this.errorMessage = '';
    this.authService.register({ username: this.username, email: this.email, password: this.password }).subscribe({
      next: () => { this.isLoading = false; this.router.navigate(['/']); },
      error: err => {
        this.isLoading = false;
        this.errorMessage =
          err.error?.username?.[0] || err.error?.email?.[0] || err.error?.password?.[0] ||
          err.error?.error || 'Registration failed.';
      },
    });
  }
}
