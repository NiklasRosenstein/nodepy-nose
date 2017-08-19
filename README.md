# nodepy/nose

This package provides a simple command to execute `nosetests` from a Node.py
context. Simply install the package and use `nodepy-nosetests` as a
replacement for `nosetests`.

    ppym install @nodepy/nose
    $ nodepy-nosetests .
    .......
    ----------------------------------------------------------------------
    Ran 7 tests in 0.010s

    OK

## Changelog

### v0.0.3

* Add `.` to `require.path` of the `nodepy-nose` package, enabling to
  specify filenames on the `nodepy-nose` command-line
