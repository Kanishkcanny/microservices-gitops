# INC-001: WSL2 Cannot Access Docker Desktop Published Ports Through Localhost

## Environment
- OS: Windows with Ubuntu on WSL2
- Container Runtime: Docker Desktop
- Orchestration: Docker Compose
- Services: User Service and Order Service
- Ports: 8001 and 8002

## Issue
Both containers were running, but Ubuntu could not access the published ports using `127.0.0.1`.

## Investigation

### 1. Container status
Both services were running successfully.

### 2. Internal container communication
Order Service successfully accessed User Service using Docker service DNS:

`http://user-service:8001/health`

Result: HTTP 200 OK.

### 3. Windows host testing
Both services were accessible from Windows PowerShell:

- localhost:8001/health — HTTP 200
- localhost:8002/health — HTTP 200

### 4. Ubuntu localhost testing
Both requests failed with Connection refused:

- 127.0.0.1:8001
- 127.0.0.1:8002

### 5. WSL gateway testing
Retrieved the default gateway using:

`ip route show default`

Gateway observed during testing: `<WSL_WINDOWS_GATEWAY_IP>`

Both services responded successfully through this gateway.

### 6. End-to-end validation
Executed:

`curl http://<WSL_WINDOWS_GATEWAY_IP>:8002/orders/101/details`

Result: Successfully returned order information and associated user information.

## Findings
- Docker containers were healthy.
- Docker internal networking worked.
- Windows could access published container ports.
- Ubuntu localhost access failed.
- Ubuntu could access the services through the Windows host gateway.

The exact underlying cause of the localhost forwarding failure has not yet been established.

## Lessons Learned
- Verify container health before investigating networking.
- Understand Docker bridge networking and service DNS.
- Distinguish container-to-container communication from host-to-container communication.
- Test Windows and WSL connectivity separately.
- Discover the WSL gateway dynamically instead of hardcoding a temporary IP address.

## Status
Workaround verified. Root cause investigation remains open.
