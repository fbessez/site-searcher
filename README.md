# Site Searcher

### Description

This script takes a txt file of domains (ex: `sites.txt`) and keyword args (ex: `cookies,cake,bread and butter`) and returns back the occurrences of each keyword on each webpage within the given domain's sitemap.

### Usage

Fill in `sites.txt` with the URL that you are interested in searching.

Then run the following to output the raw data to `data.json`

```
python3 searcher.py -k="<KEYWORDS,GO,HERE>"
```

Then, if you want to filter out the not-found keywords and the sites where no keywords were found, run:

```
python3 filter.py
```

It will output the filtered data to `filtered_data.json`

### Example

##### Input

```
    python3 searcher.py --keywords='word and another word,cookies'
```

##### Output

```
Seaching on https://fabien.bessez.com/pensieve/house-hacker for grpc
Seaching on https://fabien.bessez.com/pensieve/grpc-at-juvo for grpc
Seaching on https://fabien.bessez.com/pensieve/burpsuite-traffic-proxy for grpc
Seaching on https://fabien.bessez.com/pensieve/tags/network-monitoring/ for grpc
Seaching on https://fabien.bessez.com/pensieve/tags/traffic-proxy/ for grpc
Seaching on https://fabien.bessez.com/pensieve/tags/aws/ for grpc
Seaching on https://fabien.bessez.com/pensieve/tags/craigslist/ for grpc
Seaching on https://fabien.bessez.com/pensieve/tags/ec-2/ for grpc
Seaching on https://fabien.bessez.com/pensieve/tags/go/ for grpc
Seaching on https://fabien.bessez.com/pensieve/tags/grpc/ for grpc
Seaching on https://fabien.bessez.com/pensieve/tags/protobuf/ for grpc
Seaching on https://fabien.bessez.com/pensieve/tags/python/ for grpc
Seaching on https://fabien.bessez.com/pensieve/tags/redis/ for grpc
Seaching on https://fabien.bessez.com/archive/ for grpc
Seaching on https://fabien.bessez.com/ for grpc
Seaching on https://fabien.bessez.com/pensieve/ for grpc
Seaching on https://fabien.bessez.com/pensieve/tags/ for grpc
failed to search on blablabla
{'https://fabien.bessez.com/': {'grpc': 1},
 'https://fabien.bessez.com/archive/': {'grpc': 1},
 'https://fabien.bessez.com/pensieve/': {'grpc': 4},
 'https://fabien.bessez.com/pensieve/burpsuite-traffic-proxy': {'grpc': 1},
 'https://fabien.bessez.com/pensieve/grpc-at-juvo': {'grpc': 14},
 'https://fabien.bessez.com/pensieve/house-hacker': {'grpc': 1},
 'https://fabien.bessez.com/pensieve/tags/': {'grpc': 3},
 'https://fabien.bessez.com/pensieve/tags/aws/': {'grpc': 1},
 'https://fabien.bessez.com/pensieve/tags/craigslist/': {'grpc': 1},
 'https://fabien.bessez.com/pensieve/tags/ec-2/': {'grpc': 1},
 'https://fabien.bessez.com/pensieve/tags/go/': {'grpc': 4},
 'https://fabien.bessez.com/pensieve/tags/grpc/': {'grpc': 7},
 'https://fabien.bessez.com/pensieve/tags/network-monitoring/': {'grpc': 1},
 'https://fabien.bessez.com/pensieve/tags/protobuf/': {'grpc': 4},
 'https://fabien.bessez.com/pensieve/tags/python/': {'grpc': 1},
 'https://fabien.bessez.com/pensieve/tags/redis/': {'grpc': 1},
 'https://fabien.bessez.com/pensieve/tags/traffic-proxy/': {'grpc': 1}}
```

### Setup + Requirements

1. You will need to have installed `python3`
2. You will need to have installed `pip3`
3. Run `pip3 install -r requirements.txt` to install the dependencies
4. Voila!

### Help

Feel free to reach out for any questions/comments!
