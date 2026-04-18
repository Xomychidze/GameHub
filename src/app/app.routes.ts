import { Routes } from '@angular/router';
import { Home } from './features/home/home';
import { Store } from './features/store/store';
import { LoginComponent } from './features/login-component/login-component';
import { RegisterComponent } from './features/register-component/register-component';
import { CartComponent } from './features/cart-component/cart-component';
import { LibraryComponent } from './features/library-component/library-component';
import { GameDetailComponent } from './features/game-detail-component/game-detail-component';
import { ProfileComponent } from './features/profile-component/profile-component';
import { authGuard } from './core/interceptors/auth.guard';

export const routes: Routes = [
  { path: '',        component: Home },
  { path: 'store',   component: Store },
  { path: 'games/:id', component: GameDetailComponent },
  { path: 'login',   component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'cart',    component: CartComponent,    canActivate: [authGuard] },
  { path: 'library', component: LibraryComponent, canActivate: [authGuard] },
  { path: 'profile', component: ProfileComponent, canActivate: [authGuard] },
  { path: '**',      redirectTo: '' },
];
