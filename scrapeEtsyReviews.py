# Importing Libraries
from bs4 import BeautifulSoup
from selenium import webdriver
import numpy as np
import pandas as pd
import csv
import time
from time import sleep
from selenium.common.exceptions import NoSuchElementException
# from google.colab import drive
# import sqlite3 as sql

# Start timer
start_time = time.time()

# Defining variables
product_url = []
review_list = []
START_PAGE = 1
END_PAGE = 250
csv_file_name = ''

# To get how many products were scraped successfully
scrape_count = 0

# To get how many products in a page 
product_count = 0

# Starting the web driver
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
driver.set_page_load_timeout(15)
driver.implicitly_wait(2)

for page_no in range(START_PAGE, END_PAGE+1):

    # Page URL
    page_url = 'https://www.etsy.com/in-en/c/jewelry/earrings/ear-jackets-and-climbers?ref=pagination&page=' + str(page_no)

    # Switching to the page_url
    driver.switch_to.window(driver.window_handles[0])

    # Get page_url
    driver.get(page_url)
    sleep(1)

    print('\n\n***** Scraping products from page: {} *****\n\n'.format(page_no))

    try:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('div', 'wt-bg-white wt-display-block wt-pb-xs-2 wt-mt-xs-0')

        # Extracting Product URL
        for li in results[0].ul:
            try:
                product_url.append(li.a.get("href"))
                # product_url.append(li.a.get('href').rpartition('/')[0])
            except:
                pass

        # Removing empty strings in product_url list
        while ('' in product_url):
            product_url.remove('')

        print('\nTotal products in page {} is {}\n'.format(page_no, len(product_url)))

        # Open a new window
        driver.execute_script("window.open('');")

        try:
            for product in product_url:
                # Open a new window, (uncomment below line if scraping in local PC.)
                # driver.execute_script("window.open('');")

                # Switch to the new window
                driver.switch_to.window(driver.window_handles[1])

                # Opening the product page
                driver.get(product)

                soup = BeautifulSoup(driver.page_source, 'html.parser')

                # Finding review text from 1st review page and storing in a list
                for review in soup.find_all('div', class_='wt-content-toggle--truncated-inline-multi'):
                    review_list.append(review.text.strip())
                print('1st review page of product no. {} is scraped'.format(product_url.index(product)+1))

                
                # Scraping 2nd review_page of the product
                try:
                    second_page = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div/div[2]/nav/ul/li[3]/a')
                    second_page.click()
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    for review in soup.find_all('div', class_='wt-content-toggle--truncated-inline-multi'):
                        review_list.append(review.text.strip())
                    print('{} products scraped'.format(scrape_count+1))
                    
                    scrape_count += 1
                    product_count += 1
                except:
                    pass
        except:
            failed_product_urls.append(product_url)
            print('Failed to scrape a product')
            continue

        finally:
            # Close product URL tab, switch back to pagination URL
            driver.close()
            driver.switch_to.window(driver.window_handles[0]) 


    except:
        # Append the page_no to a list to extract data from, later
        print('\nFailed to scrape page:{}\n'.format(page_no))
        failed_pages.append(page_no)
        continue

    print('{} products scraped from page number {}'.format(product_count+1, page_no))
    product_count = 0

    if (page_no % 10 == 0):
      df = pd.DataFrame(set(review_list))
      csv_file_name = 'scraped_pages_{}_{}.csv'.format(page_no-10, page_no)
      df.to_csv(csv_file_name, mode = 'a', header = False, index = False)
      sleep(2)
      review_list.clear()
    
    product_url.clear()

# Quitting the web driver
driver.quit()

# Stop timer, calculate execution time
end_time = time.time()

hours, rem = divmod(end_time-start_time, 3600)
minutes, seconds = divmod(rem, 60)
print('\n\nExecution Time:')
print("--- {:0>2}:{:0>2}:{:05.2f} ---".format(int(hours),int(minutes),seconds))
