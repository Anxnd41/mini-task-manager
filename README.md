# Mini Task Manager

A small Python project for testing the 4o4PR bug-detection workflow.

## Setup

From this directory, create a virtual environment and install the test
dependency:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the tests

```powershell
python -m pytest -q
```

The project contains one intentional bug in `complete_task`: it leaves a
completed task marked as incomplete. The test suite should fail until an agent
finds and fixes it.

## Test with 4o4PR

Open this folder as the repository under test, then use a prompt like:

```text
Run the pytest suite, identify the failing test, explain the root cause,
generate the smallest safe patch, apply it, and run the tests again.
Summarize the changed file and final test result.
```

After the fix, all five tests should pass.
