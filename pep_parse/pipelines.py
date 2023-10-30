import csv
import datetime as dt
from collections import defaultdict
import logging

from pep_parse.settings import (BASE_DIR, DATETIME_FORMAT, RESULTS,
                                SUMMARY_NAME, SUMMARY_BOTTOM, SUMMARY_HEADER)


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)
        self.logger = logging.getLogger(__name__)

    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        filename = f'{SUMMARY_NAME}_{now_formatted}.csv'
        file_path = self.results_dir / filename
        with CsvWriter(file_path) as writer:
            writer.write_rows([
                SUMMARY_HEADER,
                *self.statuses.items(),
                f'{SUMMARY_BOTTOM} {sum(self.statuses.values())}',
            ])
        self.logger.info(f'Saved summary to {file_path}')


class CsvWriter:

    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.file = open(self.file_path, mode='w', encoding='utf-8')
        self.writer = csv.writer(
            self.file,
            dialect=csv.unix_dialect,
            quoting=csv.QUOTE_NONE,
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def write_rows(self, rows):
        self.writer.writerows(rows)
