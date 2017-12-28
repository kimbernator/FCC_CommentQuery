# Query customizations
api_key = "TBTYBAOTWRtUNy0JU5WDqAE8T8ZO5ZNGddBPUcvK"
proceeding = "17-108" # "Restoring Internet Freedom"
sort_terms = "date_submission,ASC" # field,(ASC|DESC)
limit = 10000 # 10,000 is the typical max, anything more will default to 25
api_url = f"https://publicapi.fcc.gov/ecfs/filings?api_key={api_key}&proceedings.name={proceeding}&submissiontype.description=COMMENT&sort={sort_terms}"


# Database settings
db_host = '192.168.1.109'
db_user = ''
db_password = ''
db_schema = ''
