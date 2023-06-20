# Cryptocurrency address generator (FAST API)
## Table of contents:
1. [Prerequisites](#prereqs)
2. [Installation](#install)
3. [Usage](#usage)


## 1. Prerequisites <a name="prereqs"/>
1. [Python](https://www.python.org/) (version 3.11)


## 2. Installation <a name="setup"/>
### 2.1. Create & and source virtual environment:
    ```
    $VENV_DIR=".venv"
    python -m venv $VENV_DIR
    source $VENV_DIR/bin/activate
    ```

### 2.2. Install poetry:
    ```
    pip install poetry
    ```

### 2.3. Install dependancies
    ```
    poetry install
    ```

### 2.4. Install git hooks
    ```
    pre-commit install
    ```

### 2.5. Create env variables
    Create `.env` file in project root, add line `PRIVATE_KEY="your private key"` and save.
    Or, create environmental variable manuallu using `export PRIVATE_KEY="your private key"`

### 2.5. Happy coding!


## 3. Usage <a name="usage"/>
    Run application:
    ```
    python src/app.py
    ```

    Run tests:
    ```
    pytest tests/
    ```
