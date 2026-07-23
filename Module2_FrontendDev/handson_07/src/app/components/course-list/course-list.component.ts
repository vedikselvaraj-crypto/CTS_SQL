import { Component, OnInit } from '@angular/core';
import { CourseService, Course } from '../../services/course.service';

@Component({
  selector: 'app-course-list',
  template: `
    <div class="container">
      <h2 style="margin-bottom: 1rem;">Course Directory</h2>

      <div class="search-box">
        <input 
          type="text" 
          class="search-input" 
          placeholder="Search courses by name or code..."
          [(ngModel)]="searchTerm"
        >
      </div>

      <div *ngIf="loading" class="loading-spinner">
        Loading courses from server...
      </div>

      <div *ngIf="!loading && filteredCourses.length === 0" style="text-align: center; color: #64748b; padding: 2rem;">
        No courses found matching "{{ searchTerm }}".
      </div>

      <div *ngIf="!loading && filteredCourses.length > 0" class="course-grid">
        <app-course-card
          *ngFor="let course of filteredCourses; trackBy: trackByCourseId"
          [name]="course.name"
          [code]="course.code"
          [credits]="course.credits"
          [grade]="course.grade">
        </app-course-card>
      </div>
    </div>
  `
})
export class CourseListComponent implements OnInit {
  courses: Course[] = [];
  searchTerm: string = '';
  loading: boolean = true;

  constructor(private courseService: CourseService) {}

  ngOnInit(): void {
    this.loading = true;
    this.courseService.getCourses().subscribe({
      next: (data) => {
        this.courses = data;
        this.loading = false;
      },
      error: (err) => {
        console.error('Failed to load courses:', err);
        this.loading = false;
      }
    });
  }

  get filteredCourses(): Course[] {
    if (!this.searchTerm.trim()) {
      return this.courses;
    }
    const term = this.searchTerm.toLowerCase();
    return this.courses.filter(c => 
      c.name.toLowerCase().includes(term) || 
      c.code.toLowerCase().includes(term)
    );
  }

  trackByCourseId(index: number, course: Course): number {
    return course.id;
  }
}
