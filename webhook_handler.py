import hmac
import logging
import os
import threading

from fastapi import FastAPI, Request

WEBHOOK_SECRET = os.environ["WEBHOOK_SECRET"]

logger = logging.getLogger(__name__)
app = FastAPI()
build_thread = None


def build_site():
    os.system("bash site_deploy.sh")


@app.post("/site-deploy")
async def root(request: Request):
    body_hmac = hmac.new(bytes(WEBHOOK_SECRET, "utf-8"), digestmod="sha256")
    body_hmac.update(await request.body())
    calculated_signature = "sha256=" + body_hmac.hexdigest()

    github_signature = request.headers["x-hub-signature-256"]

    if github_signature != calculated_signature:
        logger.error("Request signature does not match")
        return {"error": "Signature invalid!"}

    global build_thread
    if build_thread and build_thread.is_alive():
        logger.warning("Build already in progress")
        return {"message": "Build already in progress.."}

    logger.info("Rebuilding the website")
    build_thread = threading.Thread(target=build_site)
    build_thread.start()
    return {"message": "Build started!"}
