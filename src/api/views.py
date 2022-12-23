import json
import logging

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from utils.lottery import Lottery

view = APIRouter()


@view.post("/register")
async def register(request: Request) -> JSONResponse:
    post_data = json.loads(await request.body())

    try:
        lottery = Lottery()
        lottery.register(name=post_data["user_name"])
        return JSONResponse(
            {"status": "success", "title": "報名成功", "message": "您已成功報名抽獎！"}
        )
    except:
        return JSONResponse(
            {"status": "error", "title": "很抱歉", "message": "報名失敗，請重新再試！"}
        )


@view.get("/unregister")
async def unregister(name: str) -> JSONResponse:
    try:
        lottery = Lottery()
        lottery.unregister(name=name)
        return JSONResponse(
            {"status": "success", "title": "刪除成功", "message": "成功刪除抽獎者"}
        )
    except:
        return JSONResponse(
            {"status": "error", "title": "很抱歉", "message": "操作失敗，請重新再試！"}
        )


@view.get("/lottery")
async def lottery() -> JSONResponse:
    try:
        lottery = Lottery()
        pairs = lottery.start()
        logging.info(pairs)
        result = "抽將結果：\n"
        for receiver, sender in pairs.items():
            result += f"{receiver} <- {sender}\n"
        return JSONResponse({"status": "success", "title": "抽獎結果", "message": result})
    except:
        return JSONResponse(
            {"status": "error", "title": "很抱歉", "message": "抽獎失敗，請重新再試！"}
        )
