from typing import Optional, Sequence

from objcache import ResultCache
from tests.utils import ResultCacheForTesting, delete_result_cache_for_testing, ResultClassForTesting


class TestResultCache:
    cache: Optional[ResultCache] = None
    test_cache_path: Sequence[str] = ('a', 'b')
    stored_result: ResultClassForTesting = ResultClassForTesting('abc')

    def setup_method(self):
        self.cache = ResultCacheForTesting(self.test_cache_path)

    def teardown_method(self):
        self.cache = None
        delete_result_cache_for_testing()

    def test_store_and_get(self):
        self.cache.store(self.stored_result)
        self.cache = ResultCacheForTesting(self.test_cache_path)  # reload cache
        gotten = self.cache.get()
        assert gotten == self.stored_result




