# %%
#Import
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# %%
#Environment Variable
password = os.getenv("SUPER_SECRET_KEY")

# %%
#Connection
raw_host = 'isba-dev-01.c9q88v25is0v.us-east-1.rds.amazonaws.com'
raw_username = "admin"
raw_password = password
raw_schema = "sql_project"

raw_db_config = {
    'host' : raw_host,
    'username' : raw_username,
    'password' : raw_password,
    'schema' : raw_schema
}

raw_engine = create_engine(f"mysql+mysqldb://{raw_db_config['username']}:{raw_db_config['password']}@{raw_db_config['host']}/{raw_db_config['schema']}")

# %%
#Descriptive Query
query1 = "SELECT Vendor, COUNT(*) AS num_vulnerabilities, RANK() OVER (ORDER BY COUNT(*) DESC) AS vendor_rank FROM CVE c  GROUP BY Vendor ORDER BY vendor_rank;"

# %% [markdown]
# Which Vedors have the Highest CVE counts in the Dataset?

# %%
#Storing to DF
df1 = pd.read_sql(query1, raw_engine)
df1

# %% [markdown]
# Insight: Microsoft, Apple, Google, Ivanti, and Cisco have the most. This makes sense for everyone minus Ivanti, as they are global corps with a ton of products.
# Recommendation: Look into solutions for Ivanti. Much lower market share than other companies, should be porportional to size. 
# Prediction: Ivanti will go lower on the list.

# %%
#Diagnostic Query
query2 = "SELECT Ransomware, Vendor, COUNT(*) AS num_vulnerabilities FROM CVE WHERE Ransomware = '  Known' GROUP BY Vendor, Ransomware ORDER BY num_vulnerabilities DESC;"

# %% [markdown]
# Which Vendors have had the most ransomware vulnerabilities?

# %%
#Storing to DF
df2 = pd.read_sql(query2, raw_engine)
df2

# %% [markdown]
# Insight: Atlassian has the most ransomware CVE's.
# Reccomendation: Review atlassian security policies. Make reccomendation to customers on atlassian based on said policies.
# Prediction: Customers will have less ransomware attacks/ Atlassian fixes security policies.

# %%



