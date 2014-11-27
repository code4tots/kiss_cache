import os, pickle

class Cache(object):
  def __init__(self, cache_directory=None):
    if cache_directory is None:
      cache_directory = os.path.join(os.path.expanduser('~'), '.kiss_cache')

    cache_directory = os.path.realpath(cache_directory)

    try: os.makedirs(cache_directory)
    except os.error: pass

    self._cache_directory = cache_directory

  def _file_path(self, name):
    return os.path.join(self._cache_directory, name)

  def __getattr__(self, name):
    with open(self._file_path(name), 'rb') as f:
      return pickle.load(f)

  def __setattr__(self, name, value):
    if name.startswith('_'):
      self.__dict__[name] = value
    with open(self._file_path(name), 'wb') as f:
      pickle.dump(value, f, 0)

cache = Cache()
