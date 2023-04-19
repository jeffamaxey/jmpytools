# jmpytools

[![PyPI](https://img.shields.io/pypi/v/jmpytools.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/jmpytools.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/jmpytools)][python version]
[![License](https://img.shields.io/pypi/l/jmpytools)][license]

[![Read the documentation at https://jmpytools.readthedocs.io/](https://img.shields.io/readthedocs/jmpytools/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/jeffamaxey/jmpytools/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/jeffamaxey/jmpytools/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/jmpytools/
[status]: https://pypi.org/project/jmpytools/
[python version]: https://pypi.org/project/jmpytools
[read the docs]: https://jmpytools.readthedocs.io/
[tests]: https://github.com/jeffamaxey/jmpytools/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/jeffamaxey/jmpytools
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Features

    `jmpytools` is a python toolbox for easy and effective data exploration, 
    'and designed to work from Jupyter notebooks and interactively from python modules.


## Requirements  

 * asttokens
 * beautifulsoup4
 * black
 * boto3
 * coverage
 * darglint
 * dash
 * dash-bootstrap-components
 * dash-mantine-components
 * dask
 * flake8
 * flake8-bandit
 * flake8-bugbear
 * flake8-docstrings
 * flake8-rst-docstrings
 * fsspec
 * furo
 * geojson
 * google-cloud-storage
 * ipython
 * ipywidgets
 * isort
 * joblib
 * kaleido
 * livereload
 * matplotlib
 * mike
 * mistune
 * mkdocs
 * mkdocs-autorefs
 * mkdocs-include-markdown-plugin
 * mkdocs-material
 * mkdocs-material-extensions
 * mkdocstrings
 * mypy
 * myst-parser
 * nbconvert
 * networkx
 * numpy
 * openpyxl
 * pandas
 * pep8-naming
 * plotly
 * pre-commit
 * pre-commit-hooks
 * pyarrow
 * Pygments
 * pyinstaller
 * pyLDAvis
 * pyod
 * pyodbc
 * pypng
 * pyreadline
 * pytest
 * pytest-cov
 * pyupgrade
 * s3fs
 * safety
 * scikit-image
 * scikit-learn
 * scipy
 * seaborn
 * sphinx
 * sphinx-autobuild
 * sphinx-click
 * sqlalchemy
 * statsmodels
 * toml
 * toolz
 * tox
 * twine
 * typeguard
 * virtualenv
 * wheel
 * xdoctest
 * xlrd
 * xlsxwriter
 * xlwings

## Installation

You can install _jmpytools_ via [pip] from [PyPI]:

```console
$ pip install jmpytools
```

## Usage

Please see the [Command-line Reference] for details.

Features:  
 
* Intended Users:
  * Data Explorer is designed as a wrapper which helps users explore data more convenient and efficient.
* Data Importer:  
  * You can easily import data set from several files as well as databases into a Pandas or dask DataFrame.
* Data Exporter:
  * You can easily import data set from Pandas DataFrame or other data objects into several files or databases.
* Data Explorer:
  * Explore your data set quickly and efficiently using the DataExplorer:
    * Data Typing:
      * Check whether represented data types of Pandas is equal to the real data types occurring in the data
    * Data Health Check:

                  Check the health of the data set in order to detecting, describing and visualizing ...
                      ... the ammount of missing or invalid data vs. valid observations
                      ... the amount of duplicated data
                      ... the amount of invariant data

              -- Data Distribution:

                  Describing and visualizing statistical distribution of ...
                      ... categorical features
                      ... continuous features
                      ... date features

              -- Outlier Detection:

                  Analyze outliers or anomalies of continuous features using univariate and multivariate methods:
                      a) Univariate: Examines outlier values for each features separately using Inter-Quantile-Range (IQR)
                      b) Multivarite: Examines outliers for each possible feature pair combined using a bunch of different machine learning algorithms. For further information just look at the PyOD packages documentation, because it is used under the hood.

              -- Categorical Breakdown Statistics:

                  Descriptive statistics of continuous features grouped by values of each categorical feature in the data set:


              -- Correlation:

                  Correlation analysis of continuous features. For analyzing multi-collinearity there is a partial correlation method implemented. The differences between marginal and partial correlations are inspected by visualizing the differences of the coefficients in a heat map as well.

              -- Geo Statistics:

                  Descriptive statistics of continuous features grouped by values of each geo features in the data set. Additionally, there is a geo map (OpenStreetMap) generated to visualize statistical distribution.

              -- Text Analyzer:

                  Analyze potential text features and generate various numerical features from those

          - Data Visualizer:

              Visualize your data set very easily using Plot.ly an interactive visualization library under the hood. The DataVisualizer is an efficient wrapper to abstract the most important elements for data exploration:

                  -- Table Chart:
                      Visualize matrix (Pandas DataFrame) as an interactive table

                  -- Heat Map:
                      Visualize value range of continuous features as heat map

                  -- Geo Map:
                      Visualize statistics of categorical and continuous features as interactive OpenStreetMap

                  -- Contour Chart:
                      Visualize value ranges of at least two continuous features as contours

                  -- Pie Chart:
                      Visualize occurances of values of categorical features as an interactive pie chart

                  -- Bar Chart:
                      Visualize occurances of values of categorical features as an interactive bar chart

                  -- Histogram:
                      Visualize distribution of continuous features as an interactive histogram

                  -- Box-Whisker-Plot:
                      Visualize descriptive statistics of continuous features as an interactive box-whisker-plot

                  -- Violin Chart:
                      Visualize descriptive statistics of continuous features as an interactive violin chart

                  -- Parallel Category Chart:
                      Visualize relationships interactively between categorical features especially, but it can also be used for mixed relations between values of categorical and continuous features by using brushing as well.

                  -- Parallel Coordinate Chart:
                      Visualize relationships interactively between ranges of continuous features especially, but it can also be used for mixed relations between values of categorical and ranges of continuous features as well.

                  -- Scatter Chart:
                      Visualize values of continuous features interactively.

                  -- Scatter3D Chart:
                      Visualize values of three continuous features in one chart interactively.

                  -- Joint Distribution Chart:
                      Visualize values of two continuous features interactively, including contours and histogram for each continuous feature.

                  -- Ridgeline Chart:
                      Visualize changes in distribution of continuous features on certain time steps separately.

                  -- Line Chart:
                      Visualize distribution after certain time steps as an interactive line chart.

                  -- Candlestick Chart:
                      Visualize descriptive statistics for each time steps as an interactive candlestick chart.

                  -- Dendrogram:
                      Visualize hierarchical clusters.

                  -- Silhoutte Chart:
                      Visualize partitioned clusters.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_jmpytools_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/jeffamaxey/jmpytools/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/jeffamaxey/jmpytools/blob/main/LICENSE
[contributor guide]: https://github.com/jeffamaxey/jmpytools/blob/main/CONTRIBUTING.md
[command-line reference]: https://jmpytools.readthedocs.io/en/latest/usage.html
