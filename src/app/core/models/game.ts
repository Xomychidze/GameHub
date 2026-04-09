import { Genre } from './genre';

export interface Game {
  id: number;
  title: string;
  price: number;
  description: string;
  image: string;
  rating: number;
  genre: Genre;
  // опциональные поля — добавляй по мере необходимости:
  originalPrice?: number;
  discount?: number;
  developer?: string;
  releaseDate?: string;
  screenshots?: string[];
}
