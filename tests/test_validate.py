from the_big_username_blacklist import validate


def test_check_words():
    assert not validate("root")
    assert not validate(" you")
    assert not validate("SSL")
    assert not validate("   sitemap")
    assert not validate("terms-of-use")
    assert validate("wwwvar")
