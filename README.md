tox-example
===========

Small python project example with [tox](https://testrun.org/tox/latest/), [pyenv](https://github.com/yyuu/pyenv) and [pytest](http://pytest.org/latest/).

# Information

In this repository there is an implementation of wieghted indegree for directed graphs based on [NetworkX](https://networkx.github.io/), which will be tested by [pytest](http://pytest.org/latest/) in multiple [pyenv](https://github.com/yyuu/pyenv) environments.

# Prerequisites

   1. install python 2.7.9:
   
   ```bash
   pyenv install 2.7.9
   ```
   
   2. create a new virtualenv named __tox_example_env__:

   ```bash
   pyenv virtualenv 2.7.9 tox_example_env
   ```
   
   3. install [tox](https://pypi.python.org/pypi/tox) and [tox-pyenv](https://pypi.python.org/pypi/tox-pyenv) into the new environment:

   ```bash
   pyenv activate tox_example_env
   pip install tox tox-pyenv
   ``` 

   4. After cloning the repository set __tox_example_env__ as local pyenv environment:
   
   ```bash
   cd tox-example
   pyenv local tox_example_env
   ```

# Dependencies and testing

__TODO: create different branches for the 2 case!!!__

## a.) Install with pip manually

   * These python modules are needed for this repository:
   
   ```bash
   pyenv activate tox_example_env
   pip install networkx numpy pytest
   ```
   
   It is __IMPORTANT__ to install __pytest__ here! Later running tests might not work.
   
   * Use the following _tox.ini_ file:
   ```ini
   [tox]
   envlist = tox_example_env
   [testenv]
   commands = py.test
   ```
   
   * Then you can run tests:
   
   __By pytest :__ It will work only with the selected pyenv environment
     
   ```bash
   cd tox-example
   py.test  
   ```
   
   __By tox :__ It can handle run tests for multiple pyenv environments as well
     
   ```bash
   cd tox-example
   tox
   ```   
   

## b.) Install with tox automatically




