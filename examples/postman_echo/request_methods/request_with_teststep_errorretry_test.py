# NOTE: Generated By HttpRunner v3.1.6
# FROM: request_methods/request_with_teststep_errorretry.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseRequestWithTeststepErrorretry(HttpRunner):

    config = Config("request teststep: with error retry").base_url(
        "https://postman-echo.com"
    )

    teststeps = [
        Step(
            RunRequest("get with params")
            .with_retry(tries=3, delay=5)
            .get("/get")
            .with_params(**{"info": "ip"})
            .with_headers(**{"User-Agent": "HttpRunner/${get_httprunner_version()}"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.args.foo1", "bar11")
            .assert_equal("body.args.sum_v", "3")
            .assert_equal("body.args.foo2", "bar21")
        ),
    ]


if __name__ == "__main__":
    TestCaseRequestWithTeststepErrorretry().test_start()
