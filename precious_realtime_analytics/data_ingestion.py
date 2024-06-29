import polars as pl
import duckdb

df = pl.read_csv('online_retail.csv')

# Add 'TotalAmount' column
df = df.with_columns((pl.col('Quantity') * pl.col('UnitPrice')).round(2).alias('TotalAmount'))

#Create new columns for finance adata
finance_df = df.group_by("StockCode").agg(
    pl.sum("TotalAmount").alias("Total_cost_stock_sold").round(2),
    pl.mean("TotalAmount").alias("Average_cost_stock_sales").round(2),
    pl.min("Quantity").alias("Min_sales"),
    pl.max("Quantity").alias("Max_sales")
    )

# Select the required columns to create a new DataFrame
# finance_df = df.select([
#     "StockCode",
#     "Total_cost_stock_sold",
#     "Average_cost_stock_sales",
#     "Min_sales",
#     "Max_sales"
# ])

# # Store the retail data in the database
# df.write_database(
#     table_name='retail_data',
#     connection="duckdb:///retail.db",
#     if_table_exists='replace'
# )

# Store the finance data in the database
finance_df.write_database(
    table_name='finance_data',
    connection="duckdb:///retail.db",
    if_table_exists='replace'
)

print('data saved to database successfully')

# test the connection
#with duckdb.connect(database="retail.db", read_only=False) as con:
#    con.query("SELECT * FROM finance_data").show()