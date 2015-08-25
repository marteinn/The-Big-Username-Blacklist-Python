# The-Big-Username-Blacklist-Python

This library lets you validate usernames against a blacklist. The blacklist data is based on the data from [The-Big-Username-Blacklist](https://github.com/marteinn/The-Big-Username-Blacklist) and contains privilege, programming terms, section names, financial terms and actions.


## How it works

the_big_username_blacklist exposes a function named validate, you can use that function to see if a word is occuring in the The-Big-Username-Blacklist.

## Usage

Validating a username is easy, if the word is in the blacklist, return False (validation failed), otherwise True. Example:

```python
>>>> from the_big_username_blacklist import validate
>>>> validate("root")
False
>>>> validate("martin")
True

```

## Installation

This package is available through pip

    $ pip install the-big-username-blacklist


## Tests

Make sure you have the necessary dependencies (pytest)

    pip install -r requirements/tests.t

Then run the tests

    py.test


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

The-Big-Username-Blacklist-Python is released under the [MIT License](http://www.opensource.org/licenses/MIT).
