import argparse
import re
import requests
import pprint
from usp.tree import sitemap_tree_for_homepage

def get_args():
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

def main():
    pp = pprint.PrettyPrinter()
    args = get_args()
    keywords = args.keywords.split(',')

    output = {}
    sites_file = open('sites.txt', 'r')
    site_urls = sites_file.read().splitlines()
    for site_url in site_urls:
        try:
            tree = sitemap_tree_for_homepage(site_url)
            for page in tree.all_pages():
                page_text = requests.get(page.url).text
                output[page.url] = {}
                for keyword in keywords:
                    print("Seaching on %s for %s" % (page.url, keyword))
                    occ = re.findall(keyword, page_text)
                    occurrence_count = len(occ)
                    if occurrence_count > 0:
                        output[page.url][keyword] = occurrence_count

                if output[page.url] == {}:
                    output.pop(page.url)
        except:
            print("failed to search on %s" % site_url)

    pp.pprint(output)

if __name__ == "__main__":
    main()
