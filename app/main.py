from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from .repository import CommentRepository

app = FastAPI()

templates = Jinja2Templates(directory="templates")
repository = CommentRepository()

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/comments_list")
def get_comments(request: Request):
    comments = reversed(repository.get_all())
    return templates.TemplateResponse("comments.html", {"request": request, "comments": comments})

@app.get("/add_comment")
def get_comment(request: Request):
    return templates.TemplateResponse("add_comment.html", {"request": request})

@app.post("/add_comment")
def post_comment(comment: str = Form(), type: str = Form()):
    repository.save({"text": comment, "type": type})
    return RedirectResponse("/comments_list", status_code=303)


