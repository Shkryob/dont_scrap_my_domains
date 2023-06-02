import sys

from dig import dig
from domain_extractor import domain_extractor
from my_whois import my_whois
from personal_info_extractor import personal_info_extractor
from report_writer import ReportWriter

domains = domain_extractor(sys.argv[1])
print('Domains extracted:')
print(len(domains))
print(domains)

report_writer = ReportWriter()
for domain in domains:
    print('Getting info for ' + domain)
    report_writer.add_target(domain)
    print('Extracting dig info')
    report_writer.add_dig_info(dig(domain))
    print('Dig info has been extracted')
    print('Extracting whois info')
    whois_info = my_whois(domains[0]).text
    print('Whois info has been extracted')
    report_writer.add_whois_info(whois_info)
    print('Asking ChatGPT to extract personal info from whois text')
    report_writer.add_personal_info(domain, personal_info_extractor(whois_info))
    print('Personal info has been extracted')
