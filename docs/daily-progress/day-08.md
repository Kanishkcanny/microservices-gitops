# Day 08 - Kubernetes Kustomize Overlays

## 1. Development Overlay
- Created development Kustomize overlay.
- Referenced shared Kubernetes base manifests.
- Configured User Service replicas: 1.
- Configured Order Service replicas: 1.

## 2. Production Overlay
- Created production Kustomize overlay.
- Reused the same base manifests.
- Configured User Service replicas: 2.
- Configured Order Service replicas: 2.

## 3. Validation
- Rendered development manifests successfully.
- Rendered production manifests successfully.
- Development server-side dry run: Passed.
- Production server-side dry run: Passed.
- No changes applied to the running cluster.

## 4. Key Learnings
- Kustomize base and overlays.
- Environment-specific configuration.
- Replica count customization.
- Reusing Kubernetes manifests.
- Server-side dry-run validation.

## 5. Next Steps
- Review image tagging and versioning.
- Integrate Argo CD.
- Configure GitOps synchronization.
