thonimport json
import os
from extractors.instagram_parser import InstagramParser
from outputs.exporters import Exporter

def main():
    input_file = 'data/sample.json'
    output_file = 'data/output.json'
    
    # Load the input data
    with open(input_file, 'r') as f:
        posts_data = json.load(f)
    
    # Initialize the Instagram Parser and Exporter
    parser = InstagramParser(posts_data)
    parsed_data = parser.parse_posts()
    
    # Export the parsed data
    exporter = Exporter(parsed_data)
    exporter.export_to_json(output_file)
    print(f"Data exported to {output_file}")

if __name__ == '__main__':
    main()