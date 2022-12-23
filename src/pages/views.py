from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

view = APIRouter()
templates = Jinja2Templates(directory="templates")

# Registert Page
@view.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", context={"request": request})


# Lottery Page
@view.get("/lottery", response_class=HTMLResponse)
async def lottery(request: Request):
    return templates.TemplateResponse("lottery.html", context={"request": request})


# Health check
@view.get("/healthz")
async def health() -> JSONResponse:
    """Health check

    Returns:
        JSONResponse: Status message.
    """
    return JSONResponse({"status": "Success", "message": "I'm alive!"})
