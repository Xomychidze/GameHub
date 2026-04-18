import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Profile } from '../models/profile';

@Injectable({ providedIn: 'root' })
export class ProfileService {
  private readonly API = 'http://localhost:8000/api';
  constructor(private http: HttpClient) {}

  getProfile(): Observable<Profile> {
    return this.http.get<Profile>(`${this.API}/profile/`);
  }

  updateProfile(data: { bio?: string }): Observable<Profile> {
    return this.http.put<Profile>(`${this.API}/profile/`, data);
  }
}
