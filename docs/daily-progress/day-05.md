
# Day 05 - Automated Testing

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
- Review test coverage and add failure scenarios.
- Add automated tests to GitHub Actions.
- Review Docker image security and size.
- Plan Kubernetes deployment.
