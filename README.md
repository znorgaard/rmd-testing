[![Knit Tests](https://github.com/znorgaard/rmd-testing/actions/workflows/knit_tests.yml/badge.svg)](https://github.com/znorgaard/rmd-testing/actions/workflows/knit_tests.yml)

## Overview

This repository is intended to be a simple example of how to automate testing rmarkdown report generation for a variety of inputs.

## System Dependencies

Knitting the minimal_example.Rmd file in this repository requires:
- [R, Tested with version 4.2.0](https://cran.r-project.org/src/base/R-4/)
- [Pandoc](https://pandoc.org/installing.html) which is included with [RStudio installs](https://www.rstudio.com/products/rstudio/download/)

To use the python test suite of the html report content, poetry is used.
- [Poetry installation](https://python-poetry.org/docs/#installation)

## R Package Dependencies
There are two R packages required: `rmarkdown` and `flexdashboard`

In an R console you can install these with:

```R
install.packages("rmarkdown", "flexdashboard")
```

## Python Dependencies

The python dependencies used in testing are defined in `pyproject.toml` and can be installed with poetry.
In the repository root directory run:

```R
poetry install
```
