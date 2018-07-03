from tempfile import NamedTemporaryFile
import os

class Storage:
    def put(self, path, data):
        with NamedTemporaryFile('w', delete=False) as f:
            f.write(data)
        os.replace(f.name, path)

    def get(self, path):
        with open(path) as f:
            return f.read()
