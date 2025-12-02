from typing import Annotated, Optional
from fastapi import FastAPI, Depends, Request, Header
import subprocess
import os

app = FastAPI()

SECRET = os.getenv("DEPLOY_SECRET")

def verify_origin(
        request: Request,
        x_signature: Annotated[Optional[str], Header()] = None
):
    if x_signature == SECRET:
        return True
    return False

VerifyDep = Annotated[bool, Depends(verify_origin)]

@app.get("/deploy/alertsys")
def deploy_alertsys(verify: VerifyDep):
    print("Receive trigger for alertsys deploy")
    if not verify:
        return "not authorized"
    command = "docker service update --update-delay=10s --with-registry-auth --image eguefif/grb-amateur:alertsys-latest grb_alertsys".split(" ")
    print("Update alertsys")
    ret = subprocess.run(command)
    if ret.returncode == 0:
        print("Alertsys deploy OK")
        return "ok"
    else:
        print("Alertsys deploy Failure")
        return "error"

@app.get("/deploy/backend")
def deploy_backend(verify: VerifyDep):
    print("Receive trigger for backend deploy")
    if not verify:
        return "not authorized"

    command = "docker service update --update-delay=10s --with-registry-auth --image eguefif/grb-amateur:backend-latest grb_backend".split(" ")
    print("Update backend")
    ret = subprocess.run(command)
    if ret.returncode == 0:
        print("Alertsys deploy OK")
        return "ok"
    else:
        print("Alertsys deploy Failure")
        return "error"

@app.get("/deploy/frontend")
def deploy_backend(verify: VerifyDep):
    print("Receive trigger for frontend deploy")
    if not verify:
        return "not authorized"

    command = "docker service update --update-delay=10s --with-registry-auth --image eguefif/grb-amateur:nginx-latest grb_nginx".split(" ")
    print("Update frontend")
    ret = subprocess.run(command)
    if ret.returncode == 0:
        print("Alertsys deploy OK")
        return "ok"
    else:
        print("Alertsys deploy Failure")
        return "error"
