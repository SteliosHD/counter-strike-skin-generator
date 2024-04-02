# Counter Strike Scrapers
This repository contains a collection of scrapers that I have written to scrape data from the Counter Strike Global Offensive (CSGO) websites. 
The scrapers are written in Python and use the BeautifulSoup library to scrape the data.


## Requirements
- Python 3.10 or higher
- Poetry 1.8.2


## Installation
1. Clone the repository
2. Install the dependencies using poetry
```bash
poetry install
```
3. Activate the virtual environment (if you are using an ide like PyCharm, it will automatically detect the virtual environment and activate it for you. 
If you are using the terminal, you can activate the virtual environment using the following command)
```bash
poetry shell
```
4. Install the pre-commit hooks
```bash
pre-commit install
```
5. Install playwright
```bash
playwright install
```

## Usage
To run the scrapers, you can use the following command
```bash
python manage.py run <scraper_name> <optional_extra_arguments>
```
e.g. if you want to run the weapon_urls scraper, you can use the following command
```bash
python manage.py run cs-stash --weapon_urls
```
You should see the following output
```bash
Weapon URLs have run was successful
[<list of weapon urls>]
```
The same command can be used to run the skin_urls scraper
```bash
python manage.py run cs-stash --skin_urls
```

## Contributing
If you would like to contribute to this repository, please create a new branch and make a pull request.
Once approved by the code owner, the changes will be merged into the master branch.