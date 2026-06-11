# ToDoMVC Playwright Mini Project

UI end-to-end tests for the React version of TodoMVC using Python, Pytest, and Playwright.

## Application Under Test

`https://todomvc.com/examples/react/dist/`

## Tech Stack

- Python
- Pytest
- Playwright
- `pytest-playwright`

## What This Project Covers

The test suite validates common TodoMVC user flows, including:

- creating a single todo
- creating multiple todos
- preventing empty or whitespace-only todos
- allowing duplicate todos
- marking todos as completed
- filtering active and completed todos
- clearing completed todos
- removing a todo item

## Project Structure

```text
.
├── README.md
├── requirements.txt
└── tests
    ├── test_clear_completed.py
    ├── test_completed_todo.py
    ├── test_create_todo.py
    ├── test_filter.py
    └── test_remove_todo.py
```

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install the test dependencies:

```bash
pip install pytest playwright pytest-playwright
```

3. Install Playwright browsers:

```bash
playwright install
```

## Run The Tests

Run the full suite:

```bash
pytest
```

Run a single test file:

```bash
pytest tests/test_create_todo.py
```

Run with headed browser mode:

```bash
pytest --headed
```

## Notes

- These tests depend on the public TodoMVC demo site being available.
- Because the target application is hosted externally, test failures can sometimes be caused by site or network issues rather than local code changes.
