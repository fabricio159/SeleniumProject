from dotenv import load_dotenv
import os

# Loading env vars

load_dotenv()

print(os.getenv('BROWSER'))
print(os.getenv('BASE_URL'))


class Config:
    BROWSER = os.getenv('BROWSER', 'chrome').lower()
    BASE_URL = os.getenv('BASE_URL')
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'
    PAGE_LOAD_TIMEOUT = int(os.getenv('PAGE_LOAD_TIMEOUT', '30'))
    EXPLICIT_WAIT = int(os.getenv('EXPLICIT_WAIT', '10'))


