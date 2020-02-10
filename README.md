My way of great python scripts:


1. Use **.gitignore** to only save in repositories, what really belongs there
1. Use **.editorconfig** file and IDE plugins for easy formatting
1. Use **Pipfile** and its CLI calls for local testing (it eases the usage of python's virtual environments)
1. Create a **src** and **test** folder to run **pytest**
1. Use **mypy** for bigger projects, where you need to maintain readability a lot. It checks for static typing in your files.


# Hints

## AWS Lambda
* For local includes of packages e.g. *from .util.logging import configure_logger* we need to create a subfolder. See more information on this [gist](https://gist.github.com/gene1wood/06a64ba80cf3fe886053f0ca6d375bc0)
* Additionally Lambda runtime requires to have a __init__.py file if we use local imports. Workarounds:
    * Either use global imports (without the >.< at the beginning (but is deprecated by Python3))
    * Or create a __init__.py file in every folder where .py files are located

## mypy
* It requires to either have a
    * \_\_init\_\_.py file - marks a folder as python package (legacy stuff of python2.x, [but mypy requires it so far](https://github.com/python/mypy/issues/1645)) or
    * \_\_init\_\_.pyi file - It defines stubs for packages, but can be left empty as well.
