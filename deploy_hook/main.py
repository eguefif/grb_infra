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
    if not verify:
        return "not authorized"
    command = "docker service update --update-delay=10s --with-registry-auth --image eguefif/grb-amateur:alertsys-latest grb_alertsys".split(" ")
    print("Update alertsys")
    subprocess.run(command)
    return "ok"

@app.get("/deploy/backend")
def deploy_backend(verify: VerifyDep):
    if not verify:
        return "not authorized"

    command = "docker service update --update-delay=10s --with-registry-auth --image eguefif/grb-amateur:backend-latest grb_backend".split(" ")
    print("Update backend")
    subprocess.run(command)
    return "ok"

@app.get("/deploy/frontend")
def deploy_backend(verify: VerifyDep):
    if not verify:
        return "not authorized"

    command = "docker service update --update-delay=10s --with-registry-auth --image eguefif/grb-amateur:nginx-latest grb_nginx".split(" ")
    print("Update frontend")
    subprocess.run(command)
    return "ok"
