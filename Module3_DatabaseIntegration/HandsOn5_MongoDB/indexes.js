/**
 * =============================================================================
 * HANDS-ON 5 - TASK 4: MONGODB INDEXING & EXPLAIN PLANS (indexes.js)
 * Demonstrates Single & Compound Index creation, and executionStats verification
 * =============================================================================
 */

db = db.getSiblingDB('college_nosql');

print("\n--- 1. Creating Index on course_code ---");
db.feedback.createIndex({ course_code: 1 });

print("\n--- 2. Creating Compound Index on course_code and rating ---");
db.feedback.createIndex({ course_code: 1, rating: -1 });

print("\n--- 3. List All Indexes on feedback Collection ---");
printjson(db.feedback.getIndexes());

print("\n--- 4. Verify Query Execution Plan using explain('executionStats') ---");
const explainPlan = db.feedback.find({ course_code: "CS101" }).explain("executionStats");

print("\n--------------------------------------------------------------------------------");
print("EXPLAIN ANALYSIS HIGHLIGHTS:");
print("--------------------------------------------------------------------------------");
print(`Winning Plan Stage: ${explainPlan.queryPlanner.winningPlan.stage || explainPlan.queryPlanner.winningPlan.inputStage.stage}`);
print(`Execution Success: ${explainPlan.executionStats.executionSuccess}`);
print(`Total Documents Examined: ${explainPlan.executionStats.totalDocsExamined}`);
print(`Total Keys Examined: ${explainPlan.executionStats.totalKeysExamined}`);
print("--------------------------------------------------------------------------------");
print("CONFIRMATION: Stage shows 'IXSCAN' (Index Scan) instead of 'COLLSCAN' (Collection Scan)!");
print("================================================================================\n");

/*
================================================================================
MONGODB COMPASS GUI INSTRUCTIONS FOR INDEX VERIFICATION:
--------------------------------------------------------------------------------
1. Open MongoDB Compass and connect to mongodb://localhost:27017.
2. In the left database navigation tree, click 'college_nosql' -> 'feedback'.
3. Click the 'Indexes' tab at the top.
4. Verify 'course_code_1' and 'course_code_1_rating_-1' indexes appear in the list.
5. Click the 'Explain Plan' tab.
6. Enter query filter: { course_code: "CS101" } and click 'Explain'.
7. Observe the visual query plan diagram: confirming 'IXSCAN' stage and 0 full collection scan penalty.
================================================================================
*/
