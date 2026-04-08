import { Routes } from '@angular/router';
import {Home} from './features/home/home';
import { RegisterComponent } from './features/register-component/register-component';
import {CartComponent} from './features/cart-component/cart-component';
import {LibraryComponent} from './features/library-component/library-component';
import {LoginComponent} from './features/login-component/login-component';
import {GameDetailComponent} from './features/game-detail-component/game-detail-component';
import { Store } from './features/store/store';
import { Component } from '@angular/core';

 export const routes: Routes = [
  {path: '', component: Home, children: [

  ]},
  {path: 'login', component: LoginComponent},
  {path: 'cart', component: CartComponent},
  {path: 'register', component: RegisterComponent},
  {path: 'library', component: LibraryComponent},
  {path: 'games/:id', component: GameDetailComponent},
  {path: 'store', component: Store},
];




