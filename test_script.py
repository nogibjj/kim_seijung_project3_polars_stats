import os
from script import main


def test_main():

    # Run the main function to trigger the end-to-end process
    main()

    # Check if the images folder exists
    assert os.path.exists("images"), "Images folder should be created"

    # Check if the necessary image files have been generated
    assert os.path.exists(
        "images/main_category_ratings_count_bar_chart.png"
    ), "Bar chart should be saved"

    assert os.path.exists(
        "images/main_category_mean_ratings_bar_chart.png"
    ), "Mean ratings chart should be saved"

    first_category = "appliances"  # Ensure the correct first category is used
    assert os.path.exists(
        f"images/{first_category}_ratings_histogram.png"
    ), f"Histogram for {first_category} should be saved"

    # Check if the PDF has been generated
    assert os.path.exists("Amazon_Sales_Report.pdf"), "PDF should be generated"

    # Check if the markdown report has been generated
    assert os.path.exists(
        "Amazon_Sales_Report.md"
    ), "Markdown report should be generated"
