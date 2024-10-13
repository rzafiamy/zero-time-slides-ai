import openai
import requests
import json
import os

class AIRequester:
    def __init__(self, config):
        """
        Initialize the AIRequester with the specified provider, host, and API key.
        """
        self.provider = config['PROVIDER']
        self.host = config['HOST']
        self.api_key = config['API_KEY']
        self.config = config
        self.cache_file = os.path.join(config['OUTPUT_PATH'], 'cache.json')

        if self.provider == 'openai':
            openai.api_key = self.api_key
            openai.base_url = self.host

        # Create the cache file if it doesn't exist
        if not os.path.exists(self.cache_file):
            with open(self.cache_file, 'w') as f:
                json.dump({}, f)

    def create_prompt(self, topic, slide_length, context=''):
        """
        Create a prompt for the AI model based on the topic and slide length.
        """
        return f"""Create an outline for a slideshow presentation on the topic of {topic} which is {slide_length}
        slides long. Make sure it is {slide_length} long.

        You are allowed to use the following slide types:
        Title Slide - (Title, Subtitle)
        Content Slide - (Title, Content)
        Image Slide - (Title, Content, Image)
        Thanks Slide - (Title)

        Put this tag before the Title Slide: [L_TS]
        Put this tag before the Content Slide: [L_CS]
        Put this tag before the Image Slide: [L_IS]
        Put this tag before the Thanks Slide: [L_THS]
        
        Put this tag before the Title: [TITLE]
        Put this tag after the Title: [/TITLE]
        Put this tag before the Subtitle: [SUBTITLE]
        Put this tag after the Subtitle: [/SUBTITLE]
        Put this tag before the Content: [CONTENT]
        Put this tag after the Content: [/CONTENT]
        Put this tag before the Image: [IMAGE]
        Put this tag after the Image: [/IMAGE]

        Put "[SLIDEBREAK]" after each slide 

        For example:
        [L_TS]
        [TITLE]Among Us[/TITLE]

        [SLIDEBREAK]

        [L_CS] 
        [TITLE]What Is Among Us?[/TITLE]
        [CONTENT]
        1. Among Us is a popular online multiplayer game developed and published by InnerSloth.
        2. The game is set in a space-themed setting where players take on the roles of Crewmates and Impostors.
        3. The objective of Crewmates is to complete tasks and identify the Impostors among them, while the Impostors' goal is to sabotage the spaceship and eliminate the Crewmates without being caught.
        [/CONTENT]

        [SLIDEBREAK]

        Elaborate on the Content, provide as much information as possible.
        REMEMBER TO PLACE a [/CONTENT] at the end of the Content.
        Do not include any special characters (?, !, ., :, ) in the Title.
        Do not include any additional information in your response and stick to the format.
        
        Context:
        {context}
        """

    def request_ai(self, message):
        """
        Get the response from the chosen AI model.
        """
        cached_response = self._check_cache(message)
        if cached_response:
            return cached_response
        
        if self.provider == 'openai':
            response = self._get_openai_response(message)
        elif self.provider == 'ollama':
            response = self._get_ollama_response(message)
        else:
            raise ValueError("Unsupported provider")
        
        # Cache the response
        self._update_cache(message, response)
        
        return response

    def _get_openai_response(self, message):
        """
        Get the response from the OpenAI GPT-3 model.
        """
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content

    def _get_ollama_response(self, message):
        """
        Get the response from the Ollama AI model.
        """
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"prompt": message}
        response = requests.post(f"{self.host}/api/completion", json=data, headers=headers)
        response_json = response.json()
        return response_json['response']

    def _check_cache(self, message):
        """
        Check if the message exists in the cache and return the cached response if it does.
        """
        with open(self.cache_file, 'r') as f:
            cache = json.load(f)
        return cache.get(message)

    def _update_cache(self, message, response):
        """
        Update the cache with the new request-response pair.
        """
        with open(self.cache_file, 'r') as f:
            cache = json.load(f)
        cache[message] = response
        with open(self.cache_file, 'w') as f:
            json.dump(cache, f, indent=4)
