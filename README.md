# sql-project
1. This project is my Vulnerability Management SQL Project

2. 
  a. The issue I plan to solve through this project is vulnerability management
  b. I am solving this problem through building a data pipeline to help companies know of important vulnerabilities in the products they use

3.
  a. The way this idea came up was through my job. I work as an information security analyst, and this was a project suggested to me by my boss.
      Rather than do this manually, I thought it would be really cool to automate the process. Most XDR's have an advisory page, but they're not that
      detailed or great. Additionally, this was a great way to fuse two interests of mine, data engineering and cybersecurity. When I found the job posting
      for Crowdstrike, I knew this would be the perfect job for this project.
  b. This project ties into the posting in two ways. First, the posting requres SQL and Python experience. Second, the posting talks about how part of the job
      is making insights for business leaders.

4. 
  a. I have two data sources. One is the Microsoft Security Response Center Advisories, and one is the CISA CVE list.
  b. The MSRC data is my API data. One pro of this API is that it doesn't require any authentication to use. However, there is one huge con.
     There is little to no documentaion for this api. Any information I found on it was through some really deep internet investigation.
     The CISA data was different. Tons of documention on the page. However, accessing elements on the page was difficult. Many elements I needed were nested deep in the HTML.

5. 
   a. [API_ETL.ipynb](https://github.com/Csomoya/sql-project/blob/main/notebooks/API_ETL.ipynb) This notebook is my API ETL. It's what I used to get api data.
   b. https://github.com/Csomoya/sql-project/blob/main/notebooks/Web_Scrape_ETL.ipynb This is what I used to scrape  the CISA page.
   c. https://github.com/Csomoya/sql-project/blob/main/notebooks/02_API_ETL.ipynb This is how I loaded the api csv data into my RDS instance.
   d. https://github.com/Csomoya/sql-project/blob/main/notebooks/02_Web_Scrape.ipynb This is how I loaded the web scrape csv data into my RDS instance.
   e. https://github.com/Csomoya/sql-project/blob/main/notebooks/API_SQL_ANALYSIS.py This is my SQL query for the API. Sorry it is .py, codespaces stopped committing.
   f. https://github.com/Csomoya/sql-project/blob/main/notebooks/WEB_SCRAPE_SQL_ANALYSIS.py This is my API query for the web scrape.

6.
  a. The first improvement I would like is for the API to be fully automated. The way I got data was from a release where I had to physically query 2024-apr inside the url for
      it to work. I could probably find a way to do this, I just need more time.
  b. Getting better at version control on Github. I totally messed up several times and made it so that I could no longer commit anything from codespaces. This was something that
      I wasted hours on.
  c. I will put a third in as well. I wish I could figure out what was going on when I tried to get the due_date for CVE. Some worked, and some didn't. Having that date
      could've been a great diagnostic analytic for entries over time.
