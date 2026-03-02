\# task-cli



A Python-based command-line tool that retrieves task data from a public REST API and presents structured, user-friendly output.



This project demonstrates:

\- REST API consumption

\- JSON parsing

\- CLI argument validation

\- Structured HTTP error handling (including 404 handling)

\- Documentation lifecycle practices within a Git-managed repository



---



\## Overview



`task-cli` accepts a task ID as a command-line argument, sends an HTTP request to a public API, parses the JSON response, and prints formatted output to the console.



---



\## Features



\- Fetch task data by ID

\- Validate numeric input

\- Gracefully handle HTTP errors

\- Provide clear user-facing error messages

\- Maintain full supporting documentation



---



\## Requirements



\- Python 3.x



---



\## Setup



Create and activate a virtual environment:



```bash

python -m venv venv

source venv/Scripts/activate

