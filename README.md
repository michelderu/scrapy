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
- Run the command `fetch("https://old.reddit.com/")` to fetch a specific page.
- Run `response.xpath("//title/text()").get()` to get the title of the page.

```bash
scrapy shell 'https://www.deklerkbv.nl/nl/' --nolog
```
- Run the command `response.xpath("//a/@href").getall()` to get the all anchor tags of the page.

## Creating a spider
Steps to create a spider:
- Make a copy of the `spider.py` file and name it according to the website you want to scrape.
- Modify the structure you want to process, possibly by first using the shell (see above).

Have a look at the [scrapy documentation](https://docs.scrapy.org/en/2.11/intro/overview.html) for more inspiration on how to structure your spider.

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
