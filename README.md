# gammer

GAM generator

## Setup for development

Make sure that the following tools are installed *globally*:

* pipx: https://github.com/pypa/pipx
  ```Shell
  pip install pipx
  ```
* pdm: https://github.com/pdm-project/pdm
  ```Shell
  pipx install pdm
  ```
* pre-commit: https://github.com/pre-commit/pre-commit
  ```Shell
  pipx install pre-commit
  ```

### Linux / WSL / Git Bash

We provide a script that perform all the necessary setup steps for you. Simply run

```Shell
./setup.sh
```
## Pre-commit hook

The package `pre-commit` is used to check for consistent style regarding whitespace, sorting of
imports etc. When `pre-commit` complains during a commit, usually `pre-commit` has already fixed
the findings for you - all you have to do is to *add* these modified files anew to the git index and
attempt to commit again - this time it should work.

## Install

Simply run

```Shell
pdm install
```

## Run the module

### As an application

Execute by calling the module directly:

    pdm run gammer

### Use as a module

Just import it:

    from gammer import ...

If you decide (and this is recommended) to explicitly name your public items in the module's
`__init__.py`, you should only try to import these published items.

## Unit tests

Unit tests are located under the parent directory `test/`. `pytest` will discover your test files if they are named like `test_*`. Any function named `test_*` will be executed by pytest.

Because the unit tests are not located within the module source files, the module has to be locatable via an `import` statement - in other words, the module must be installed, otherwise the tests will not find the unit test files, but not the module itself to be tested.

So be sure that the module is installed - in development, this will typically be via:

    pdm install

Note: this step is already performed by the `setup.sh` script.

Then run the tests:

    pdm run pytest -vv -o log_cli=true

Or, run with a coverage report:

    # collect coverage info while testing
    pdm run pytest --cov=gammer -vv -o log_cli=true

    # for a quick tabular summary report
    pdm run coverage report

    # for an in-depth, browsable HTML report
    pdm run coverage html

## Documentation

If you wish to write your code documentation and publish it as a gitlab page,
follow this step-by-step tutorial: https://bmd-se.code.siemens.io/gitlab-pages-quick-guide/
(Repository: https://code.siemens.com/bmd-se/gitlab-pages-quick-guide).

## Maintainer

Contact Alexander Eck-Zimmer (alexander.eckzimmer@gmail.com)
