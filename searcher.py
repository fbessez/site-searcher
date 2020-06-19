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
    parser.add_argument(
        "site_url", help="URL of the site you would like to search.", type=str
    )

    parser.add_argument("-k",
                        "--keywords",
                        help="comma delimited string of keywords you would like to search for",
                        default=None,
                        type=str)

    args = parser.parse_args()

    return args

def main():
    args = get_args()
    keywords, site_url = args.keywords.split(','), args.site_url
    pp = pprint.PrettyPrinter()
    print(keywords)
    print("You have requested to search for: %s on %s" % (keywords, site_url))

    output = {}
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

        if output[page.url] == {}: output.pop(page.url)

    pp.pprint(output)

if __name__ == "__main__":
    main()
