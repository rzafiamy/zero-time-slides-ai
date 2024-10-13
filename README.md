# Zero-time-Slides-AI - Python Application

## Overview

**Zero-time-Slides-AI** is a Python application that automates the creation of PowerPoint presentations. By simply providing a topic and the number of slides, it generates high-quality slides, complete with text content and images, using AI and web crawling technologies.

The app integrates:
- **OpenAI** or **Ollama** for AI-generated content based on the provided topic.
- **icrawler** to automatically download relevant images from the internet using `GoogleImageCrawler`.
- **python-pptx** to generate the PowerPoint (.pptx) slides.
- **argparse** for command-line arguments to specify the topic and number of slides.
  
All API keys and other sensitive configurations are stored in a `.env` file and accessed via a centralized `config.py` module.

## Features

- **Automated Content**: Fetches AI-generated content using OpenAI or Ollama API based on the given topic.
- **Image Fetching**: Uses `icrawler` to search and download images from the internet relevant to each slide.
- **Slide Creation**: Utilizes `python-pptx` to generate the slides with both text and images.
- **Command-Line Interface**: Easy to use with CLI arguments for the topic and number of slides.
- **Configurable via `.env`**: Stores all keys and configurations in an environment file, ensuring secure and flexible configuration management.
- **Library Usage**: Can also be integrated as a module into other Python projects.
- **Free and Open Source**: Completely free to use and modify.

## Requirements

Before running **Zero-time-Slides-AI**, ensure the following Python packages are installed:

- `openai`
- `ollama`
- `icrawler`
- `python-pptx`
- `python-dotenv`
- `argparse`

You can install these dependencies using pip:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/rzafiamy/Zero-time-Slides-AI.git
cd Zero-time-Slides-AI
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your `.env` file:

Create a `.env` file in the root directory of your project and add your API keys:

```
OPENAI_API_KEY=your-openai-api-key
OLLAMA_API_KEY=your-ollama-api-key
IMAGE_DOWNLOAD_PATH=your-image-download-directory
```

4. Update `config.py` to load configuration from the `.env` file:

```python
# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY")
IMAGE_DOWNLOAD_PATH = os.getenv("IMAGE_DOWNLOAD_PATH")
```

## Usage

### Command Line Interface

Run the app via the command line by passing the required arguments:

```bash
python generate_slides.py --topic "Artificial Intelligence" --pages 10
```

**Arguments:**
- `--topic`: The main topic for the presentation (e.g., "Artificial Intelligence").
- `--pages`: The number of slides to generate (e.g., 10).

### Library Usage

You can also use Zero-time-Slides-AI as a module in your Python projects:

```python
from zero_slides_ai import generate_presentation

generate_presentation(topic="Artificial Intelligence", pages=10)
```

## Configuration

All API keys and configuration settings are stored in a `.env` file. The app reads these settings through `config.py` to avoid hardcoding sensitive information. 

Ensure your `.env` file includes the following keys:
- `OPENAI_API_KEY`: Your OpenAI API key.
- `OLLAMA_API_KEY`: Your Ollama API key (if using Ollama).
- `IMAGE_DOWNLOAD_PATH`: The path where images will be downloaded for slide integration.

## Example

To generate a 5-slide presentation on "Climate Change", run:

```bash
python generate_slides.py --topic "Climate Change" --pages 5
```

This will create a PowerPoint file with:
- AI-generated content on the topic.
- Relevant images downloaded from the web.
- A `.pptx` file ready for use in presentation software.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contribution

Contributions are welcome! If you encounter any issues or have suggestions for new features, feel free to open an issue or submit a pull request.

## Contact

For any queries or feedback, please reach out:

- **Your Name**: [rzafiamy@infodev.ovh](mailto:rzafiamy@infodev.ovh)
- GitHub: [rzafiamy](https://github.com/rzafiamy)