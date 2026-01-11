*** Settings ***
Resource    ../resources/keywords.robot

*** Test Cases ***
Current Measurement Is Within Limits
    ${i}=    Measure Current
    Should Be True    ${i} > 0
    Should Be True    ${i} < 50