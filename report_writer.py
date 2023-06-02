import os.path
from pathlib import Path


class ReportWriter:
    report_folder = 'report'
    targets_file_name = 'targets.txt'
    dig_file_name = 'dig.txt'
    whois_file_name = 'whois.txt'
    info_file_name = 'info.txt'

    def __init__(self):
        self.create_report_folder()
        self.clear_report()
        self.targets_file = self.get_file(self.targets_file_name)
        self.dig_file = self.get_file(self.dig_file_name)
        self.whois_file = self.get_file(self.whois_file_name)
        self.info_file = self.get_file(self.info_file_name)

    def clear_report(self):
        [f.unlink() for f in Path(self.report_folder).glob("*") if f.is_file()]

    def create_report_folder(self):
        if not os.path.exists(self.report_folder):
            os.makedirs(self.report_folder)

    def get_file(self, filename):
        file_path = Path(os.path.join(self.report_folder, filename))
        file_path.touch(exist_ok=True)

        return open(file_path, 'a')

    def add_target(self, target):
        self.targets_file.write(target)
        self.targets_file.write('\n')

    def add_dig_info(self, dig_info):
        self.dig_file.write(dig_info)
        self.dig_file.write('\n\n')

    def add_whois_info(self, whois_info):
        self.whois_file.write(whois_info)
        self.whois_file.write('\n\n')

    def add_personal_info(self, domain, personal_info):
        self.info_file.write(domain)
        self.info_file.write('\n')
        self.info_file.write(personal_info)
        self.info_file.write('\n\n')
