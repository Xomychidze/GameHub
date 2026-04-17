// review.ts
export interface Review {
  id: number;
  userId: number;   // лучше чем просто user
  gameId: number;
  rating: number;
  text: string;
  created_at: string;
}
