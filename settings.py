# Query customizations
api_key = ""
proceeding = "17-108"
sort_terms = "date_submission,ASC"
limit = 10000
api_url = f"https://publicapi.fcc.gov/ecfs/filings?api_key={api_key}&proceedings.name={proceeding}&submissiontype.description=COMMENT&sort={sort_terms}"

# Database settings
db_host = '192.168.1.109'
db_user = ''
db_password = ''
db_schema = ''
