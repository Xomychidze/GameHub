import { Component } from '@angular/core';
import { Footer } from '../../shared/footer/footer';
import { Header } from '../../shared/header/header';

@Component({
  selector: 'app-cart-component',
  imports: [Footer, Header],
  templateUrl: './cart-component.html',
  styleUrl: './cart-component.css',
})
export class CartComponent {

}
