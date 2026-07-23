/**
 * =============================================================================
 * HANDS-ON 5 - TASK 1: MONGODB DATABASE & COLLECTION SETUP (mongo_setup.js)
 * Target Database: college_nosql
 * Target Collection: feedback
 * =============================================================================
 */

// Switch to target database
db = db.getSiblingDB('college_nosql');

// Clean collection if exists
db.feedback.drop();

// -----------------------------------------------------------------------------
// Step 61, 62, 63: Insert 11 Feedback Documents (Including schema-less document)
// -----------------------------------------------------------------------------
db.feedback.insertMany([
  {
    student_id: 1,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 5,
    comments: "Excellent teaching! Data structures concepts were explained clearly.",
    tags: ["challenging", "well-structured", "good-examples"],
    submitted_at: ISODate("2022-11-30T10:15:00Z"),
    attachments: [
      { filename: "ds_notes.pdf", size_kb: 240 }
    ]
  },
  {
    student_id: 2,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 4,
    comments: "Great assignments, but exams were quite tough.",
    tags: ["challenging", "interactive", "heavy-workload"],
    submitted_at: ISODate("2022-11-30T11:20:00Z"),
    attachments: [
      { filename: "assignment1_solution.pdf", size_kb: 512 }
    ]
  },
  {
    student_id: 5,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 2,
    comments: "Pace of lectures was too fast for beginners.",
    tags: ["fast-paced", "challenging"],
    submitted_at: ISODate("2022-12-01T09:00:00Z"),
    attachments: []
  },
  {
    student_id: 1,
    course_code: "CS102",
    semester: "2022-ODD",
    rating: 5,
    comments: "Database normalization module was very practical.",
    tags: ["practical", "well-structured", "great-faculty"],
    submitted_at: ISODate("2022-12-02T14:30:00Z"),
    attachments: [
      { filename: "erd_diagram.png", size_kb: 1024 }
    ]
  },
  {
    student_id: 5,
    course_code: "CS102",
    semester: "2022-ODD",
    rating: 5,
    comments: "Outstanding explanation of SQL query execution plans.",
    tags: ["practical", "good-examples"],
    submitted_at: ISODate("2022-12-02T15:45:00Z"),
    attachments: [
      { filename: "query_optimization.pdf", size_kb: 380 }
    ]
  },
  {
    student_id: 3,
    course_code: "EC101",
    semester: "2021-EVEN",
    rating: 4,
    comments: "Lab sessions provided good hands-on experience.",
    tags: ["hands-on", "interactive"],
    submitted_at: ISODate("2021-05-20T16:00:00Z"),
    attachments: [
      { filename: "circuit_lab_report.pdf", size_kb: 650 }
    ]
  },
  {
    student_id: 6,
    course_code: "EC101",
    semester: "2021-EVEN",
    rating: 3,
    comments: "Course material requires update for modern electronics.",
    tags: ["outdated-slides", "interactive"],
    submitted_at: ISODate("2021-05-21T10:10:00Z"),
    attachments: []
  },
  {
    student_id: 4,
    course_code: "ME101",
    semester: "2023-ODD",
    rating: 1,
    comments: "Thermodynamics concepts were poorly explained.",
    tags: ["difficult", "unclear-grading"],
    submitted_at: ISODate("2023-11-28T08:30:00Z"),
    attachments: [
      { filename: "thermo_complaint.txt", size_kb: 15 }
    ]
  },
  {
    student_id: 7,
    course_code: "ME101",
    semester: "2023-ODD",
    rating: 2,
    comments: "Heavy workload and tough grading criteria.",
    tags: ["heavy-workload", "difficult"],
    submitted_at: ISODate("2023-11-29T12:00:00Z"),
    attachments: []
  },
  {
    student_id: 8,
    course_code: "CS103",
    semester: "2022-ODD",
    rating: 4,
    comments: "Good introduction to Java OOP concepts.",
    tags: ["well-structured", "good-examples"],
    submitted_at: ISODate("2022-12-05T17:15:00Z"),
    attachments: [
      { filename: "oop_patterns.pdf", size_kb: 420 }
    ]
  },
  // Step 63: Intentionally omit attachments field to demonstrate schema-less nature
  {
    student_id: 9,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 4,
    comments: "Feedback submitted via mobile app without file attachments.",
    tags: ["challenging", "mobile-submission"],
    submitted_at: ISODate("2022-12-06T19:00:00Z")
  }
]);

// -----------------------------------------------------------------------------
// Step 64: Verify document count
// -----------------------------------------------------------------------------
const count = db.feedback.countDocuments();
print("================================================================================");
print(`[SUCCESS] Feedback collection initialized! Total Documents Inserted: ${count}`);
print("================================================================================");
