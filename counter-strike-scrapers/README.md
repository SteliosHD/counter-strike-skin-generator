# Counter Strike Scrapers
This repository contains a collection of scrapers that I have written to scrape data from the Counter Strike Global Offensive (CSGO) websites. 
The scrapers are written in Python and use the BeautifulSoup library to scrape the data.

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
