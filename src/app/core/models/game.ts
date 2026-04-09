import {Genre} from './genre';

export interface Game {
  id: number;
  title: string;
  price: number;
  description: string;
  image: string;
  rating: number;
  genre: Genre;
}
