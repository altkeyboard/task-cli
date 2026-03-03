# task-cli

A Python-based command-line tool that retrieves task data from a public REST API and presents structured, user-friendly output.

This project demonstrates:

- REST API consumption
- JSON parsing
- CLI argument parsing with `argparse`
- Structured HTTP error handling (including 404 handling)
- Explicit exit codes for automation scenarios
- Documentation lifecycle practices within a Git-managed repository

---

## Overview

`task-cli` accepts a task ID as a command-line argument, sends an HTTP request to a public API, parses the JSON response, and prints formatted output to the console.

The tool is intentionally designed to reflect backend documentation literacy and production-style CLI behavior.

---

## Features

- Fetch task data by ID
- Validate numeric input using `argparse`
- Gracefully handle HTTP errors
- Provide clear user-facing error messages
- Return structured exit codes
- Maintain full supporting documentation set

---

## Requirements

- Python 3.x

---

## Setup

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/Scripts/activate

