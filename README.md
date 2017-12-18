# FCC_CommentQuery
Uses the FCC's API to access and store filings

requires modules:
json
requests
mysql.connector

Prerequisites

- Mysql database with existing schema that has a default character set of utf8mb4 (utf8 will result in errors with emojis)
- API key from https://api.data.gov/

Usage

- Edit ```settings.py``` with your API key and database connection information. This file can also be edited to change the size of each API call's result, the proceeding you want to collect filings for, and the sort method.
- Execute ```python fcc.py```. This will continue until interrupted or there are no results left.
- If interrupted, running the program again will resume by querying the highest value in the database and modifying the offset. To restart, the database must be dropped or truncated.
