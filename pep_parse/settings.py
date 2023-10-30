from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']

PEP_SPIDER_URL = 'peps.python.org'

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).parent.parent

RESULTS = 'results'
RESULTS_DIR = BASE_DIR / RESULTS

PEP_NAME = 'pep'
PEP_FILE_NAME = f'{PEP_NAME}_%(time)s.csv'

FEEDS = {
    f'{RESULTS}/{PEP_FILE_NAME}': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

SUMMARY_NAME = 'status_summary'
SUMMARY_HEADER = ('Status', 'Quantity')
SUMMARY_BOTTOM = 'Total'
