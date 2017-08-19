# Copyright (c) 2017 Niklas Rosenstein
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from nose.plugins.base import Plugin

import nose
import os
import unittest
import sys


class CustomFactory(nose.suite.ContextSuiteFactory):

  def ancestry(self, context):
    # Disable any "ancestry" for Node.py modules.
    return
    yield


class TestRunner(unittest.TestCase):

  def __init__(self, name, func):
    setattr(self, name, func)
    super(TestRunner, self).__init__(name)


class TestLoader(Plugin):

  name = 'nodepy-nose'
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
