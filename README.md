Check CI/CD Status: 

[![Install](https://github.com/nogibjj/kim_seijung_project3_polars_stats/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/kim_seijung_project3_polars_stats/actions/workflows/install.yml)

[![Format](https://github.com/nogibjj/kim_seijung_project3_polars_stats/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/kim_seijung_project3_polars_stats/actions/workflows/format.yml)

[![Lint](https://github.com/nogibjj/kim_seijung_project3_polars_stats/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/kim_seijung_project3_polars_stats/actions/workflows/lint.yml)

[![Test](https://github.com/nogibjj/kim_seijung_project3_polars_stats/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/kim_seijung_project3_polars_stats/actions/workflows/test.yml)


# Mini-project #3
#### repo title: kim_seijung_project3_polars_stats
#### Author: Seijung Kim (sk591)

## Overview
This project uses Python scripts and the Polars library to load a dataset and generate different summary statistics for Exploratory Data Analysis. The generated data visualizations and PDF report should serve as useful tools to understand the dataset and its variables. You can load this repository to a codespace and make the devcontainer execute the Makefile that will run the following: install, format, lint, test. This project pushes the generated PDF report via CI/CD pipeline.

## Requirements

* Python script using Polars for descriptive statistics
* Read a dataset (CSV or Excel)
* Generate summary statistics (mean, median, standard deviation)
* Create at least one data visualization

## Deliverable
* Python script 
* CI/CD with badge
* Generated summary report (PDF or markdown) via CI/CD for extra credit

## About the Dataset
<img src="Amazon-Logo.webp" alt="Amazon Logo" width="200"/>

The `Amazon-Products-100k.csv` file used in this project is from the Amazon Products Sales Dataset 2023, obtained via Kaggle (). This is a product sales dataset scraped from the Amazon website from the year 2023, including a total of 142 item categories such as Fine Art, Dog Supplies, etc. The csv file was truncated to contain the first 100k rows of data from the original full products csv file due to the large size and memory limits for GitHub storage. The csv file consists of 10 columns with a row number and the following 9 variables.

| **Variable**      | **Description**                                                          |
|-------------------|--------------------------------------------------------------------------|
| `name`            | The name of the product                                                  |
| `main_category`   | The main category the product belongs to                                 |
| `sub_category`    | The sub-category the product belongs to                                  |
| `image`           | The image representing the product                                       |
| `link`            | The Amazon website reference link of the product                         |
| `ratings`         | The ratings given by Amazon customers for the product                    |
| `no of ratings`   | The number of ratings given to the product on Amazon                     |
| `discount_price`  | The discount price of the product                                        |
| `actual_price`    | The actual MRP (Maximum Retail Price) of the product                     |


## Python Scripts

Python Scripts
* In `script.py`, the script uses modules loaded from `lib.py`, and it will read data from a CSV file, perform statistical analysis, and generate a PDF report with the statistics and data visualizations about the dataset. The script will generate three images and a PDF report. This is sript is tested with `test_script.py` 
* In `lib.py`, the script creates helper functions to clean up the loaded dataset, generate all necessary statistics and the PDF report. This is sript is tested with `test_lib.py` 

## Instructions
1. Once you load this repository, wait for the installation of requirements.txt
2. You can run the following premade commands `make install`, `make format`, `make lint`, `make test`, or `make all`
3. Check whether you are able to display the statistics and data visualization when running `script.py` and the `project1.ipynb`
4. You can check the full statistics documentation as a PDF. Check `Amazon_Sales_Report.pdf`. For the images, check the `images` folder.
5. To check the full status of the CI/CD pipeline, navigate to the Actions tab of your repository on GitHub.

## Overview of Statistics
You can also view the same results in the PDF report `Amazon_Sales_Report.pdf`.



