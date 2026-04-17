import { Game } from "./game";

export interface User {
  id: number;
  username: string;
  library: Game[];   // вместо lib
  token: string;
  role: 'admin' | 'user';
}

