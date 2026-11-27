# Day 07 - Kubernetes Deployment with Kustomize

## 1. Kubernetes Manifests
- Created Kubernetes base manifests for the `microservices` namespace.
- Created Deployment and ClusterIP Service resources for User Service and Order Service.
- Configured container images, ports, health probes, CPU and memory requests and limits.
- Created the Kustomize configuration using `kustomization.yaml`.
- Organized Kubernetes resources under `kubernetes/base/`.

## 2. Configuration and Deployment
- Validated manifests using Kubernetes server-side dry run.
- Applied Kubernetes resources using `kubectl apply -k`.
- Confirmed namespace, Deployments and Services were created successfully.
- Verified the resources were unchanged on a subsequent apply.

## 3. Deployment Verification
- Kubernetes context: `kind-microservices-gitops`
- Namespace: `microservices`
- User Service: 1/1 Running.
- Order Service: 1/1 Running.
- Both ClusterIP Services created successfully.
- Both Deployments available.

## 4. Service-to-Service Communication
- Verified Kubernetes DNS resolution for `order-service`.
- Confirmed TCP connectivity on port `8002`.
- Tested `GET /orders/101/details` from a temporary curl pod.
- Received HTTP `200 OK`.
- Verified the returned JSON contained order and associated user details.
- Confirmed User Service API requests in application logs.

## 5. Cleanup
- Deleted the temporary `curl-test` pod.
- Confirmed both application pods remained healthy.
- Verified both Deployments and Services remained available.

## 6. Validation Results
- Kubernetes manifest validation: Passed.
- Kustomize build/apply: Passed.
- User Service: 1/1 Running.
- Order Service: 1/1 Running.
- Order details endpoint: HTTP 200 OK.
- Kubernetes DNS resolution: Passed.
- Inter-service communication: Passed.
- Temporary diagnostic pod cleanup: Completed.

## 7. Key Learnings
- Kubernetes Deployments and Services.
- ClusterIP service discovery.
- Kubernetes internal DNS.
- Kustomize base configuration.
- Server-side dry-run validation.
- Readiness and liveness probes.
- Inter-service communication.
- Troubleshooting using logs and temporary diagnostic pods.

## 8. Next Steps
- Create development and production Kustomize overlays.
- Review image tagging and deployment versioning.
- Configure rolling updates and rollback strategies.
- Integrate Kubernetes deployment into the CI/CD pipeline.
- Plan GitOps deployment using Argo CD.
