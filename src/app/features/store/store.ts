import { Component } from '@angular/core';
import { Footer } from '../../shared/footer/footer';
import { Header } from '../../shared/header/header';

@Component({
  selector: 'app-store',
  imports: [Footer, Header],
  templateUrl: './store.html',
  styleUrl: './store.css',
})
export class Store {

}
