import  hello

def test_main(capsys):
    hello.main(["Mark"])

    out, err = capsys.readouterr()
    assert out == "Hello sexy boy Mark\n"
    assert err == ""

def test_main_error_with_empty_string(capsys):
    hello.main([''])

    out, err = capsys.readouterr()
    assert out == ""
    assert err == "Person's name must not be empty\n"