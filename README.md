[![Build Status](https://travis-ci.org/marteinn/The-Big-Username-Blacklist-Python.svg?branch=master)](https://travis-ci.org/marteinn/the-big-username-blacklist-python)
[![PyPI version](https://badge.fury.io/py/the-big-username-blacklist.svg)](https://badge.fury.io/py/the-big-username-blacklist)

# The-Big-Username-Blacklist-Python

This library lets you validate usernames against a blacklist. The blacklist data is based on the data from [The-Big-Username-Blacklist](https://github.com/marteinn/The-Big-Username-Blacklist) and contains privilege, programming terms, section names, financial terms and actions.

You can try the blacklist using the tool [Username checker](http://marteinn.github.io/The-Big-Username-Blacklist-JS/).


## How it works

the_big_username_blacklist exposes a function named validate, you can use that function to see if a word is occuring in the blacklist.

## Usage

Validating a username is easy, if the word is in the blacklist, return False (validation failed), otherwise True. Example:

```python
>>>> from the_big_username_blacklist import validate
>>>> validate("root")
False
>>>> validate("martin")
True

```


#### Access the blacklist

If you only want to retrive the blacklist data, you can find it in the `list` property.

```python

>>>> from the_big_username_blacklist import get_blacklist
>>>> get_blacklist()
[ '400',
  '401',
  '403'...
```

## Installation

This package is available through pip

    $ pip install the-big-username-blacklist


## Tests

Make sure you have the necessary dependencies (pytest)

    pip install -r requirements/tests.txt

Then run the tests

    py.test tests


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

The-Big-Username-Blacklist-Python is released under the [MIT License](http://www.opensource.org/licenses/MIT).
