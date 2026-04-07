import {Genre} from './genre';

export interface Game {
  id: number;
  title: string;
  price: number;
  description: string;
  cover_image: string;
  rating: number;
  genre: Genre;
}
