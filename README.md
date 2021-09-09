# simpy-examples
SimPy simulation examples for simple queueing systems.

This github repository was created to provide teaching examples for Final Year Project students
at the Department of Eletrical Engineering, City University of Hong Kong, specifically for
projects related to the design and simulation of stochastic (i.e. random) systems.

### 1. Installing Python and SimPy
These examples are written in Python 3.  The recommended method for installing Python is via
the Windows Store (https://www.microsoft.com/en-us/p/python-39/9p7qfqmjrfp7) or via apt
on Linux (`sudo apt install python3`).  Packages such as SimPy can be installed using the `pip` command:

```
pip install simpy
```

Note some libraries such as `random` are included with base Python and do not need to be
installed with `pip`.

#### 1.1 Python versions
To ensure that you are running Python 3, type:

```
python --version
```

If you getting version 2 as a result instead, you should be able to force version 3 using
`python3` instead of `python` in the command line, assuming version 3 is also installed.
Similarly, use `pip3` instead of `pip`.

On Linux (Ubuntu 20.04 or later), you may instead install the `python-is-python3` package.

### 2. More info
For more information on stochastic systems and queueing theory, an excellent resource is
Prof. Moshe Zukerman's free textbook: http://www.ee.cityu.edu.hk/~zukerman/classnotes.pdf.
For more information on the SimPy library, see: https://simpy.readthedocs.io.

