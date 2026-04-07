import { Component } from '@angular/core';
import {Footer} from './../../shared/footer/footer';
import {Header} from './../../shared/header/header';
@Component({
  selector: 'app-home',
  imports: [Header,
    Footer
  ],
  templateUrl: './home.html',
  styleUrl: './home.css',
})
export class Home {

}
