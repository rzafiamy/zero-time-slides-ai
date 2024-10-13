import argparse
from core.slides_generator import SlidesGenerator
from config import load_config

def main():
    parser = argparse.ArgumentParser(description="Generate PowerPoint presentations using AI.")
    
    parser.add_argument("--topic", type=str, required=True, help="Topic of the presentation")
    parser.add_argument("--slides", type=int, required=True, help="Number of slides")
    parser.add_argument("--api_key", type=str, help="API key for the provider")
    
    args = parser.parse_args()

    # Load configuration from .env
    config = load_config()

    # Override API key if provided
    if args.api_key:
        config['API_KEY'] = args.api_key
    
    # Generate PPT
    generator = SlidesGenerator(config)
    ppt_file = generator.generate_presentation(args.topic, args.slides)
    print(f"Presentation generated: {ppt_file}")

if __name__ == "__main__":
    main()
