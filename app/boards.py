"""
Leader boards api
"""
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

LEADER_BOARDS = APIRouter()


@LEADER_BOARDS.get('/', status_code=status.HTTP_200_OK)
async def all_leaders():
    data = {
        "msg": "this is initial api"
    }
    return JSONResponse(data)