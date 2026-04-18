import { Genre } from './genre';

export interface Game {
  id: number;
  title: string;
  price: number;
  originalPrice?: number;
  discount?: number;
  description: string;
  image: string;
  rating: number;
  genre: Genre;
  developer?: string;
  releaseDate?: string;
  is_active: boolean;
}
