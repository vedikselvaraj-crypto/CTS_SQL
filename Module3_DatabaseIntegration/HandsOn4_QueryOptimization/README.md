# Hands-On 4: Query Optimization — Indexes, EXPLAIN & the N+1 Problem

**Course**: Digital Nurture 5.0 - Python Full Stack Engineer Track  
**Module**: Database Performance Tuning, Indexing Strategies & ORM N+1 Mitigation  

---

## 📋 Overview

This hands-on exercise analyzes database query execution plans using `EXPLAIN` / `EXPLAIN ANALYZE`, creates single-column B-Tree, Composite UNIQUE, and Partial indexes to eliminate Sequential Scans, and benchmarks the ORM **N+1 Query Problem** using an executable Python script comparing 13 lazy-loaded queries vs. 1 eager JOIN query.

---

## 📁 Files Included

- `optimization.sql`: Baseline query plans, index creation DDL, partial indexes, and optimized query execution plans.
- `n_plus_one.py`: Executable Python benchmark script comparing N+1 lazy loading vs. SQL JOIN eager loading.
- `README.md`: Exercise documentation.

---

## 🚀 Execution & Benchmark Instructions

### 1. Execute SQL Index Optimization Script
```bash
psql -U postgres -d college_db -f optimization.sql
```

### 2. Run N+1 Python Benchmark
```bash
cd HandsOn4_QueryOptimization
python n_plus_one.py
```

**Expected Benchmark Output**:
```text
================================================================================
N+1 QUERY BENCHMARK RESULTS
================================================================================
Approach 1 (Bad N+1 Lazy Loading): 13 database round-trips | Execution Time: 0.0142s
Approach 2 (Optimized Eager JOIN):  1 database round-trip  | Execution Time: 0.0018s
--------------------------------------------------------------------------------
Performance Gain: Approach 2 was 7.89x FASTER and saved 12 database round-trips!
================================================================================
```
