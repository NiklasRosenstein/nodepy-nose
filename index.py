
import nose.loader, nose.importer
import os
import unittest
import sys


class Importer(nose.importer.Importer):

  def importFromPath(self, filename, module):
    return require(filename)


# Allow requiring modules from the current working directory. This is
# needed so that #TestLoader.loadTestsFromName() can find the files
# specified on the command-line.
require.path.insert(0, '.')

if require.main == module:
  nose.main(testLoader=nose.loader.TestLoader(importer=Importer()))
