# This demonstrates a problem I have with molotov and non-package modules

## Install dependencies

The library we use depends on Python 3.

This tool uses [pip](https://pypi.org/project/pip/) to manage its python dependencies.
This is usually already installed with Python.

We also strongly suggest to use virtualenv to encapsulate this project's
dependencies.

### Create a virtualenv for this project
```
virtualenv --python python3 venv
```

### Enter the virtualenv
```
source venv/bin/activate
```
Note: to exit the virtualenv, just run `deactivate`.

### Install molotov
```
pip install -r requirements.txt
```

Upgrading later, when `requirements.txt` changes, is done like this:
```
pip install -U -r requirements.txt
```

## Running

Enable the virtualenv if that's not done yet:
```
source venv/bin/activate
```
Enabling the virtualenv isn't strictly necessary but makes things easier. It's
also possible to run the molotov executable directly.

This exhibits the problem:
```
molotov --single-run -v molotov-script.py
```

And here is the output:
```
$ molotov --single-run -v molotov-script.py
**** Molotov v2.0. Happy breaking! ****
Traceback (most recent call last):
  File "<path>/venv/bin/molotov", line 8, in <module>
  sys.exit(main())
  File "<path>/venv/lib/python3.7/site-packages/molotov/run.py", line 223, in main
  return run(args)
  File "<path>/venv/lib/python3.7/site-packages/molotov/run.py", line 264, in run
  spec.loader.exec_module(module)
  File "<frozen importlib._bootstrap_external>", line 728, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "molotov-script.py", line 6, in <module>
  from common import returnSomething
  ModuleNotFoundError: No module named 'common'
```

The python script `normal-script.py` does the same operation but loads the
module without an issue:

```
$ python normal-script.py
5
```
