import pytest
from testcode import conftest
from base.baseCode import BaseCode
from base.baseHttp import BaseHttp
import base.log as Loglib

import getConfig

local_read_config = getConfig.GetConfig()
reportPath = getConfig.RESPORTS_DIR_PATH
base_code = BaseCode()
base_http = BaseHttp()
Log = Loglib.Log()


@pytest.mark.parametrize("case_data", base_code.get_case_data("TestCase"))
def test_run(case_data):
    log = Log.get_logger()
    response = None
    Log.add_start_line(case_data["caseName"])
    if case_data["caseMethod"] == "post":
        response = base_http.post(case_data["caseUri"], case_data["caseData"])
    elif case_data["caseMethod"] == "get":
        response = base_http.get(case_data["caseUri"], case_data["caseData"])
    elif case_data["caseMethod"] == "post_json":
        response = base_http.post_with_json(case_data["caseUri"], case_data["caseData"])
    else:
        Log.logger.info("未找到正确的 Method 类型")

    assert case_data["caseStatusCode"] == response.status_code

    Log.add_end_line(case_data["caseName"])
