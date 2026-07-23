import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-course-card',
  template: `
    <article class="course-card">
      <div class="card-header">
        <span class="course-code">{{ code }}</span>
        <span class="course-credits">{{ credits }} Credits</span>
      </div>
      <h3 style="font-size: 1.1rem; color: #0f172a; margin-bottom: 0.5rem;">{{ name }}</h3>
      <p style="font-weight: 600; color: #059669; font-size: 0.9rem;">Target Grade: {{ grade }}</p>
    </article>
  `
})
export class CourseCardComponent {
  @Input() name: string = '';
  @Input() code: string = '';
  @Input() credits: number = 0;
  @Input() grade: string = '';
}
