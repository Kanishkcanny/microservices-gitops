# INC-002: Kubernetes Pod Restarts

## Issue
Kubernetes pods showed a restart count of 2.

## Investigation
- Checked Kubernetes events.
- Observed SandboxChanged events.
- Inspected Order Service pod details.
- Previous container exit code: 255.
- Previous container reason: Unknown.
- Previous logs showed successful health checks.
- Logs ended with a graceful "Shutting down" message.

## Findings
The evidence is consistent with Kubernetes recreating pod sandboxes
during a Docker/Kind environment restart.

No application-level exception was found in the available logs.

## Verification
- Order Service: Running and Ready.
- User Service: Running and Ready.
- All four pods: 1/1 Ready.

## Outcome
Services are operational.
The exact underlying trigger for the sandbox recreation
was not established.
