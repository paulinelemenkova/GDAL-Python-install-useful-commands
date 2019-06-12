# purpose: re-install python3* and jupyter notebook to solve problem 'jupyter notebook command not found on mac ox' (broken PATH)
sudo rm -rf /Library/Frameworks/Python.framework
rm /usr/local/bin/python3*
brew uninstall --ignore-dependencies python3
brew install python3
which python3
python3 -m pip install --upgrade pip
python3 -m pip install jupyter
which jupyter
jupyter notebook
# successfully installed python-3.7.3 and jupyter notebook
# Python has been installed as /usr/local/bin/python3

# библиотеки установил в /Users/pauline/miniconda3/lib/python3.7/site-packages/
# remove miniconda
rm -rf ~/miniconda3

# reinstall seaborn
python3 -m pip install seaborn # (+ установит Matplotlib, Pandas, SciPy)
python3 -m pip install sklearn
python3 -m pip install patsy
python3 -m pip install statsmodels

# now correct path to IDLE. Go to lib /usr/local/Cellar/python/3.7.3/
# исправлен PATH to libraries (Command+Shift+G /usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/3.7/lib/site-packages)
# ( было: /Users/pauline/miniconda3/lib/python3.7/site-packages/pip )
#
# проверить версию питона
python -V # версия Python (3.7.3)
pip3 -V # куда смотрит pip
# /usr/local/lib/python3.7/site-packages/pip (python 3.7)

# если надо удалить библиотеку
pip uninstall seaborn
pip uninstall pandas
pip uninstall scipy
pip uninstall matplotlib
