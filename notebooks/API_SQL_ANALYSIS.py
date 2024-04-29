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
query1 = "SELECT category, COUNT(*) AS product_count FROM ProductTree pt GROUP BY category"

# %% [markdown]
# Buesiness Question: Which Products have the highest number of anvisories from microsoft?

# %%
#Storing to DF
df1 = pd.read_sql(query1, raw_engine)
df1

# %% [markdown]
# Insight: Dev Tools, Windows and Azure are top three
# Reccomendation: Highten awareness of new patches for these three products. Create alerts rather than having weekly updates.
# Prediction: Lower likelihood of compromise.

# %%
#Diagnostic Query
query2 = "WITH new_vuln_data AS (SELECT * FROM Vulnerabilities WHERE inserted_at = (SELECT MAX(inserted_at) FROM Vulnerabilities) SELECT threats, COUNT(*) AS num_occurrences FROM new_vuln_data WHERE threats IS NOT NULL GROUP BY threats ORDER BY num_occurrences DESC;"
query3 = "SELECT threats, COUNT(*) AS num_occurrences FROM Vulnerabilities WHERE threats IS NOT NULL GROUP BY threats ORDER BY num_occurrences DESC;"

# %% [markdown]
# What are the largest threats from microsoft advisory?

# %%
#Storing to DF
df2 = pd.read_sql(query3, raw_engine)
df2

# %% [markdown]
# Insight: The two highest are Priveledge Escalation and Remote Code Execution
# Reccomendation: Reccomend that customers enable stricter policies when using microsoft products. Sell cloudflare security solutions to supplement defender
# Prediction: Microsoft stays on top of threats. Customers have lower likelihood of being compromised VIA these methods.


