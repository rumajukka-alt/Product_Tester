*** Settings ***
Resource    ../resources/keywords.robot

*** Test Cases ***
UI Logic Start Flow Works
    Log    Testing UILogic start flow
    Press Start    ${DEFAULT_SPEC}
    ${status}=    Get UI Status
    Should Be Equal    ${status}    Finished

UI Logic Stop Flow Works
    Log    Testing UILogic stop flow
    Press Stop
    ${status}=    Get UI Status
    Should Be Equal    ${status}    Stopped

UI Logic Cancel Flow Works
    Log    Testing UILogic cancel flow
    Press Cancel
    ${status}=    Get UI Status
    Should Be Equal    ${status}    Cancelled