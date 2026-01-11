*** Settings ***
Resource    ../resources/keywords.robot

*** Test Cases ***
Smoke Test Runs Successfully
    Log    Starting smoke test
    ${result}=    Run Test    ${DEFAULT_SPEC}
    Should Not Be Empty    ${result}
    Log    Smoke test finished