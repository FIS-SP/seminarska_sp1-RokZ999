import harperdb
from secrets import HARPERDB_USERNAME, HARPERDB_URL, HARPERDB_PASSWORD

db = harperdb.HarperDB(
    url=HARPERDB_URL,
    username=HARPERDB_USERNAME,
    password=HARPERDB_PASSWORD
)