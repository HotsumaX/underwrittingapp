import logging
import pandas as pd
from sqlalchemy import create_engine, text
import extract_listing_data  # Import your module that extracts listings data

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to store data in the database and log current contents
def store_data():
    engine = create_engine('postgresql://weaponx@localhost:5432/mydatabase')
    with engine.connect() as connection:
        listings = extract_listing_data.get_listings()  # Get listings data
        df = pd.DataFrame(listings)
        df.to_sql('real_estate_listings', engine, if_exists='replace', index=False)

        # Log the current contents of the real_estate_listings table
        result = connection.execute(text("SELECT * FROM real_estate_listings"))
        rows = result.fetchall()
        logger.info("Current contents of real_estate_listings table:")
        for row in rows:
            logger.info(row)

# Store the listings data
store_data()