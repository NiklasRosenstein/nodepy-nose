## nodepy-nose

This package enables you to use the Python `nose` module for running test
cases on your Node.py packages.

### Installation

    $ nodepypm install --save-dev git+https://github.com/nodepy/nodepy-nosetests.git
    $ nodepy-nosetests .

### Usage

Place your `*_test.py` files in the same directory as your source files:

    nodepy-package.toml
    lib/
      semver.py
      semver_test.py

You can also place them in a `test` directory and glob the test files:

    $ ls test/
    semver.py
    $ nodepy-nosetests test/*.py

Your tests are loaded just like normal Node.py modules:

```python
from nose.tools import *
import {Version} from './semver'

def test_version():
  # ...
```

## Changelog

### v0.0.6

* Greatly simplified implementation by implementing a custom `Importer`

### 0.0.4/0.0.5

* Transition to Node.py and nodepypm 2

### v0.0.3

* Add `.` to `require.path` of the `nodepy-nose` package, enabling to
  specify filenames on the `nodepy-nose` command-line
