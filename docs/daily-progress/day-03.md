# Day 03 – Dockerization and Container Health Checks

## Completed
- Created Dockerfile for User Service.
- Created Dockerfile for Order Service.
- Configured Docker Compose for both microservices.
- Created a shared Docker bridge network.
- Configured service-to-service communication using Docker DNS.
- Added Docker health checks to both services.
- Configured Order Service to wait until User Service is healthy.
- Successfully built and started both containers.

## Validation
- User Service health endpoint: HTTP 200
- Order Service health endpoint: HTTP 200
- User listing endpoint: Passed
- Order listing endpoint: Passed
- Order details endpoint: Passed
- Both Docker containers: Healthy
- End-to-end service communication: Successful

## Key Learnings
- Dockerfile instructions and image building.
- Docker Compose multi-container orchestration.
- Docker bridge networking and service DNS.
- Container health checks.
- `depends_on` with `condition: service_healthy`.
- Difference between container startup and application readiness.

## Troubleshooting
Previously investigated WSL-to-Docker Desktop localhost connectivity. Both services were verified through the Windows host gateway as a workaround. The underlying localhost forwarding issue remains under investigation.

## Next Steps
- Add automated tests.
- Improve Dockerfiles with non-root users.
- Implement GitHub Actions CI/CD.
- Deploy services to Kubernetes.
