from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from typing import Optional
import sqlite3
import datetime as dt

from utils.generate_prefix import generate_prefix
from utils.get_short_links import get_short_links_by_tuple

connection = sqlite3.connect('ShortLinks.db', check_same_thread=False)
cursor = connection.cursor()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hi! Give me full link to http://localhost:8000/create_link?link=..."}


@app.get("/p/{postfix}")
def home(postfix: str):
    if postfix:
        cursor.execute("SELECT * FROM short_links")
        links = get_short_links_by_tuple(cursor.fetchall())

        if postfix in links:
            return RedirectResponse(links[postfix])

        return {"message": "Fail.. Link not found"}

    return {"message": "Hi! Give me short link"}


@app.get("/create_link/")
def create_short_link(link: Optional[str] = None):
    if link != None:
        cursor.execute("SELECT * FROM short_links")
        links = get_short_links_by_tuple(cursor.fetchall())

        prefix = generate_prefix()
        while prefix in links:
            prefix = generate_prefix()

        if "https" not in link or "http" not in link:
            link = "http://" + link

        cursor.execute("INSERT INTO short_links VALUES (?, ?)", (prefix, link))
        connection.commit()

        return {"link": f"http://localhost:8000/p/{prefix}"}

    return {"message": "Give me full link"}
