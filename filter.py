import os
import json
import time

def filter_data(data):
    sites_to_delete = []
    for site, keyword_counts in data.items():
        keywords_to_delete = []
        for keyword, count in keyword_counts.items():
            if count == 0:
                keywords_to_delete.append(keyword)

        for keyword_to_delete in keywords_to_delete:
            print(keyword_to_delete)
            del data[site][keyword_to_delete]

        print(data.get(site))
        if not data.get(site):
            sites_to_delete.append(site)

    for site_to_delete in sites_to_delete:
        del data[site_to_delete]

    return data

def save_data(data):
    file_path = 'filtered_data.json'
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
    data = fetch_data()
    filtered_data = filter_data(data)
    save_data(filtered_data)
    print("Please check filtered_data.json for your filtered data")

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))