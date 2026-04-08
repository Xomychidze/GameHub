import { Component } from '@angular/core';
import { Footer } from '../../shared/footer/footer';
import { Header } from '../../shared/header/header';

@Component({
  selector: 'app-library-component',
  imports: [Footer, Header],
  templateUrl: './library-component.html',
  styleUrl: './library-component.css',
})
export class LibraryComponent {

}
