# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/srchIdNotInt.yaml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseSrchidnotint(HttpRunner):

    config = Config("PhoneSearch").base_url("${ENV(BASEURL)}")

    teststeps = [
        Step(
            RunRequest("searchByidAndName")
            .with_variables(**{"a": "aa", "b": "Ami"})
            .get("/searchPhone")
            .with_headers(**{"UContent-Type": "application/json"})
            .with_json({"a": "$a", "b": "$b"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.Error_code", 21)
        ),
    ]


if __name__ == "__main__":
    TestCaseSrchidnotint().test_start()
