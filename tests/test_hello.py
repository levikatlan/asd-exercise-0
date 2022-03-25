import hello


def test_hello(capsys):
    hello.hello()
    out, err = capsys.readouterr()
    assert out == 'Hello, World!\n'
    assert err == ''
