from typing import Optional, Sequence
import gc

from objcache import ObjectCache
from tests.utils import ObjectCacheForTesting, delete_object_cache_for_testing, ObjectClassForTesting


class TestObjectCache:
    cache: Optional[ObjectCache] = None
    test_cache_path: Sequence[str] = ('a', 'b')
    stored_result: ObjectClassForTesting = ObjectClassForTesting('abc')

    def setup_method(self):
        self.cache = ObjectCacheForTesting(self.test_cache_path)

    def teardown_method(self):
        self.cache = None
        gc.collect()
        delete_object_cache_for_testing()

    def test_store_and_get(self):
        self.cache.store(self.stored_result)
        self.cache = ObjectCacheForTesting(self.test_cache_path)  # reload cache
        gotten = self.cache.get()
        assert gotten == self.stored_result




