# Using Scrapy to scrape websites

## Install dependencies
```bash
pip install -r requirements.txt
```

## Using the scrapy shell to understand the HTML structure
Here are some examples of how to use the scrapy shell to understand the HTML structure of a website.
```bash
scrapy shell 'https://scrapy.org' --nolog

```
Run the command `response.xpath("//title/text()").get()` to get the title of the page.

```bash
scrapy shell 'https://www.deklerkbv.nl/nl/' --nolog
```
Run the command `response.xpath("//a").get()` to get the first anchor tag of the page.

## Creating a spider
Steps to create a spider:
- Make a copy of the `spider.py` file and name it according to the website you want to scrape.
- Modify the structure you want to process, possibly by first using the shell (see above).

## Running the spider
Run the spider and save the output to a JSON file.
```bash
scrapy runspider deklerkbv.py -o out.json
```

## Converting the JSON to a plain newline-separated list of URLs
```bash
cat out.json | jq -r '.[].url'
```
or:
```bash
python convert_to_list.py
```
Now you can pass the output to the [URL List component](https://github.com/michelderu/langflow-playground) in Langflow.
