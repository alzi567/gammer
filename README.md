# gammer

GAM generator.

Read all pixels from an image file and generate GAM cubes of the same color as the image pixels as a GAM project file.

## Installation

Install the package (preferably with pipx). The executable is called `gammer`.

## Example Usage

Get a GAP file from an image:

```
gammer image.jpg output.gap
```

Limit to a maximum size with the `--size` option:

```
gammer --size 20x20 image.jpg output.gap
```

Limit to a maximum size of 1400 pixels in total with the `--max-pixels` option (the image will be downscaled, preserving its original aspect ratio):

```
gammer --max-pixels 1400 image.jpg output.gap
```

Dismiss colors with the `--bw` flag:

```
gammer --bw --size 20x20 image.jpg output_gray.gap
```

Add margin of half the size of one "pixel" cube between each "pixel" using the `--margin` option:

```
gammer --margin 0.5 --bw --size 20x20 image.jpg output_gray.gap
```

Show usage screen:

```
gammer --help
```

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
