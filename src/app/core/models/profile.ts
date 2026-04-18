import { Purchase } from './purchase';

export interface Profile {
  id: number;
  username: string;
  email: string;
  bio: string;
  avatar: string | null;
  purchasedGames: Purchase[];
}
