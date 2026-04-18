import { Game } from './game';

export interface Purchase {
  id: number;
  game: Game;
  price: number;
  purchasedAt: string;
}

export interface Review {
  id: number;
  username: string;
  rating: number;
  text: string;
  likes: number;
  dislikes: number;
  createdAt: string;
}
