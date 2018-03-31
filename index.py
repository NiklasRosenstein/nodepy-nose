
import nose.loader, nose.importer
import os
import unittest
import sys


class ContextSuiteFactory(nose.suite.ContextSuiteFactory):

  def ancestry(self, context):
    return; yield


class Importer(nose.importer.Importer):

  def importFromPath(self, filename, module):
    return require(filename)


# Allow requiring modules from the current working directory. This is
# needed so that #TestLoader.loadTestsFromName() can find the files
# specified on the command-line.
require.path.insert(0, '.')

if require.main == module:
  testLoader = nose.loader.TestLoader(importer=Importer())
  testLoader.suiteClass = ContextSuiteFactory()
  nose.main(testLoader=testLoader)
