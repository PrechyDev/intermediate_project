# Realtime data analytics pipeline using Polars, DuckDB and Docker

The dataset used here is a transactional dataset which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail. The company mainly sells unique all-occasion gifts and have may wholesale customers. <br>
Download the dataset here - [Online Retail](http://archive.ics.uci.edu/dataset/352/online+retail), and unzip it. 

### Data Cleaning
The data set is cleaned in the `data_cleaning.py` script using `polars` and loaded into a csv file. This process is not automated in the docker container and can be done manually by downloading the dataset and loading it into the data_cleaning script. 
<br>
The null values and inconsistent formats are handled,and duplicate values dropped. The cleaned dataframe is then loaded into `online_retail.py`.

### Data Ingestion into database
The CSV file is then loaded into a polars dataframe for further transformation.

- A new column `TotalAmount` is obtained for each transaction by multiplying `Quantity` by `UnitPrice`.

- The data is grouped by `StockCode` and teach of the following group is calculated to obtain new columns.
    - The sum of `TotalAmount` as `Total_cost_stock_sold`.
    - The mean of `TotalAmount` as `Average_cost_stock_sales`.
    - The minimum of `Quantity` as `Min_sales`.
    - The maximum of `Quantity` as `Max_sales`.

- A new dataframe is created with the columns the columns `StockCode`, `Total_cost_stock_sold`, `Average_cost_stock_sales`, `Min_sales`, and `Max_sales` as finance_df.

- Using `duckdb-engine`, a duckdb SQLAlchemy driver, the new dataframe is written to a DuckDB database named `retail.db` in a table called `finance_data`. This process requires the `pyarrow` package to load the dataframe to db. This is because, polars converts the dataframe to a pandas df under the hood before loadiing to a database. It also requires the `sqlalchemy` package.

### Dockerizing
This project requires that the entire project be dockerized alongside the duckdb CLI to help query the finance_data table. A `duckdb` binary file is included in the project container to make this possible.
<br>
All the requirements are listed in the `requirements.txt`.
<br>
To build the docker container, run `docker compose up`. This would automatically run the python ingestion script and also keep the container running. <br>
Access the duckdb_cli container and open an interactive shell using the command - `docker compose exec duckdb_cli /bin/sh
`. You can then run the duckdb CLI using `./duckdb /analytics/retail.db
`. This should allow you to run sql commands in the duckdb cli. 
<br>
To test, run `SELECT * FROM finance_data LIMIT 5`.
