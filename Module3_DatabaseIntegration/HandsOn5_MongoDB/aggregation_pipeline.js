/**
 * =============================================================================
 * HANDS-ON 5 - TASK 3: MONGODB AGGREGATION PIPELINES (aggregation_pipeline.js)
 * Multi-stage pipelines ($match, $group, $sort, $project, $round, $unwind)
 * =============================================================================
 */

db = db.getSiblingDB('college_nosql');

print("\n================================================================================");
print("PIPELINE 1 & 2: Course Average Rating & Feedback Count for Semester '2022-ODD'");
print("================================================================================");

const courseRatingPipeline = [
  // Stage 1: Filter documents matching semester '2022-ODD'
  { 
    $match: { semester: "2022-ODD" } 
  },
  
  // Stage 2: Group by course_code, calculating avg rating & count
  { 
    $group: {
      _id: "$course_code",
      raw_avg_rating: { $avg: "$rating" },
      total_feedback_count: { $sum: 1 }
    } 
  },

  // Stage 3: Project fields, rename avg_rating to average_rating & round to 1 decimal
  { 
    $project: {
      _id: 0,
      course_code: "$_id",
      average_rating: { $round: ["$raw_avg_rating", 1] },
      total_feedback_count: 1
    } 
  },

  // Stage 4: Sort by average_rating descending
  { 
    $sort: { average_rating: -1 } 
  }
];

const courseRatingResults = db.feedback.aggregate(courseRatingPipeline).toArray();
printjson(courseRatingResults);


print("\n================================================================================");
print("PIPELINE 3: Tag Frequency Leaderboard ($unwind array deconstruction)");
print("================================================================================");

const tagLeaderboardPipeline = [
  // Stage 1: Deconstruct tags array into individual document instances
  { 
    $unwind: "$tags" 
  },

  // Stage 2: Group by tag name and count occurrences
  { 
    $group: {
      _id: "$tags",
      tag_count: { $sum: 1 }
    } 
  },

  // Stage 3: Project clean output shape
  { 
    $project: {
      _id: 0,
      tag: "$_id",
      tag_count: 1
    } 
  },

  // Stage 4: Sort by tag_count descending
  { 
    $sort: { tag_count: -1 } 
  }
];

const tagLeaderboardResults = db.feedback.aggregate(tagLeaderboardPipeline).toArray();
printjson(tagLeaderboardResults);
