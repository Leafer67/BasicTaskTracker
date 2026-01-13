from __future__ import annotations
from typing import Annotated, Literal
from pathlib import Path

import typer
import sqlite3
from datetime import datetime
import json

DB_PATH = Path("tasktracker.db")

app = typer.Typer()

def get_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_db():
    db = sqlite3.connect(DB_PATH)
    db.executescript(Path("schema.sql").read_text(encoding="utf-8"))
    return db

@app.command()
def add(name: Annotated[str, typer.Argument(help="Name of the task")]):
    """
    Add a task to the database
    """

    db = get_db()
    db.execute("INSERT INTO tasks(description) VALUES (?)", (name,))
    db.commit()

    print(f"Added {name}")

@app.command()
def update(id: Annotated[int, typer.Argument(help="Id of the task to update")], name: Annotated[str, typer.Argument(help="New name for the task")]):
    """
    Update the name of the task
    """

    db = get_db()
    cursor = db.execute("UPDATE tasks SET description=?, updated_at=? WHERE id=?", (name, get_datetime(), id))

    if cursor.rowcount == 0:
        print(f"Couldn't find task with id: {id}")
    else:
        db.commit()
        print(f"Updated {id} to {name}")

@app.command()
def delete(id: Annotated[int, typer.Argument(help="Id of the task to delete")]):
    """
    Delete the task
    """

    db = get_db()
    cursor = db.execute("DELETE FROM tasks WHERE id=?", (id,))

    if cursor.rowcount == 0:
        print(f"Couldn't find task with id: {id}")
    else:
        db.commit()
        print(f"Deleted task {id}")

@app.command()
def mark_in_progress(id: Annotated[int, typer.Argument(help="Id of the task to mark as in progress")]):
    """
    Mark the task as in progress
    """

    db = get_db()
    cursor = db.execute("UPDATE tasks SET status='in-progress', updated_at=? WHERE id=?", (get_datetime(), id))

    if cursor.rowcount == 0:
        print(f"Couldn't find task with id: {id}")
    else:
        db.commit()
        print(f"Marked task {id} as in-progress")

@app.command()
def mark_done(id: Annotated[int, typer.Argument(help="Id of the task to mark as done")]):
    """
    Mark the task as done
    """

    db = get_db()
    cursor = db.execute("UPDATE tasks SET status='done', updated_at=? WHERE id=?", (get_datetime(), id))

    if cursor.rowcount == 0:
        print(f"Couldn't find task with id: {id}")
    else:
        db.commit()
        print(f"Marked task {id} as done")

@app.command()
def list(
    json_: Annotated[bool, typer.Option("--json", help="Format the output to JSON", is_flag=True)] = False,
    filter: Annotated[Literal["todo", "in-progress", "done"],
    typer.Argument(help="Optional filter")] = None
    ):
    """
    List all tasks and informations about them
    """

    db = get_db()
    if filter is None:
        res = db.execute("SELECT * FROM tasks ORDER BY id ASC")
    else:
        res = db.execute("SELECT * FROM tasks WHERE status=? ORDER BY id ASC", (filter,))
    
    rows = res.fetchall()

    if json_:
        data = []
        for id_, name, status, created_at, updated_at in rows:
            data.append({
                "id": id_,
                "name": name,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            })

        print(json.dumps(data, indent=2))
        return

    print(f"{'ID':>3}  {'NAME':<30}  {'STATUS':<12}  {'CREATED':<19}  {'UPDATED':<19}")
    print("-" * 91)

    for id_, name, status, created_at, updated_at in rows:
        print(
            f"{id_:>3}  "
            f"{name:<30}  "
            f"{status:<12}  "
            f"{created_at:<19}  "
            f"{updated_at or '-':<19}"
        )

if __name__ == "__main__":
    app()
