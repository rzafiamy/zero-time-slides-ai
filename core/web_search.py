# web_search.py
from duckduckgo_search import DDGS
from bs4 import BeautifulSoup

class WebSearch:
    def __init__(self, config, query, max_results=5):
        """
        Initializes the WebSearch with a query and maximum number of results.
        """
        self.query = query
        self.max_results = max_results
        self.config = config

    def search(self):
        """
        Performs a DuckDuckGo search and returns the raw results.
        """
        try:
            results = DDGS().text(self.query, max_results=self.max_results)
            return results
        except Exception as e:
            print(f"Error while searching: {e}")
            return []

    def parse_results(self, results):
        """
        Parses the search results and returns them in a markdown format.
        """
        markdown_results = []
        for result in results:
            title = result.get('title', 'No title')
            href = result.get('href', 'No link')
            body = result.get('body', 'No description')
            
            # Parse the body using BeautifulSoup (if needed)
            soup = BeautifulSoup(body, 'html.parser')
            parsed_body = soup.get_text()

            # Format the result in markdown format
            markdown_result = f"### [{title}]({href})\n\n{parsed_body}\n"
            markdown_results.append(markdown_result)

        return "\n---\n".join(markdown_results)

    def format_with_llm(self, ai_requester, markdown_results):
        """
        Uses ai_requester to format the results via LLM.
        """
        try:
            formatted_response = ai_requester.request_ai("Format the following results in proper markdown:\n" + markdown_results)

            return formatted_response
        except Exception as e:
            print(f"Error while formatting with LLM: {e}")
            return markdown_results

    def perform_search_and_format(self, ai_requester):
        """
        Performs the entire flow: search, parse, and format using LLM.
        """
        # Step 1: Perform search
        results = self.search()
        
        if not results:
            return "No results found."

        # Step 2: Parse results into markdown
        markdown_results = self.parse_results(results)

        # Step 3: Format results with LLM
        formatted_results = self.format_with_llm(ai_requester, markdown_results)

        return formatted_results