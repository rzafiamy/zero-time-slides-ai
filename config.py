import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    return {
        'PROVIDER': os.getenv('PROVIDER', 'openai'),  # Default to 'openai'
        'HOST': os.getenv('HOST', 'https://api.openai.com'),
        'API_KEY': os.getenv('API_KEY'),
        'OUTPUT_PATH': os.getenv('OUTPUT_PATH', 'output'),  # Default to 'output',
        'IMAGES_PATH': os.getenv('IMAGES_PATH', 'images')  # Default to 'images'
    }
