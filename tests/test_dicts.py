from work_on_tests.utils import dicts


def test_get_val():
    assert dicts.get_val({}, '', 'git') == 2



