import duckdb
import pandas as pd

# connect DuckDB
con = duckdb.connect(database='mydb.db')

# create table
con.execute("CREATE TABLE mytable (id INTEGER, name STRING)")
con.execute("INSERT INTO mytable VALUES (1, 'Alice')")
con.execute("INSERT INTO mytable VALUES (2, 'Bob')")

# query data
result = con.execute("SELECT * FROM mytable").fetchdf()



# convert DuckDB to DataFrame of Pandas
df = pd.DataFrame(result, columns=result.columns)
