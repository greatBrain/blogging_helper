#Helper functions

from dotenv import load_dotenv
import os


#Get Tiny PNG API token
def get_tinify_api() -> str:     
    
    try:
      load_dotenv('../docs/keys.env')     
      return(os.getenv("TINY_API_KEY"))

    except ValueError as e:
       return("Error getting Tinify API key", " ", e)