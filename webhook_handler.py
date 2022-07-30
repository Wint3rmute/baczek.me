import os
import threading

from fastapi import FastAPI, Request

app = FastAPI()


build_thread = None


def build_site():
    os.system("bash site_deploy.sh")


@app.post("/site-deploy")
async def root(request: Request):
    print(dir(request))
    print(vars(request))
    print(await request.body())
    global build_thread
    if build_thread and build_thread.is_alive():
        return {"message": "Build already in progress.."}

    build_thread = threading.Thread(target=build_site)
    build_thread.start()
    return {"message": "Build started!"}
