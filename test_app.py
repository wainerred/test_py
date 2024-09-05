       def test_main(capsys):
           from app import main
           main()
           captured = capsys.readouterr()
           assert captured.out == "Hello, World!\n"
       
