import sys
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/todos"

def get_todo(todo_id: int) -> dict:
    resp = requests.get(f"{BASE_URL}/{todo_id}", timeout=10)
    resp.raise_for_status()
    return resp.json()

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python app.py <todo_id>")
        print("Example: python app.py 1")
        sys.exit(1)

    try:
        todo_id = int(sys.argv[1])
    except ValueError:
        print("Error: <todo_id> must be an integer.")
        sys.exit(1)

    try:
        data = get_todo(todo_id)
    except requests.HTTPError as e:
        status = e.response.status_code if e.response is not None else None
        if status == 404:
            print(f"Task {todo_id} was not found (404). Try an ID between 1 and 200.")
            sys.exit(2)
        print(f"Request failed (HTTP {status}): {e}")
        sys.exit(1)
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        sys.exit(1)

    print(f"Task ID: {data.get('id')}")
    print(f"Title: {data.get('title')}")
    print(f"Completed: {data.get('completed')}")

if __name__ == "__main__":
    main()