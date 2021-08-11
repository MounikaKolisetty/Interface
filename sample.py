import pyodbc

# Replace <table-name> with the name of the database table to query.
table_name = "edl_current.telematics_machine_enhanced"
column_name = "srl_num"
# Connect to the Databricks cluster by using the
# Data Source Name (DSN) that you created earlier.
conn = pyodbc.connect("DSN=Database", autocommit=True)

# Run a SQL query by using the preceding connection.
cursor = conn.cursor()
cursor.execute(f"SELECT * FROM {table_name} where substr(native_pin,0,4) = '1L06' LIMIT 3")

# Print the rows retrieved from the query.
print(f"Query output: SELECT * FROM {table_name} LIMIT 3\n")
for row in cursor.fetchall():
  print(row)