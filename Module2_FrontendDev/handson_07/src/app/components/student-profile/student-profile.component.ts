import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-student-profile',
  template: `
    <div class="container">
      <div class="profile-form-card">
        <h2 style="margin-bottom: 1.5rem; color: #0f172a;">Student Profile Form</h2>
        
        <form [formGroup]="profileForm" (ngSubmit)="onSubmit()">
          <div class="form-group">
            <label for="name">Full Name *</label>
            <input 
              type="text" 
              id="name" 
              formControlName="name" 
              placeholder="Enter full name"
            >
            <div *ngIf="profileForm.get('name')?.touched && profileForm.get('name')?.invalid" class="error-text">
              <span *ngIf="profileForm.get('name')?.errors?.['required']">Name is required.</span>
            </div>
          </div>

          <div class="form-group">
            <label for="email">Email Address *</label>
            <input 
              type="email" 
              id="email" 
              formControlName="email" 
              placeholder="Enter email address"
            >
            <div *ngIf="profileForm.get('email')?.touched && profileForm.get('email')?.invalid" class="error-text">
              <span *ngIf="profileForm.get('email')?.errors?.['required']">Email is required.</span>
              <span *ngIf="profileForm.get('email')?.errors?.['email']">Enter a valid email address.</span>
            </div>
          </div>

          <div class="form-group">
            <label for="semester">Current Semester (1 - 8) *</label>
            <input 
              type="number" 
              id="semester" 
              formControlName="semester" 
              placeholder="Semester number"
            >
            <div *ngIf="profileForm.get('semester')?.touched && profileForm.get('semester')?.invalid" class="error-text">
              <span *ngIf="profileForm.get('semester')?.errors?.['required']">Semester is required.</span>
              <span *ngIf="profileForm.get('semester')?.errors?.['min'] || profileForm.get('semester')?.errors?.['max']">
                Semester must be between 1 and 8.
              </span>
            </div>
          </div>

          <button type="submit" class="btn-primary" [disabled]="profileForm.invalid">
            Save Profile Changes
          </button>
        </form>

        <div *ngIf="submittedValue" style="margin-top: 1.5rem; background: #ecfdf5; padding: 1rem; border-radius: 6px; border: 1px solid #a7f3d0;">
          <h4 style="color: #047857;">Form Submitted Successfully:</h4>
          <pre style="font-size: 0.9rem; margin-top: 0.5rem;">{{ submittedValue | json }}</pre>
        </div>
      </div>
    </div>
  `
})
export class StudentProfileComponent {
  profileForm: FormGroup;
  submittedValue: any = null;

  constructor(private fb: FormBuilder) {
    this.profileForm = this.fb.group({
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      semester: [1, [Validators.required, Validators.min(1), Validators.max(8)]]
    });
  }

  onSubmit(): void {
    if (this.profileForm.valid) {
      this.submittedValue = this.profileForm.value;
    }
  }
}
