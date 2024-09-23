# Seijung Kim (sk591)
# This script uses functions created in lib.py to
# generate data analysis and visualizations.

from lib import (
    load_dataset,
    statistics,
    category_counts,
    visualization,
    generate_pdf,
    generate_markdown,
)


def main():
    data_path = "Amazon-Products-100k.csv"

    # Load the dataset
    df = load_dataset(data_path)

    # Perform statistics for each main category
    stats = statistics(df)

    # Get the counts of main and sub categories
    main_category_counts, sub_category_counts = category_counts(df)

    # Generate visualizations
    visualization(df)

    # Generate the PDF report
    generate_pdf(main_category_counts, sub_category_counts, stats)

    # Generate the Markdown report
    generate_markdown(main_category_counts, sub_category_counts, stats)


if __name__ == "__main__":
    main()
