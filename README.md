# scraping-challenge-1
**Overview:**

Referral Link: https://docs.scrapy.org/en/latest/intro/tutorial.html

We are going to obtain the following datas from the site books.toscrape.com using scrapy :

Book Title, Product Price, Image URL and Book URL

**Step 1:** First we need to install the Scrapy module.

```
sudo pip install scrapy
```

**Step 2:** To test out the "scraping-challenge-1"  project, please execute the below commands:

```
git clone https://github.com/balav92/scraping-challenge-1.git

cd scraping-challenge-1

scrapy crawl books2scrape
```

**Step 3:** In order to export the data into a CSV file, please execute the below command:

```
scrapy crawl books2scrape -o output.csv
```

**Note:** You can specify your desired filename for the .csv file in the above command ( Ex: result.csv, Finaloutput.csv)
Now the following fields  are displayed in the CSV output file :

```
Book Title
Product Price
Image URL 
Book URL 
```

![alt text](https://raw.githubusercontent.com/balav92/scraping-challenge-1/main/Start.PNG)

![alt text](https://raw.githubusercontent.com/balav92/scraping-challenge-1/main/End.PNG)

Thats all folks!
