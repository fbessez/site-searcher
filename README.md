# Site Searcher

### Description

This script takes a domain (ex: https://fabien.bessez.com) and keyword args (ex: `cookies,cake,bread and butter`) and returns back the occurrences of each keyword on each webpage within the given domain's sitemap.

### Usage

```
python3 searcher.py <URL> -k="<KEYWORDS,GO,HERE>"
```

### Example

##### Input

```
    python3 searcher.py https://fabien.bessez.com --keywords='word and another word,cookies'
```

##### Output

```
https://fabien.bessez.com/pensieve/house-hacker found 1 occurrences of grpc
https://fabien.bessez.com/pensieve/house-hacker found 0 occurrences of cookies
https://fabien.bessez.com/pensieve/grpc-at-juvo found 14 occurrences of grpc
https://fabien.bessez.com/pensieve/grpc-at-juvo found 0 occurrences of cookies
https://fabien.bessez.com/pensieve/burpsuite-traffic-proxy found 1 occurrences of grpc
https://fabien.bessez.com/pensieve/burpsuite-traffic-proxy found 0 occurrences of cookies
https://fabien.bessez.com/pensieve/tags/network-monitoring/ found 1 occurrences of grpc
https://fabien.bessez.com/pensieve/tags/network-monitoring/ found 0 occurrences of cookies
https://fabien.bessez.com/pensieve/tags/traffic-proxy/ found 1 occurrences of grpc
https://fabien.bessez.com/pensieve/tags/traffic-proxy/ found 0 occurrences of cookies
https://fabien.bessez.com/pensieve/tags/aws/ found 1 occurrences of grpc
https://fabien.bessez.com/pensieve/tags/aws/ found 0 occurrences of cookies
https://fabien.bessez.com/pensieve/tags/craigslist/ found 1 occurrences of grpc
https://fabien.bessez.com/pensieve/tags/craigslist/ found 0 occurrences of cookies
https://fabien.bessez.com/pensieve/tags/ec-2/ found 1 occurrences of grpc
https://fabien.bessez.com/pensieve/tags/ec-2/ found 0 occurrences of cookies
https://fabien.bessez.com/pensieve/tags/go/ found 4 occurrences of grpc
https://fabien.bessez.com/pensieve/tags/go/ found 0 occurrences of cookies
https://fabien.bessez.com/pensieve/tags/grpc/ found 7 occurrences of grpc
https://fabien.bessez.com/pensieve/tags/grpc/ found 0 occurrences of cookies
https://fabien.bessez.com/pensieve/tags/protobuf/ found 4 occurrences of grpc
https://fabien.bessez.com/pensieve/tags/protobuf/ found 0 occurrences of cookies
https://fabien.bessez.com/pensieve/tags/python/ found 1 occurrences of grpc
https://fabien.bessez.com/pensieve/tags/python/ found 0 occurrences of cookies
https://fabien.bessez.com/pensieve/tags/redis/ found 1 occurrences of grpc
https://fabien.bessez.com/pensieve/tags/redis/ found 0 occurrences of cookies
https://fabien.bessez.com/archive/ found 1 occurrences of grpc
https://fabien.bessez.com/archive/ found 0 occurrences of cookies
https://fabien.bessez.com/ found 1 occurrences of grpc
https://fabien.bessez.com/ found 0 occurrences of cookies
https://fabien.bessez.com/pensieve/ found 4 occurrences of grpc
https://fabien.bessez.com/pensieve/ found 0 occurrences of cookies
https://fabien.bessez.com/pensieve/tags/ found 3 occurrences of grpc
https://fabien.bessez.com/pensieve/tags/ found 0 occurrences of cookies
```

### Setup + Requirements

1. You will need to have installed `python3`
2. You will need to have installed `pip3`
3. Run `pip3 install -r requirements.txt` to install the dependencies
4. Voila!

### Help

Feel free to reach out for any questions/comments!
