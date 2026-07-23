/**
 * =============================================================================
 * HANDS-ON 5 - TASK 2: MONGODB CRUD OPERATIONS (crud_operations.js)
 * Demonstrates READ queries, Array matching, Projections, Updates & Deletes
 * =============================================================================
 */

db = db.getSiblingDB('college_nosql');

print("\n--- 1. READ: All feedback documents where rating is 5 ---");
const fiveStarFeedback = db.feedback.find({ rating: 5 }).toArray();
printjson(fiveStarFeedback);

print("\n--- 2. READ: CS101 feedback where tags array contains 'challenging' ---");
const challengingCS101 = db.feedback.find({ 
  course_code: "CS101", 
  tags: "challenging" 
}).toArray();
printjson(challengingCS101);

print("\n--- 3. READ: Projection (student_id, course_code, rating only; exclude _id) ---");
const projectedFeedback = db.feedback.find(
  {}, 
  { student_id: 1, course_code: 1, rating: 1, _id: 0 }
).toArray();
printjson(projectedFeedback);

print("\n--- 4. UPDATE: Set needs_review = true for documents with rating < 3 ---");
const updateReviewResult = db.feedback.updateMany(
  { rating: { $lt: 3 } },
  { $set: { needs_review: true } }
);
print(`[UPDATE RESULT] Matched: ${updateReviewResult.matchedCount}, Modified: ${updateReviewResult.modifiedCount}`);

print("\n--- 5. UPDATE: Push 'reviewed' tag into tags array where needs_review is true ---");
const pushTagResult = db.feedback.updateMany(
  { needs_review: true },
  { $push: { tags: "reviewed" } }
);
print(`[PUSH TAG RESULT] Matched: ${pushTagResult.matchedCount}, Modified: ${pushTagResult.modifiedCount}`);

print("\n--- 6. DELETE: Delete all feedback documents where semester is '2021-EVEN' ---");
const deleteResult = db.feedback.deleteMany({ semester: "2021-EVEN" });
print(`[DELETE RESULT] Deleted Documents: ${deleteResult.deletedCount}`);

print(`\n[FINAL DOCUMENT COUNT]: ${db.feedback.countDocuments()}`);
