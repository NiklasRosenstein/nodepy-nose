
from nose.plugins.base import Plugin

import nose
import os
import unittest
import sys


class CustomFactory(nose.suite.ContextSuiteFactory):

  def ancestry(self, context):
    # Disable any "ancestry" for Node.py modules.
    return; yield


class TestRunner(unittest.TestCase):

  def __init__(self, name, func):
    setattr(self, name, func)
    super(TestRunner, self).__init__(name)


class TestLoader(Plugin):

  name = 'nodepy-nosetests'
  enabled = True

  def options(self, parser, env):
    pass

  def loadTestsFromName(self, name, module=None, importPath=None):
    if os.path.isfile(name):
      module = require(name)
      for key in dir(module):
        if key.startswith('test'):
          yield TestRunner(key, getattr(module, key))

  def prepareTestLoader(self, loader):
    self.loader = loader
    loader.suiteClass = CustomFactory(self.loader.config)


# Allow requiring modules from the current working directory. This is
# needed so that #TestLoader.loadTestsFromName() can find the files
# specified on the command-line.
require.path.insert(0, '.')

if require.main == module:
  nose.main(plugins=[TestLoader()])
