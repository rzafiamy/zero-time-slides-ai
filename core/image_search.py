import os
import json
import random
import string
from icrawler import ImageDownloader
from icrawler.builtin import GoogleImageCrawler, BingImageCrawler
from urllib.parse import urlparse
import base64



class PrefixDownloader(ImageDownloader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # generate unique name for each image using uuid and base64
        self.unique_image_name = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

    def get_filename(self, task, default_ext):
        url_path = urlparse(task['file_url'])[2]
        if '.' in url_path:
            extension = url_path.split('.')[-1]
            if extension.lower() not in [
                'jpg', 'jpeg', 'png', 'bmp', 'tiff', 'gif', 'ppm', 'pgm'
            ]:
                extension = default_ext
        else:
            extension = default_ext

        filename = base64.b64encode(url_path.encode()).decode()
        return "p_" + self.unique_image_name + '{}.{}'.format(filename, extension)

class ImageSearcher:
    def __init__(self, config):
        self.images_path = config.get('IMAGES_PATH', 'images')
        self.cache_file = os.path.join(self.images_path, config.get('CACHE_FILE', 'cache.json'))
        self.cache = self.load_cache()

    def load_cache(self):
        """Load cache from a JSON file."""
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("Cache file is corrupted, starting with an empty cache.")
        return {}

    def save_cache(self):
        """Save cache to a JSON file."""
        with open(self.cache_file, 'w') as f:
            json.dump(self.cache, f)

    def download_image(self, query):
        # Check if the query result is already cached
        if query in self.cache:
            print(f"Cache hit for query: {query}")
            return self.cache[query]

        # If not cached, download the image
        google_crawler = BingImageCrawler(
            downloader_cls=PrefixDownloader,
            feeder_threads=1,
            parser_threads=2,
            downloader_threads=4,
            storage={'root_dir': self.images_path})
        google_crawler.crawl(keyword=query, max_num=1)

        # Find the downloaded image file
        image_files = [f for f in os.listdir(self.images_path) if f.startswith('p_')]
        image_file = image_files[0] if image_files else None

        # rename file by removing the prefix 'p_'
        if image_file:
            os.rename(os.path.join(self.images_path, image_file), os.path.join(self.images_path, image_file[2:]))
            image_file = image_file[2:]
        
        # Cache the result before returning it and save to JSON file
        if image_file:
            self.cache[query] = image_file
            self.save_cache()

        image_file = 'default.png' if not image_file else image_file
        
        return image_file
