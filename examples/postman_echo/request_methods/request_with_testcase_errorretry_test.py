# NOTE: Generated By HttpRunner v3.1.6
# FROM: request_methods/request_with_testcase_errorretry.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from request_methods.request_with_teststep_errorretry_test import (
    TestCaseRequestWithTeststepErrorretry as RequestWithTeststepErrorretry,
)


class TestCaseRequestWithTestcaseErrorretry(HttpRunner):

    config = Config("request testcase: with error retry").base_url(
        "https://postman-echo.com"
    )

    teststeps = [
        Step(
            RunTestCase("get with params")
            .with_retry(tries=3, delay=5)
            .call(RequestWithTeststepErrorretry)
        ),
    ]


if __name__ == "__main__":
    TestCaseRequestWithTestcaseErrorretry().test_start()