# EC206
Energy cost calculator
___
Python 2.7 is required.

Installing other requirements: <br>
`pip install -r requirements` <br><br>

Installing PyQt4 (Ubuntu):<br>
`sudo apt install python-qt4`<br>
or<br>
`apt-cache search pyqt`<br>
`sudo apt install <pyqt4 package name>`<br><br>

Installing PyQt4 (Windows):
* Download PyQt4 .whl file [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4). <br>
  obs: choose the correct .whl file according to your Python version and architecture.

  ![Python Shell](https://puu.sh/uOR9k/449e27712e.png)
  ![Wheel files](https://puu.sh/uORma/627fe91cdb.png)
  
* Then open cmd on the directory where the .whl file is and run `pip install pyqt4_wheel_file.whl`,
  changing `pyqt4_wheel_file` with the downloaded file name.

Also, you need to add `ec206.sql` script to your server.<br><br>
Note: if you have some problems installing the requirements, search for equivalent wheel files [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/)
