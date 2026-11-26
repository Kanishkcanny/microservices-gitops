
# Day 05 - Automated Testing

## Docker Hub Publishing

- Created Docker Hub repositories for user-service and order-service.
- Configured GitHub Actions repository secrets.
- Added Docker Hub authentication to the CI workflow.
- Built and tagged Docker images using the Git commit SHA.
- Published both `latest` and commit-specific tags.
- Verified both images on Docker Hub.
- Confirmed linux/amd64 architecture.

## Verification

- User Service image: Published successfully.
- Order Service image: Published successfully.
- GitHub Actions workflow: Successful.
- Automated API tests: 12 passed.

## Completed
- Created User Service API tests.
- Created Order Service API tests.
- Tested root and health endpoints.
- Tested successful and unsuccessful resource lookups.
- Mocked User Service responses to test Order Service independently.
- Tested successful order and user data integration.
- Tested handling of a missing associated user.
- Configured pytest test execution.

## Validation
- User Service tests: 5 passed.
- Order Service tests: 7 passed.
- Total automated tests: 12 passed.
- Test execution: Passed.
- Runtime: 0.36 seconds.

## Warning
- Starlette reports a deprecation warning for its current HTTPX TestClient integration.
- Tests pass; dependency compatibility cleanup is pending.

## Next Steps
- Review test coverage and add more failure scenarios.
- Resolve the HTTPX TestClient deprecation warning.
- Review Docker image security and size.
- Create Kubernetes deployment and service manifests.
- Deploy both microservices to Kubernetes.
- Validate service-to-service communication.
