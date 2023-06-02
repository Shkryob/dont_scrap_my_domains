import csv
import re

from my_fld import my_fld

domain_regex = r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}'


def domain_extractor(filename):
    domains = []
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file, delimiter=",")

        for row in reader:
            extracted = re.findall(domain_regex, row[0])
            domains += [my_fld(domain) for domain in extracted]

    domains = list(set(domains))

    return [domain for domain in domains if domain is not None]
