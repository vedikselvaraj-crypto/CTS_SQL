# Hands-On 5: MongoDB — Document Modelling, CRUD & Aggregation

**Course**: Digital Nurture 5.0 - Python Full Stack Engineer Track  
**Module**: NoSQL Document Modeling, BSON Data Types, MongoDB Shell & Aggregation Pipelines  

---

## 📋 Overview

This hands-on exercise implements the NoSQL Course Feedback system (`college_nosql`) using MongoDB:
- **Document Modeling**: Schema-less BSON document structure embedding sub-documents and tag arrays.
- **CRUD Operations**: BSON data insertion, array query matching (`$elemMatch`), projection, `updateMany` with `$set` and `$push`, and document deletion.
- **Multi-Stage Aggregation Pipelines**: `$match`, `$group`, `$sort`, `$project`, `$round`, and `$unwind` array deconstruction.
- **Indexing & Performance Tuning**: Single-field and compound indexes, verifying `IXSCAN` index scan execution plans over `COLLSCAN` collection scans.

---

## 📁 Files Included

- `mongo_setup.js`: Database initialization (`college_nosql`), collection creation (`feedback`), and batch document population.
- `crud_operations.js`: MongoDB CRUD queries, array matching, field projections, and atomic updates.
- `aggregation_pipeline.js`: Analytical aggregation pipelines calculating course ratings and tag frequency leaderboards.
- `indexes.js`: Index creation, `explain('executionStats')` verification, and MongoDB Compass visual setup guide.
- `README.md`: Exercise documentation.

---

## 🚀 Execution Instructions via `mongosh`

```bash
# 1. Connect and initialize database
mongosh college_nosql mongo_setup.js

# 2. Run CRUD Operations
mongosh college_nosql crud_operations.js

# 3. Run Aggregation Pipelines
mongosh college_nosql aggregation_pipeline.js

# 4. Run Indexing Verification
mongosh college_nosql indexes.js
```
