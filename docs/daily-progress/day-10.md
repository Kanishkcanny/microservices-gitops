## Argo CD Self-Healing Test

### Objective
Verify that Argo CD automatically restores
Kubernetes resources when manual changes cause drift.

### Test Procedure
1. Checked production Order Service replicas.
2. Manually scaled deployment from 1 to 0.
3. Argo CD detected configuration drift.
4. Argo CD automatically restored replicas to 1.

### Verification

Command:
kubectl get deployment order-service -n microservices-prod

Result:
READY: 1/1

Argo CD:
microservices-dev: Synced / Healthy
microservices-prod: Synced / Healthy

### Outcome
Self-healing successfully verified in the local Kind cluster.
Dev environment remained unaffected.
