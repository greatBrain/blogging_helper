#Helper functions

from dotenv import load_dotenv
import os


#Get Tiny PNG API token
def get_tiny_api() -> str | None:     
    load_dotenv('../docs/keys.env') 
    return(os.getenv("TINY_API_KEY"))