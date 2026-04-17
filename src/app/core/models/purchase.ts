// purchase.ts
import { Game } from "./game";

export interface Purchase {
  id: number;
  userId: number;
  game: Game;
  price: number;
  purchasedAt: string; 
}
