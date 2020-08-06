from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    news_title = soup.find_all('div', class_="content_title")
    news_p = soup.find_all('div', class_="article_teaser_body")

    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p
        }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
