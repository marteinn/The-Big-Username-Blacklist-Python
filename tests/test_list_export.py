from the_big_username_blacklist import get_blacklist


def test_list_export():
    assert "you" in get_blacklist()
