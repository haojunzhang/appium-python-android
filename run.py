import os, HtmlTestRunner
from script import test_login

op = os.path.abspath('./result')
runner = HtmlTestRunner.HTMLTestRunner(
    output = op,
)
runner.run(test_login.suite())