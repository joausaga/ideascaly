IdeaScaly: IdeaScale RESTful API Client
=========
[![Latest Version](https://pypip.in/version/ideascaly/badge.svg)](https://pypi.python.org/pypi/ideascaly/)
[![Supported Python versions](https://pypip.in/py_versions/ideascaly/badge.svg)](https://pypi.python.org/pypi/ideascaly/)
[![Development Status](https://pypip.in/status/ideascaly/badge.svg)](https://pypi.python.org/pypi/ideascaly/)
[![Coverage Status](https://coveralls.io/repos/joausaga/ideascaly/badge.svg)](https://coveralls.io/r/joausaga/ideascaly)
[![License](https://pypip.in/license/ideascaly/badge.svg)](https://pypi.python.org/pypi/ideascaly/)

IdeaScale RESTful API client written in Python. So far, IdeaScaly supports about **45%** of [IdeaScale API] 
(http://support.ideascale.com/customer/portal/articles/1001563-ideascale-rest-api) methods. Basically, with IdeaScaly is
 possible to:
 * Add new members;
 * Get information about community members;
 * Create ideas;
 * Vote up/down on ideas;
 * Post comments on ideas and comments;
 * Get the list of recent, top, and hot ideas;
 * Get the list of ideas under review, in progress, and complete;
 * Get the list of campaigns;
 * Get archived ideas;
 * Get active ideas;
 and much more. 
 
The complete list of implemented methods is available [here]
(https://docs.google.com/spreadsheets/d/1gICkmX7EiSukQ0iTsOkxNrkES2blc5joh-AIeFVTcI8/edit?usp=sharing).

Installation
------------

The easiest way to install the latest version is through pip/easy_install, which will pull from PyPI

`pip install ideascaly`

Also, it is possible to clone the repository from Github and install it manually:

```
git clone https://github.com/joausaga/ideascaly
cd ideascaly
python setup.py install
```

Python 2 (>=.6) & 3 (=<.4) are supported.

Documentation
-------------
* IdeaScaly, coming soon! (meanwhile the examples may help)
* [IdeaScale API](http://support.ideascale.com/customer/portal/articles/1001563-ideascale-rest-api)

License
-------
MIT