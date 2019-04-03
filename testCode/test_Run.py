import pytest
from base.baseCode import BaseCode
from base.baseHttp import BaseHttp
import base.log as Loglib

import operationConfig

local_read_config = operationConfig.OperationConfig()
reportPath = operationConfig.RESPORTS_DIR_PATH
base_code = BaseCode()
Log = Loglib.Log()
base_http = BaseHttp()


@pytest.mark.parametrize('case_data', base_code.get_case_data('TestCase'))
def test_all_run(case_data):
    response = None
    Log.add_start_line(case_data['caseName'])
    if case_data['caseMethod'] == 'post':
        response = base_http.post(case_data['caseUri'], case_data['caseData'])
    elif case_data['caseMethod'] == 'get':
        response = base_http.get(case_data['caseUri'], case_data['caseData'])
    elif case_data['caseMethod'] == "post_json":
        response = base_http.post_with_json(case_data["caseUri"], case_data["caseData"])
    else:
        Log.logger.info("未找到正确的 Method 类型")

    assert case_data["caseStatusCode"] == response.status_code

    Log.add_end_line(case_data["caseName"])


@pytest.mark.parametrize('case_data', base_code.get_case_data('TestCase', "post"))
def test_post_run(case_data):
    Log.add_start_line(case_data['caseName'])
    response = base_http.post(case_data['caseUri'], case_data['caseData'])

    assert case_data["caseStatusCode"] == response.status_code

    Log.add_end_line(case_data["caseName"])


@pytest.mark.parametrize('case_data', base_code.get_case_data('TestCase', "get"))
def test_get_run(case_data):
    Log.add_start_line(case_data['caseName'])
    response = base_http.post(case_data['caseUri'], case_data['caseData'])

    assert case_data["caseStatusCode"] == response.status_code

    Log.add_end_line(case_data["caseName"])


@pytest.mark.parametrize('case_data', base_code.get_case_data('TestCase', "post_with_json"))
def test_postWithjson_run(case_data):
    Log.add_start_line(case_data['caseName'])
    response = base_http.post(case_data['caseUri'], case_data['caseData'])

    assert case_data["caseStatusCode"] == response.status_code

    Log.add_end_line(case_data["caseName"])


@pytest.mark.parametrize('case_data', base_code.get_case_data('TestCase', rowNubmer=1))
def test_rowNubmer_run(case_data):
    Log.add_start_line(case_data['caseName'])
    response = base_http.post(case_data['caseUri'], case_data['caseData'])

    assert case_data["caseStatusCode"] == response.status_code

    Log.add_end_line(case_data["caseName"])
