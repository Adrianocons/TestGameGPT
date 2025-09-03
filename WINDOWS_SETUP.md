# Windows Setup Guide

This guide describes how to clone the repository, install dependencies, and run the game on Windows using PowerShell.

## Prerequisites
- Windows 10 or later
- [Git](https://git-scm.com/download/win)
- [Python 3.11+](https://www.python.org/downloads/windows/)

## Clone the repository
Open PowerShell and run:

```powershell
git clone <repo-url>
cd TestGameGPT
```

Replace `<repo-url>` with the URL of this repository.

## Create a virtual environment and install dependencies

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run the game

```powershell
python -m polythorogue.cli
```

## Run tests

```powershell
pytest -q
```
