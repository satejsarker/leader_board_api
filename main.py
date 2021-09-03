"""
Leader boards API
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.boards import LEADER_BOARDS, USER

description = """
Leader Boards API helps you do awesome stuff. 🚀

## Items

You can **view leader boards sores **.

## add or reduce leader scores
## add user
"""
origins = [
    "http://localhost",
    "http://localhost:8080",
]
app = FastAPI(
    title="Leader Boards API",
    description=description,
    contact={
        "name": "satej sarker ",
        "email": "onesatej@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }

)

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True,
                   allow_methods=["*"], allow_headers=["*"], )

# including boards api
app.include_router(router=LEADER_BOARDS, prefix="/boards")
app.include_router(router=USER, prefix="/users")