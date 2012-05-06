NLTK_2.0_Cookbook
=================

IPython Notebook (and converted .py) examples based on those presented in Jacob Perkin's NLTK 2.0 Cookbook text

It is assumed that you have installed Python's NLTK and any associated dependencies. 

If you have Ipython Notebook installed, simply start it in project_root_dir/notebooks
$ipython notebook --pylab inline

Note many of the example will not require pylab, so if you haven't installed numpy, scipy, and matplotlib but you do have ipython notebook then
$ipython notebook

should work for most examples.

If you have NOT INSTALLED Ipython Notebook, you can execute the .py files in the project_root/src/ch0X that correspond the .ipynb files at the root level.
The .py files contain the executable Python code as well as commented out markdown from the .ipynb file.

NLTK 2.0 Cookbook Source Code:
Many of the examples require source code provided with the NLTK 2.0 Cookbook Source Code text. Those examples assume that the source code is in the directory project_root_dir/notebooks/lib. Such examples will typically have the following at the begining of the example:
import sys
sys.path.append('lib')

The NLTK 2.0 Cookbook source code is available with the purhcase of the book. Otherwise much of it can be downloaded from:
https://bitbucket.org/sunqiang/nltkcookbook
