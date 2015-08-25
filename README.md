# The-Big-Username-Blacklist-Python

This is a simple python wrapper built around [The-Big-Username-Blacklist](https://github.com/marteinn/The-Big-Username-Blacklist).


## How it works

The library exposes a function named validate, that you can use to see if a word is occuring in the The-Big-Username-Blacklist.

## Usage

This is how you validate a word, if the word is in the blacklist, return False (validation failed), otherwise True.

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

    `pip install -r requirements/tests.t`

Then run the tests

    `py.test`


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

The-Big-Username-Blacklist-Python is released under the [MIT License](http://www.opensource.org/licenses/MIT).
