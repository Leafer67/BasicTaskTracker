# BasicTaskTracker

BasicTaskTracker is a **simple command-line task tracker** written in Python.  
It was built as a **learning and portfolio project** over a few days, with the goal of practicing:

- Python CLI design  
- SQL basics  
- SQLite integration  
- Clean project structure  

The project is intentionally simple and focuses on fundamentals rather than features.

---

## Features

- Create tasks with a description  
- List tasks  
- Update task status  
- Filter tasks by status  
- Store data persistently using SQLite  
- Optional JSON output for scripting / automation  

---

## Tech stack

- **Python**
- **Typer** (for the CLI)
- **SQLite** (via `sqlite3`)
- **Raw SQL** (no ORM)

---

## Why this project

This project was made to:
- Learn how to mix Python and SQL in a real project  
- Understand how SQLite works (schema, inserts, updates, queries)  
- Practice building a clean CLI with Typer  
- Have a small but complete tool to showcase in a portfolio  

It is not meant to replace existing task managers or be feature-complete.

---

## Usage (overview)

The tool is used entirely from the command line.

Typical actions include:
- Initializing the database  
- Adding tasks  
- Listing tasks (optionally filtered)  
- Updating task status  
- Outputting results as human-readable text or JSON  

Use `--help` on any command to see available options.
<img width="1473" height="298" alt="image" src="https://github.com/user-attachments/assets/69fbbc9b-bf48-4710-9db2-556466536342" />


