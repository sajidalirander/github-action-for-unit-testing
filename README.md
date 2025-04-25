# What need to know about GitHub Actions?

Refer to the [file](.github/workflows/test.yml) which is going to discussed in detail. 

## Step-by-step guide

`name`: This is just a human-readable name for the workflow. It can be seen as the workflow title in GitHub Actions.
```yaml
name: Run Unit Tests
```

`on`: – When should this workflow run?
```yaml
on:
  push:
    branches:
      - '**'
  pull_request:
```
* `push`: Triggers when someone pushes code to any branch ('**' means “all branches”).

* `pull_request`: Triggers when a pull request is created or updated (good for testing before merging code).

This ensures tests run automatically every time someone pushes or opens a PR.

`jobs`: – A job is a set of steps that run on a GitHub server
```yaml
jobs:
  test:
    runs-on: ubuntu-latest
```
* The job is called `test`.
* `runs-on: ubuntu-latest`: The virtual machine (runner) GitHub will use. This runner comes with Python, Git, pip, and other dependencies.

`steps`: – Actions to perform inside this job

1. Checkout the repo
    ```yaml
    - name: Checkout the repository
      uses: actions/checkout@v3
    ```
    This downloads GitHub repository into the runner so it can access your code.

2. Set up Python
    ```yaml
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
          python-version: '3.10'

    ```
    * This tells GitHub to install and use `Python 3.10` for all following steps.
    * It can be changed to another version if needed.

3. Install dependencies 
    ```yaml
    - name: Install dependencies
      run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

    ```
    * Upgrades pip
    * Installs everything listed in requirements.txt — such as pytest
    * Without this step, tests might fail because libraries like pytest will not be available.

4. Run the tests
    ```yaml
    - name: Run tests
      run: |
          export PYTHONPATH=.
          pytest
    ```
    This does the actual testing:

    * `export PYTHONPATH=.` tells Python to include current folder in the import path, so it can find imported modules/pakages.
    * `pytest` runs all the test files (files like `test_*.py` inside the `test/` folder).

