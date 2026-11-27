# Day 09 - Kustomize Overlays and Argo CD GitOps Deployment

## 1. Development Overlay
- Configured a separate Kustomize development overlay.
- Set Order Service replicas to 2.
- Set User Service replicas to 2.
- Kept the base Kubernetes manifests reusable.

## 2. Configuration Validation
- Rendered the development configuration using `kubectl kustomize`.
- Verified both Deployments had `replicas: 2`.
- Applied the configuration using `kubectl apply -k`.

## 3. Argo CD GitOps Integration
- Connected the GitHub repository to Argo CD.
- Configured automated synchronization.
- Verified automated sync, pruning and self-healing settings.
- Observed Argo CD reconciling the cluster with the Git repository.

## 4. Deployment Verification
- Argo CD application: `microservices-dev`.
- Sync Status: Synced.
- Health Status: Healthy.
- Order Service: 2/2 Ready.
- User Service: 2/2 Ready.
- Total application pods: 4 Running.

## 5. Git Version Control
- Committed the development replica configuration.
- Commit: `3b67d32`
- Message: `k8s: scale dev microservices to two replicas`
- Pushed changes to GitHub.
- Verified local branch is synchronized with `origin/main`.

## 6. Key Learnings
- Kustomize base and overlay configuration.
- Environment-specific replica management.
- Kubernetes declarative deployment.
- Argo CD automated synchronization.
- GitOps reconciliation and self-healing.
- Git commit and push workflow.

## 7. Next Steps
- Validate production overlay.
- Complete Argo CD production application configuration.
- Test GitOps-based deployment updates.
- Capture architecture and deployment screenshots.
- Prepare the final project demonstration.
