# grb_infra

Infrastructure deployment repository for the [grb_amateur](https://github.com/eguefif/grb_amateur) project.

## Overview

This repository contains the infrastructure configuration for deploying the grb_amateur application stack using Docker Swarm. It manages the deployment of multiple services including the backend API, alert system, and nginx reverse proxy.

## Services

The stack consists of three main services:

- **nginx**: Reverse proxy and web server (ports 80/443)
- **backend**: Main application backend API
- **alertsys**: Alert notification system

## Prerequisites

- Docker with Swarm mode enabled
- [just](https://github.com/casey/just) command runner
- Docker secrets configured:
  - `grb-amateur.space.pem`: SSL certificate
  - `private.key`: SSL private key
  - `backend-secrets`: Backend service secrets
  - `alertsys-secrets`: Alert system secrets

## Usage

### Starting the stack

```bash
just start-services
```

This deploys the entire stack to Docker Swarm using `docker stack deploy`.

### Stopping the stack

```bash
just stop-services
```

Removes the stack from Docker Swarm.

### Updating services

Update the alert system:
```bash
just update-alertsys
```

Update the backend:
```bash
just update-backend
```

## Network

All services communicate via the `grb_default` network.

## Docker Images

Services pull images from Docker Hub:
- `eguefif/grb-amateur:nginx-latest`
- `eguefif/grb-amateur:backend-latest`
- `eguefif/grb-amateur:alertsys-latest`
