"""
================================================================================
API GATEWAY REVERSE PROXY (app.py)
================================================================================
Runs on Port 5000.
Central ingress entry point proxying HTTP requests to backend microservices.
================================================================================
"""

import requests
from flask import Flask, request, Response

app = Flask(__name__)

COURSE_SERVICE_HOST = "http://localhost:5001"
STUDENT_SERVICE_HOST = "http://localhost:5002"


def proxy_request(target_url: str) -> Response:
    """Helper method forwarding HTTP request to target downstream service."""
    try:
        resp = requests.request(
            method=request.method,
            url=target_url,
            headers={k: v for k, v in request.headers if k.lower() != 'host'},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False,
            timeout=5.0
        )
        # Exclude transfer-encoding headers to avoid HTTP chunking issues
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(k, v) for k, v in resp.raw.headers.items() if k.lower() not in excluded_headers]
        
        return Response(resp.content, resp.status_code, headers)

    except requests.exceptions.ConnectionError:
        return Response(
            '{"error": "Service Unavailable", "message": "Target downstream microservice is offline"}',
            status=503,
            mimetype='application/json'
        )


@app.route('/api/courses/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/api/courses/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def courses_proxy(path: str):
    """Proxies /api/courses/* traffic to Course Microservice (Port 5001)."""
    target = f"{COURSE_SERVICE_HOST}/api/courses/{path}"
    if request.query_string:
        target += f"?{request.query_string.decode('utf-8')}"
    return proxy_request(target)


@app.route('/api/students/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/api/students/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def students_proxy(path: str):
    """Proxies /api/students/* traffic to Student Microservice (Port 5002)."""
    target = f"{STUDENT_SERVICE_HOST}/api/students/{path}"
    if request.query_string:
        target += f"?{request.query_string.decode('utf-8')}"
    return proxy_request(target)


@app.route('/')
def gateway_health():
    return {
        "gateway": "API Gateway Active",
        "routes": {
            "/api/courses/*": "Course Service (Port 5001)",
            "/api/students/*": "Student Service (Port 5002)"
        }
    }, 200


if __name__ == '__main__':
    print("[INFO] Starting API Gateway Proxy on Port 5000...")
    app.run(host='0.0.0.0', port=5000, debug=True)
