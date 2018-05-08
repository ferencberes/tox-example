tox-example
===========

Small python project example with [tox](https://testrun.org/tox/latest/), [pyenv](https://github.com/yyuu/pyenv) and [pytest](http://pytest.org/latest/).

# Information

In this repository there is an implementation of weighted indegree for directed graphs based on [NetworkX](https://networkx.github.io/), which will be tested by [pytest](http://pytest.org/latest/) in multiple [pyenv](https://github.com/yyuu/pyenv) environments.

# Prerequisites

   1. install python 2.7.9 and 2.7.10:
   
   ```bash
   pyenv install 2.7.9
   pyenv install 2.7.10
   ```
   
   2. create two new virtualenvs with names __tox_example_env__ and __tox_2-7-10__:

   ```bash
   pyenv virtualenv 2.7.9 tox_example_env
   pyenv virtualenv 2.7.10 tox_2-7-10
   pyenv virtualenvs
   ```
   
   3. install [tox](https://pypi.python.org/pypi/tox) and [tox-pyenv](https://pypi.python.org/pypi/tox-pyenv) in both environments:

   ```bash
   pyenv activate tox_example_env
   pip install tox tox-pyenv
   pyenv activate tox_2-7-10
   pip install tox tox-pyenv
   pyenv deactivate
   ``` 

   4. After cloning the repository set __tox_example_env__ and __tox_2-7-10__  as local pyenv environments:
   
   ```bash
   cd tox-example
   pyenv local tox_example_env tox_2-7-10
   ```

# Dependencies and testing

## a.) Install with pip manually

   * These python modules have to be installed in both environments:
   
   ```bash
   pyenv activate tox_example_env
   pip install networkx numpy pytest
   pyenv activate tox_2-7-10
   pip install networkx numpy pytest
   pyenv deactivate   
   ```
   
   Especially __pytest__, otherwise _py.test_ command will call for _pytest_ installed in an other environment!
   
   * Use the following [_tox.ini_](https://github.com/ferencberes/tox-example/blob/install_with_pip/tox.ini) file:
   ```ini
   [tox]
   envlist = tox_example_env,tox_2-7-10
   [testenv]
   commands = py.test
   ```
   
   * Then you can run tests:
   
   __By pytest :__ It will work only with a selected pyenv environment:
     
   ```bash
   cd tox-example
   pyenv activate tox_example_env
   py.test
   pyenv activate tox_2-7-10
   py.test
   pyenv deactivate 
   ```
   
   __By tox :__ It can handle run tests for multiple pyenv environments as well
     
   ```bash
   cd tox-example
   tox
   ```   
   In this case, you will get _WARNINGS_ because there was no __deps__ key specified under __[testenv]__ in the _tox.ini_ file.
   

## b.) Install with tox automatically

   * Use the following [_tox.ini_](https://github.com/ferencberes/tox-example/blob/master/tox.ini) file:
   
   ```ini
   [tox]
   envlist = tox_example_env,tox_2-7-10
   [testenv]
   deps =
       pytest
       numpy
	   networkx
   commands = py.test
   ```
   * With the above file _tox_ install all modules __automatically__ when we run the following command:
   
   ```bash
   cd tox-example
   tox
   ```  
