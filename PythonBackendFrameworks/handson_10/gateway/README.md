# API Gateway Service

**Port**: `5000`  

Stateless Flask API Gateway proxying external client traffic to target microservices:
- `/api/courses/*` -> Proxies to Course Service (Port 5001)
- `/api/students/*` -> Proxies to Student Service (Port 5002)
