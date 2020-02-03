from typing import Sequence
from objcache.models.result_cache import ResultCache

DB_FILE_PATH = 'boj_results.zodb'

class BOJResultCache(ResultCache):

    def __init__(self, cache_path: Sequence[str]):
        super().__init__(DB_FILE_PATH, cache_path)