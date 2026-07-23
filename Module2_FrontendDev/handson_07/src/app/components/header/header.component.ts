import { Component } from '@angular/core';

@Component({
  selector: 'app-header',
  template: `
    <header class="site-header">
      <a routerLink="/" class="site-title">Student Portal (Angular)</a>
      <nav class="nav-links">
        <a routerLink="/" routerLinkActive="active" [routerLinkActiveOptions]="{exact: true}">Courses</a>
        <a routerLink="/profile" routerLinkActive="active">Student Profile</a>
      </nav>
    </header>
  `
})
export class HeaderComponent {}
