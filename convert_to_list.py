import json

def extract_urls_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        url_list = [entry['url'] for entry in data]
    return url_list

# Example usage
if __name__ == "__main__":
    file_path = 'out.json'
    urls = extract_urls_from_json(file_path)
    print("\n".join(urls))
    print(urls)