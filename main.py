from craigsearch import forsale


def query(craigstopic, sites, **kwargs):
    for listing in craigstopic(sites, **kwargs):
        yield from listing.get_results()


def write(filename, listings):
    with open(filename, "w") as file:
        for listing in listings:
            file.write(f'{listing["price"]} :: {listing["name"]} :: {listing["url"]}\n')


if __name__ == "__main__":
    sites = ["sfbay", "monterey", "sacramento", "modesto", "stockton"]
    bike_filters = {
        "query": "salsa",
        "search_titles": True,
        "min_price": 400,
        "has_image": True,
    }
    write("bikes_near_me.txt", query(forsale, sites, category="bia", filters=bike_filters))
