# General Information

## Maintainer
Oliver Bründler [oliver.bruendler@psi.ch]

## License
This library is published under [PSI HDL Library License](License.txt), which is [LGPL](LGPL2_1.txt) plus some additional exceptions to clarify the LGPL terms in the context of firmware development.

## Changelog
See [Changelog](Changelog.md)

## What belongs into this Library
Any python code that is not specific to a problem. This repo should contain general purpose python functionality that helps with everyday python programming

Examples for things that belong into this library:
* Switching to specific working directory temporarily
* Execute an external application and record stdout/stderr
* Extensions of the python language (specific iterators, etc.)

Examples for things that do not belong into this library:
* Any python code specific to a given problem or program to use

## Tagging Policy
Stable releases are tagged in the form *major*.*minor*.*bugfix*. 

* Whenever a change is not fully backward compatible, the *major* version number is incremented
* Whenever new features are added, the *minor* version number is incremented
* If only bugs are fixed (i.e. no functional changes are applied), the *bugfix* version is incremented

# Installation
to install, use the command below

```
pip install <root>\dist\PsiPyUtils-<version>.tar.gz
``` 

Alternatively the package can be used directly as git-submodule (as it was done in the past). This allows for being reverse compatible and do not break projects that depend on using the package as submodule.

# Packaing
To package the project after making changes, update the version number in *setup.py* and run

```
python3 setup.py sdist
```


 