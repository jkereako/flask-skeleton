# Installation
This document provides a generic overview for installing this application. You can apply these steps to most Flask applications.

#### Clone the repository
```sh
$ git clone https://github.com/jkereako/flask-skeleton.git
Cloning into 'flask-skeleton'...
...
Checking connectivity... done.
```
#### Create the virtual environment
Although not required, you ought to install the Python package [`virtualenv`](http://virtualenv.readthedocs.org/en/latest/) if you want this to work smoothly.

**NOTE**
`pip` chokes on directory names with a space. There are ways to fix this, but it's much easier if you just acquiesce and clone this repository in a directory without a space.

```sh
$ cd flask-skeleton
$ virtualenv env
New python executable in env/bin/python
Installing setuptools, pip...done.
```
#### Start the virtual environment and install package dependencies
```sh
$ source  env/bin/activate
(env) $ pip install -r requirements.txt
...
```

#### Run the webserver
```sh
(env) $ python run.py 
 * Running on http://localhost:5000/
 * Restarting with reloader
```

Now type in `http://localhost:5000/` into your web browser and start fooling around with this thing.
