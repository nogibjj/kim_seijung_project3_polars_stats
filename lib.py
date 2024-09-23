# Seijung Kim (sk591)
# This script has functions for data cleaning,
# generating descriptive stats, data viz, and a pdf

import os
import polars as pl
import matplotlib.pyplot as plt
from fpdf import FPDF


def load_dataset(data_path):
    """Read the CSV file using polars"""
    df = pl.read_csv(
        data_path,
        null_values=["null", ""],
        infer_schema_length=1000,
    )

    # Clean and convert 'ratings' by removing non-numeric values
    df = df.with_columns(
        pl.col("ratings").str.replace_all("[^0-9.]", "").cast(pl.Float64, strict=False)
    )

    # Clean and convert 'no_of_ratings' by removing non-numeric values
    df = df.with_columns(
        pl.col("no_of_ratings")
        .str.replace_all("[^0-9]", "")
        .cast(pl.Int64, strict=False)
    )

    # Clean and convert 'discount_price' and 'actual_price'
    df = df.with_columns(
        [
            pl.col("discount_price").str.replace_all("[₹,]", "").cast(pl.Float64),
            pl.col("actual_price").str.replace_all("[₹,]", "").cast(pl.Float64),
        ]
    )

    # Drop rows with missing (null) values
    df = df.drop_nulls()

    return df


def statistics(df):
    """Function to calculate statistics for each main_category"""

    # Group by main_category and calculate descriptive statistics using Polars
    stats = (
        df.group_by("main_category")
        .agg(
            [
                # ratings
                pl.col("ratings").mean().alias("mean_ratings"),
                pl.col("ratings").median().alias("median_ratings"),
                pl.col("ratings").std().alias("std_ratings"),
                # number of ratings
                pl.col("no_of_ratings").mean().alias("mean_no_of_ratings"),
            ]
        )
        .sort("main_category")
    )

    return stats


def category_counts(df):
    """Track counts of main_category and sub_category using Polars"""
    main_category_counts = (
        df.group_by("main_category")
        .agg(pl.col("main_category").count().alias("counts"))
        .sort("main_category")
    )

    sub_category_counts = (
        df.group_by("sub_category")
        .agg(pl.col("sub_category").count().alias("counts"))
        .sort("sub_category")
    )

    return main_category_counts, sub_category_counts


def visualization(df_input):
    """Draw bar graphs and histograms for each main_category"""

    # Ensure the images directory exists
    if not os.path.exists("images"):
        os.makedirs("images")

    if isinstance(df_input, pl.DataFrame):
        df_input = df_input.to_pandas()

    first_category = df_input["main_category"].unique()[0]
    subset = df_input[df_input["main_category"] == first_category]
    plt.figure(figsize=(10, 6))
    subset["ratings"].hist(bins=20, color="#93C572")
    plt.title(f"Ratings Distribution for {first_category}")
    plt.xlabel("Ratings")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"images/{first_category}_ratings_histogram.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    ratings_counts = df_input.groupby("main_category")["ratings"].count()
    ratings_counts.plot(kind="bar", color="#ADD8E6")
    plt.title("Counts of Ratings for Each Main Category")
    plt.xlabel("Main Category")
    plt.ylabel("Count of Ratings")
    plt.tight_layout()
    plt.savefig("images/main_category_ratings_count_bar_chart.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    mean_ratings = df_input.groupby("main_category")["ratings"].mean()
    mean_ratings.plot(kind="bar", color="#ADD8E6")
    plt.title("Mean Ratings for Each Main Category")
    plt.xlabel("Main Category")
    plt.ylabel("Mean Ratings")
    plt.tight_layout()
    plt.savefig("images/main_category_mean_ratings_bar_chart.png")
    plt.close()

    return "Visualizations saved."


def generate_pdf(
    main_category_counts, sub_category_counts, stats, pdf_path="Amazon_Sales_Report.pdf"
):
    """Generate Amazon sales dataset report and save it to PDF."""
    pdf = FPDF()

    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="Amazon Sales Dataset Report", ln=True, align="C")

    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Counts of Main Categories", ln=True, align="L")

    pdf.set_font("Arial", "", 10)
    for row in main_category_counts.rows():
        pdf.cell(100, 10, txt=f"{row[0]}", border=1)
        pdf.cell(100, 10, txt=f"{row[1]}", border=1, ln=True)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Counts of Sub Categories", ln=True, align="L")
    pdf.set_font("Arial", "", 10)
    for row in sub_category_counts.rows():
        pdf.cell(100, 10, txt=f"{row[0]}", border=1)
        pdf.cell(100, 10, txt=f"{row[1]}", border=1, ln=True)

    pdf.add_page()
    pdf.set_font("Arial", "B", 10)
    pdf.cell(200, 10, txt="Statistics for Ratings", ln=True)

    pdf.set_font("Arial", "", 10)
    for row in stats.rows():
        pdf.cell(100, 10, txt=f"Main Category: {row[0]}", ln=True)
        pdf.cell(
            100,
            10,
            txt=f"Mean Ratings: {row[1]}, Median: {row[2]}, Std: {row[3]}",
            ln=True,
        )
        pdf.cell(100, 10, txt=f"Mean No of Ratings: {row[4]}", ln=True)
        pdf.ln(10)

    pdf.output(pdf_path)
    print(f"PDF report generated: {pdf_path}")


def generate_markdown(
    main_category_counts, sub_category_counts, stats, md_path="Amazon_Sales_Report.md"
):
    """Generate Amazon sales dataset report markdown file."""
    with open(md_path, "w") as md:
        md.write("# Amazon Sales Dataset Report\n\n")

        md.write("## Counts of Main Categories\n")
        for row in main_category_counts.rows():
            md.write(f"- {row[0]}: {row[1]}\n")

        md.write("\n## Counts of Sub Categories\n")
        for row in sub_category_counts.rows():
            md.write(f"- {row[0]}: {row[1]}\n")

        # Add links to images for visualizations
        md.write("\n## Visualizations\n")
        md.write("### Ratings Distribution Histogram (First Category)\n")
        md.write(
            f"![Ratings Histogram](images/"
            f"{main_category_counts[0,0]}_ratings_histogram.png)\n"
        )
        md.write("### Bar Charts\n")
        md.write("![Ratings Count](images/main_category_ratings_count_bar_chart.png)\n")
        md.write("![Mean Ratings](images/main_category_mean_ratings_bar_chart.png)\n")

        # Add a table for statistics
        md.write("\n## Descriptive Statistics for Ratings and Number of Ratings\n")
        md.write(
            "| Main Category | Mean Ratings | Median Ratings | "
            "Std Dev | Mean No of Ratings |\n"
        )
        md.write(
            "| ------------- | ------------ | -------------- | "
            "------- | ------------------ |\n"
        )
        for row in stats.rows():
            md.write(
                f"| {row[0]} | {row[1]:.2f} | {row[2]:.2f} | "
                f"{row[3]:.2f} | {row[4]:.2f} |\n"
            )

    print(f"Markdown report generated: {md_path}")


if __name__ == "__main__":

    data_path = "Amazon-Products-100k.csv"

    # Load the dataset using polars
    df = load_dataset(data_path)

    # Perform statistics for each main category
    stats_df = statistics(df)

    main_category_counts, sub_category_counts = category_counts(df)

    # Generate visualizations
    print(visualization(df))

    # Generate the reports
    generate_pdf(
        main_category_counts,
        sub_category_counts,
        stats_df,
        pdf_path="Amazon_Sales_Report.pdf",
    )
    generate_markdown(
        main_category_counts,
        sub_category_counts,
        stats_df,
        md_path="Amazon_Sales_Report.md",
    )
