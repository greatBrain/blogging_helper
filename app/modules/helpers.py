#Helper functions

from dotenv import load_dotenv
import os


#Normalizes the path to make it platform independent(on Windows adds \ and Unix Like adds /)
def get_file_path():
    keys_file_path = '../docs/keys.env'
    return(os.path.normpath(keys_file_path))


#Get Tiny PNG API token
def get_tinify_api() -> str:   

    try:
      load_dotenv(get_file_path())     
      return(os.getenv("TINY_API_KEY"))

    except ValueError as e:
       return("Error getting Tinify API key", " ", e)