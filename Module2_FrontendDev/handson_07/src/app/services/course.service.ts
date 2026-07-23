import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map } from 'rxjs';

export interface Course {
  id: number;
  name: string;
  code: string;
  credits: number;
  grade: string;
}

@Injectable({
  providedIn: 'root'
})
export class CourseService {
  private apiUrl = 'https://jsonplaceholder.typicode.com/posts?_limit=5';

  constructor(private http: HttpClient) {}

  getCourses(): Observable<Course[]> {
    return this.http.get<any[]>(this.apiUrl).pipe(
      map(posts => posts.map((post, index) => ({
        id: post.id,
        name: post.title,
        code: `CS${(index + 1) * 101}`,
        credits: (index % 2 === 0) ? 4 : 3,
        grade: 'A'
      })))
    );
  }
}
