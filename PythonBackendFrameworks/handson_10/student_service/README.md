# Student Microservice

**Port**: `5002`  
**Database**: `student_service.db` (SQLite)  

Autonomous Flask service managing student profiles and course enrollments. Performs inter-service HTTP requests to Course Service (5001) to verify course existence, handling 503 Service Unavailable when Course Service is offline.
