# Sales Dashboard Project

This project contains a data exploration and preprocessing notebook for sales data, plus a Streamlit dashboard that visualizes business KPIs and answers key business questions.

## Project Structure

- `train.ipynb` - Jupyter notebook that:
  - loads `train.csv`
  - inspects and cleans the data
  - drops unnecessary columns and duplicates
  - converts date fields to datetime
  - engineers features such as order year/month/day, shipping time, log sales, category/regional averages, and shipping days
  - saves the cleaned dataset to `cleaned_train.csv`
  - writes a Streamlit dashboard app to `app.py`
- `train.csv` - original raw sales dataset loaded by the notebook.
- `cleaned_train.csv` - cleaned dataset produced by the notebook.
- `app.py` - Streamlit dashboard application that loads `cleaned_train.csv` and shows:
  - overview KPIs
  - sales trends over time
  - top categories and regions
  - top products
  - shipping impact on sales
- `requirements.txt` - Python package dependencies.

## Dependencies

The project depends on:

- `pandas==3.0.2`
- `streamlit==1.41.1`
- `plotly` (used in the notebook for visualizations)

Install dependencies with:

```bash
pip install -r requirements.txt
pip install plotly
```

## How to Run

1. Run the notebook `train.ipynb` to create and inspect the cleaned dataset.
2. If needed, verify that `cleaned_train.csv` has been created.
3. Start the Streamlit dashboard:

```bash
streamlit run app.py
```

4. Open the local URL shown in the terminal to view the dashboard.

## What the Dashboard Shows

- `Overview` page:
  - Total revenue
  - Total orders
  - Average order value
  - Average shipping time
  - Top category, top region, and fastest shipping method
  - Sales trends and category revenue distribution
- `Business Q&A` page:
  - Top revenue-generating categories
  - Sales over time
  - Best-performing regions
  - Top products by revenue
  - Shipping days vs. sales relationship

## Notes

- The notebook cleans the raw dataset and writes a reusable CSV file.
- `app.py` depends on `cleaned_train.csv` and assumes the file is in the same directory.
- The notebook currently drops columns such as `row_id`, `order_id`, `customer_id`, `customer_name`, `country`, and `product_id`.

Enjoy exploring the sales data and using the dashboard for business insights.