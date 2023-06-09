# Learning-PyTest

The project includes a set of unit tests written using pytest, a testing framework for Python.  These tests aim to verify the correctness of the functions implemented in the project.

When you run the pytest comand ('python -m pytest'), the pytest framework automatically discovers and executes the test functions within the project directory.  It seraches for functions with names starting with 'test_' or ending with '_test'.

To run the tests, ensure that you have pytest installed.  If not, you can install it using the following command:

`pip install pytest`

Once pytest is installed, navigate to the project directory and execute the command `python -m pytest`.  Pytest will then locate the test functions and execute them, providing detailed feedback on the test results, including any failures encountered.

You can also customize the test discovery process and behavior of pytest by utilizing various command-line options and configuration files, such as `pytest.ini` or `pyproject.toml`.

Feel free to modify the provided tests or add additional test cases to further validate the functionality of the functions.

By running and maintaining a comprehensive suite of tests, you can ensure that your code functions correctly and reliably, reducing the chances of introducing bugs.