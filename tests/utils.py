import os
from dataclasses import dataclass
import time
from typing import Sequence, Any
from objcache.models.object_cache import ObjectCache

GENERATED_PATH = os.path.join('tests', 'generated_files')
DB_FILE_PATH = os.path.join(GENERATED_PATH, 'results.zodb')


class ObjectCacheForTesting(ObjectCache):

    def __init__(self, cache_path: Sequence[str]):
        super().__init__(DB_FILE_PATH, cache_path)


@dataclass
class ObjectClassForTesting:
    result: Any = None


def delete_object_cache_for_testing():
    _delete_with_retries(DB_FILE_PATH)


def _delete_with_retries(file_path: str, retries=10, sleep=0.1):
    for i in range(retries):
        try:
            return os.remove(file_path)
        except (FileNotFoundError, OSError, PermissionError):
            time.sleep(sleep)
