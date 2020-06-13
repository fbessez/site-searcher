import argparse
import re
import requests
from usp.tree import sitemap_tree_for_homepage

def get_args():
    """
Gets the args from the command line and stores in local variables.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "site_url", help="URL of the site you would like to search.", type=str
    )
    parser.add_argument(
        "keywords", help="comma delimited string of keywords you would like to search for", type=str
    )
    args = parser.parse_args()

    return args

def main():
    args = get_args()
    keywords, site_url = args.keywords.split(','), args.site_url
    print("You have requested to search for: %s on %s" % (keywords, site_url))

    tree = sitemap_tree_for_homepage(site_url)
    for page in tree.all_pages():
        page_text = requests.get(page.url).text
        for keyword in keywords:
          occ = re.findall(keyword, page_text)
          print("%s found %d occurrences of %s" % (page.url, len(occ), keyword))

if __name__ == "__main__":
    main()
