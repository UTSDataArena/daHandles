import sys
import unittest

# configure python path so that we can easily launch our tests via CLI or an IDE
sys.path.append('../python/')

if __name__ == '__main__':

    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()

    runner.run(loader.discover('.'))
