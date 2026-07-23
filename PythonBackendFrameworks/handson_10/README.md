# Hands-On 10: Microservices Architecture — Concepts & Decomposition

**Course**: Digital Nurture 5.0 - Python Full Stack Engineer Track  
**Module**: Distributed Systems, Service Bounded Contexts & API Gateway Pattern  

---

## 🏛️ Service Decomposition Matrix

In this module, the monolith Course Management API is decomposed into autonomous, database-isolated microservices:

| Service Name | Responsibility | Endpoints Owned | Database Owned | Port |
| :--- | :--- | :--- | :--- | :--- |
| **Course Service** | Manages Department & Course catalog domain | `/api/courses/` | `course_service.db` | `5001` |
| **Student Service** | Manages Student profiles & Course Enrollments | `/api/students/` | `student_service.db` | `5002` |
| **API Gateway** | Reverse-proxies client traffic to target services | Proxy `/api/*` | None (Stateless) | `5000` |
| *Auth Service* | Identity & JWT Token generation | `/api/auth/` | `auth_service.db` | `5003` |
| *Notification Service* | Async Email Notifications | Event Listener | `notification.db` | Event-Driven |

---

## 📁 Directory Structure

```text
handson_10/
├── README.md                           # Master Microservices Architecture Guide
├── course_service/                     # Independent Course Service (Port 5001)
│   ├── README.md
│   ├── requirements.txt
│   ├── app.py
│   └── models.py
├── student_service/                    # Independent Student Service (Port 5002)
│   ├── README.md
│   ├── requirements.txt
│   ├── app.py
│   └── models.py
└── gateway/                            # API Gateway Proxy (Port 5000)
    ├── README.md
    ├── requirements.txt
    └── app.py
```

---

## 🔀 Synchronous (HTTP) vs. Asynchronous (Message Queue) Communication

### 1. Synchronous HTTP Inter-Service Communication (Rest API / gRPC)
- **Mechanism**: Student Service executes an HTTP GET call directly to Course Service (`http://localhost:5001/api/courses/{id}/`).
- **Trade-offs**:
  - **Pros**: Immediate response consistency, simple implementation.
  - **Cons**: **Tight Coupling & Cascading Failures**. If Course Service suffers an outage, Student Service's enrollment endpoint fails instantly (`503 Service Unavailable`).

### 2. Asynchronous Event-Driven Communication (RabbitMQ / Apache Kafka)
- **Mechanism**: Services publish domain events (`CourseCreated`, `StudentEnrolled`) to a message broker. Subscribing services consume events asynchronously.
- **Trade-offs**:
  - **Pros**: **High Resilience & Decoupling**. If Course Service goes down, messages buffer safely in RabbitMQ queues without crashing Student Service.
  - **Cons**: **Eventual Consistency**. Data synchronization across services is delayed by milliseconds/seconds.

#### When to use RabbitMQ vs. Kafka?
- **RabbitMQ**: Ideal for traditional background jobs, command routing, complex topic exchanges, and low-latency task processing.
- **Apache Kafka**: Ideal for high-throughput event streaming, audit logging, real-time analytics, and event sourcing where message replay is required.

---

## 🚀 How to Launch the Microservices Cluster

Launch each component in separate terminal windows:

```bash
# Terminal 1: Course Service (Port 5001)
cd handson_10/course_service
python app.py

# Terminal 2: Student Service (Port 5002)
cd handson_10/student_service
python app.py

# Terminal 3: API Gateway (Port 5000)
cd handson_10/gateway
python app.py
```

### End-to-End Inter-Service Enrollment Test
Execute via API Gateway (`Port 5000`):
```bash
POST http://localhost:5000/api/students/1/enroll
Content-Type: application/json

{
  "course_id": 101
}
```
1. Gateway forwards request to **Student Service** (`5002`).
2. Student Service executes HTTP call to **Course Service** (`5001`) to verify course existence.
3. If Course Service is offline, Student Service catches `ConnectionError` and returns `503 Service Unavailable`.
