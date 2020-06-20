import argparse
import json
import os
import re
import requests
import pprint
import time
from usp.tree import sitemap_tree_for_homepage

def args():
    """
    Gets the args from the command line and stores in local variables.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("-k",
                        "--keywords",
                        help="comma delimited string of keywords you would like to search for",
                        default=None,
                        type=str)

    args = parser.parse_args()

    return args

def site_urls():
    sites_file = open('sites.txt', 'r')
    site_urls = sites_file.read().splitlines()
    return site_urls

def search_site(site, keywords, data):
    try:
        tree = sitemap_tree_for_homepage(site)
        counter = 0
        for page in tree.all_pages():
            page_text = ''
            for keyword in keywords:
                if not data.get(page.url): data[page.url] = {}
                if data[page.url].get(keyword, -1) >= 0: continue
                if not page_text:
                    print('getting page text') # only get page_text if necessary
                    page_text = requests.get(page.url).text
                print("Seaching on %s for %s" % (page.url, keyword))
                data = store_match_count(data, page.url, page_text, keyword)

            counter += 1
            if counter >= 20:
                save_data(data)
                counter = 0
    except:
        print("failed to search on %s" % site)

    return data

def store_match_count(data, page_url, page_text, keyword):
    occurrences = len(re.findall(keyword, page_text))
    data[page_url][keyword] = occurrences
    return data

def save_data(data):
    print("SAVING DATA...")
    file_path = 'data.json'
    with open(file_path, 'w') as data_file:
        json.dump(data, data_file)

def fetch_data():
    file_path = 'data.json'
    if not os.path.exists(file_path):
        open(file_path, "x")

    if os.path.getsize(file_path) == 0:
        return {}

    with open(file_path) as json_data:
        print(json_data)
        data = json.load(json_data)
        return data

def main():
    keywords = args().keywords.split(',')
    data = fetch_data()

    for site_url in site_urls():
        data = search_site(site_url, keywords, data)
        print("Saving data for %s" % site_url)
        save_data(data)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
