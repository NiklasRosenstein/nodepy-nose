# nodepy-nose

This package enables you to use the Python `nose` module for running test
cases on your Node.py packages.

    $ nodepy-pm install --save-dev nodepy-nose
    $ nodepy-nosetests .

For this you need to place your `*_test.py` files in the same directory as
your source files. For example:

    nodepy-package.toml
    lib/
      semver.py
      semver_test.py

You can also place them in a `test` directory and glob the test files. Eg:

    $ ls test/
    semver.py
    $ nodepy-nosetests test/*.py

## Changelog

### 0.0.4

* Transition to Node.py and nodepy-pm 2

### v0.0.3

* Add `.` to `require.path` of the `nodepy-nose` package, enabling to
  specify filenames on the `nodepy-nose` command-line
