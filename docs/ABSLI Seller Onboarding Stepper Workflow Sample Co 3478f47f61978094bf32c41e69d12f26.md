# ABSLI Seller Onboarding Stepper Workflow Sample Config

Vo Steps
{
"final_interview": {
"code": "final_interview",
"deleted": true,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "Final Interview",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.first_interview_outcome",
"inputField": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "Accept",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
]
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_recruitment",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"reentryCriteria": null
},
"screening": {
"code": "screening",
"deleted": true,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "Screening",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "step_actions.basic_details",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "NOT_EQUALS",
"output": null,
"returnType": "bool"
}
],
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.lead_source",
"inputField": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "Bulk Upload",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
]
},
"stepLockedMessage": null,
"mappedState": null,
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"reentryCriteria": null
},
"bop": {
"code": "bop",
"deleted": true,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "BOP/COP",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_recruitment",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"reentryCriteria": null
},
"basic_details": {
"code": "basic_details",
"deleted": false,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "Basic Details",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_application",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"reentryCriteria": null
},
"agency_leader_document_verification": {
"code": "agency_leader_document_verification",
"deleted": true,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "Agency Leader Documents Verification",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "steps.1st_al_interview",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
],
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.li_application_type",
"inputField": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": [
"fresh",
"composite",
"transfer",
"posp"
],
"dataType": "list"
}
}
],
"standardFunction": "IN",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "NOT",
"output": null,
"returnType": "bool"
}
]
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_onboarding",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"reentryCriteria": null
},
"urn_generation": {
"code": "urn_generation",
"deleted": false,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "URN Generation",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "steps.bm_review",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.li_application_type",
"inputField": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": [
"fresh",
"composite"
],
"dataType": "text"
}
}
],
"standardFunction": "IN",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "AND",
"output": null,
"returnType": "bool"
}
]
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_onboarding",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "step_actions.urn_generation",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
],
"otherConditions": null
},
"reentryCriteria": null
},
"agent_code_generation": {
"code": "agent_code_generation",
"deleted": false,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "Agent Code Generation",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.li_application_type",
"inputField": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": [
"fresh",
"composite"
],
"dataType": "text"
}
}
],
"standardFunction": "IN",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "steps.exam",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "AND",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.li_application_type",
"inputField": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": [
"transfer"
],
"dataType": "text"
}
}
],
"standardFunction": "IN",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "steps.bm_review",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "AND",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "OR",
"output": null,
"returnType": "bool"
}
]
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_onboarding",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.agent_code",
"inputField": "inputs_map.agent_code",
"voId": null
}
}
],
"standardFunction": "IS_NOT_EMPTY",
"output": null,
"returnType": "bool"
}
]
},
"reentryCriteria": null
},
"mock_exam_external": {
"code": "mock_exam_external",
"deleted": true,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "Mock Exam (External LMS or Offline)",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "steps.training",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
],
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.li_application_type",
"inputField": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": [
"fresh",
"composite",
"posp"
],
"dataType": "text"
}
}
],
"standardFunction": "IN",
"output": null,
"returnType": "bool"
}
]
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_onboarding",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.mock_test_outcome",
"inputField": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "Pass",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
]
},
"reentryCriteria": null
},
"bank_details": {
"code": "bank_details",
"deleted": false,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "Bank Details",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "step_actions.recruitment_consent",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
],
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_application",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "step_actions.validate_bank_account",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "step_actions.validate_bank_account",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "FAILED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "OR",
"output": null,
"returnType": "bool"
}
]
},
"reentryCriteria": null
},
"training": {
"code": "training",
"deleted": false,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "Training",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.li_application_type",
"inputField": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": [
"fresh",
"composite"
],
"dataType": "text"
}
}
],
"standardFunction": "IN",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "steps.urn_generation",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "AND",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.li_application_type",
"inputField": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": [
"posp"
],
"dataType": "text"
}
}
],
"standardFunction": "IN",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "steps.bm_review",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "AND",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "OR",
"output": null,
"returnType": "bool"
}
]
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_onboarding",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "step_actions.training_schedule",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "step_actions.posp_training",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "OR",
"output": null,
"returnType": "bool"
}
]
},
"reentryCriteria": null
},
"absli_bp7m6i-recruitment_leads_124r3a_posp_code_generation": {
"code": "absli_bp7m6i-recruitment_leads_124r3a_posp_code_generation",
"deleted": false,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "POSP Code Generation",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "steps.mock_exam_internal",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.li_application_type",
"inputField": null,
"voId": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": [
"posp"
],
"dataType": "text"
}
}
],
"standardFunction": "IN",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "AND",
"output": null,
"returnType": "bool"
}
]
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_onboarding",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.agent_code",
"inputField": "inputs_map.agent_code",
"voId": null
}
}
],
"standardFunction": "IS_NOT_EMPTY",
"output": null,
"returnType": "bool"
}
]
},
"reentryCriteria": null
},
"mock_exam_internal": {
"code": "mock_exam_internal",
"deleted": false,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "Mock Exam",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "steps.training",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.li_application_type",
"inputField": null,
"voId": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": [
"posp"
],
"dataType": "text"
}
}
],
"standardFunction": "IN",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "AND",
"output": null,
"returnType": "bool"
}
]
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_onboarding",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"reentryCriteria": null
},
"personal_info": {
"code": "personal_info",
"deleted": true,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "Personal Information",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_recruitment",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"reentryCriteria": null
},
"additional_details": {
"code": "additional_details",
"deleted": false,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "Additional Details",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "step_actions.recruitment_consent",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
],
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_application",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"reentryCriteria": null
},
"1st_al_interview": {
"code": "1st_al_interview",
"deleted": true,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "1st AL Interview",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.li_application_type",
"inputField": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": [
"fresh",
"composite",
"transfer",
"posp"
],
"dataType": "list"
}
}
],
"standardFunction": "IN",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "NOT",
"output": null,
"returnType": "bool"
}
]
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_onboarding",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"reentryCriteria": null
},
"first_interview": {
"code": "first_interview",
"deleted": true,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "1st Interview",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "steps.psychometric",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
],
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_recruitment",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"reentryCriteria": null
},
"bm_review": {
"code": "bm_review",
"deleted": false,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "Branch Manager Review",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "steps.application_submission",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
],
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.insurance_distributor_type",
"inputField": "inputs_map.insurance_distributor_type",
"voId": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "Partner Office",
"dataType": "text"
}
}
],
"standardFunction": "NOT_EQUALS",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.insurance_distributor_type",
"inputField": "inputs_map.insurance_distributor_type",
"voId": null
}
}
],
"standardFunction": "IS_EMPTY",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "OR",
"output": null,
"returnType": "bool"
}
]
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_onboarding",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"reentryCriteria": null
},
"pan_and_ckyc_verification": {
"code": "pan_and_ckyc_verification",
"deleted": true,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "PAN and CKYC Verification",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "step_actions.recruitment_consent",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
],
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"stepLockedMessage": null,
"mappedState": "cm43b1z1zn",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"reentryCriteria": null
},
"po_onboarding": {
"code": "po_onboarding",
"deleted": true,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "PO Onboarding",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.insurance_distributor_type",
"inputField": "inputs_map.insurance_distributor_type",
"voId": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "Partner Office",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
]
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_onboarding",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"reentryCriteria": null
},
"re-exam_follow_up_details": {
"code": "re-exam_follow_up_details",
"deleted": true,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "Re-Exam Follow up",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_application",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"reentryCriteria": null
},
"exam": {
"code": "exam",
"deleted": false,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "IRDAI Exam",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "steps.mock_exam_internal",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "step_actions.training_schedule",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "OR",
"output": null,
"returnType": "bool"
}
]
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "step_actions.training_schedule",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.li_application_type",
"inputField": null,
"voId": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": [
"fresh",
"composite"
],
"dataType": "text"
}
}
],
"standardFunction": "IN",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "AND",
"output": null,
"returnType": "bool"
}
]
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_onboarding",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.exam_outcome",
"inputField": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "Pass",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
]
},
"reentryCriteria": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map._exam_outcome",
"inputField": "inputs_map._exam_outcome",
"voId": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": [
"Fail",
"Absent"
],
"dataType": "list"
}
}
],
"standardFunction": "IN",
"output": null,
"returnType": "bool"
}
]
}
},
"psychometric": {
"code": "psychometric",
"deleted": true,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "Psychometric",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.interview_attended",
"inputField": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "Attended",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
]
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_recruitment",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"reentryCriteria": null
},
"posp_training": {
"code": "posp_training",
"deleted": true,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "POSP Training",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_onboarding",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"reentryCriteria": null
},
"2nd_al_interview": {
"code": "2nd_al_interview",
"deleted": true,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "2nd AL Interview",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.li_application_type",
"inputField": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": [
"fresh",
"composite",
"transfer",
"posp"
],
"dataType": "list"
}
}
],
"standardFunction": "IN",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "NOT",
"output": null,
"returnType": "bool"
}
]
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_onboarding",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"reentryCriteria": null
},
"kyc": {
"code": "kyc",
"deleted": false,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "KYC Verification",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "step_actions.recruitment_consent",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
],
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_application",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "step_actions.ckyc",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "step_actions.manual_kyc",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "OR",
"output": null,
"returnType": "bool"
}
]
},
"reentryCriteria": null
},
"application_submission": {
"code": "application_submission",
"deleted": false,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"name": "Application Submission",
"type": "conditional",
"description": null,
"enableIf": {
"stepStatusConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "steps.additional_details",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
},
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "steps.bank_details",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
},
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "steps.kyc",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
],
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"stepLockedMessage": null,
"mappedState": "absli_bp7m6i-recruitment_leads_124r3a_agent_recruitment_application",
"definitionOfDone": {
"stepStatusConditions": null,
"actionStatusConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "context-standard-dimension",
"operator": null,
"operatorRequired": false,
"contextPath": {
"type": "nested",
"path": "step_actions.application_verification",
"dataType": "vo"
},
"standardDimension": "status"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "COMPLETED",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
],
"otherConditions": null
},
"reentryCriteria": null
}
}

Vo Actions
{
"assisted_screening": {
"code": "assisted_screening",
"deleted": true,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"title": "Screening",
"description": null,
"type": "form_filling",
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.li_lead_source",
"inputField": null,
"voId": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": [
"Self Sourced",
"Promotional Campaign",
"Referral"
],
"dataType": "list"
}
}
],
"standardFunction": "IN",
"output": null,
"returnType": "bool"
}
]
},
"actionCategory": "PortalInputFormActionCategory",
"variables": null,
"carouselEnabled": false,
"ctas": null,
"horizontalActions": null,
"thresholdAge": {
"maxAllowedDelay": 1,
"unit": "DAYS"
},
"inputFieldMappings": [
{
"disabled": false,
"order": 10,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "screening_outcome",
"inputTypeMapping": null,
"sifgMapping": {
"required": false,
"source": null,
"hint": "Screening Outcome",
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Accept",
"inputFields": []
},
{
"disabled": false,
"order": 10,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Reject",
"inputFields": []
},
{
"disabled": false,
"order": 20,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "On Hold",
"inputFields": []
},
{
"disabled": false,
"order": 30,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Start Onboarding",
"inputFields": []
},
{
"disabled": false,
"order": 40,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Not Interested",
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "reason_for_rejection",
"inputTypeMapping": null,
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": null,
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": null,
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false
}
]
}
],
"$resourceStrings": null
},
"searchOptions": null,
"required": true,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "jb8-kq7oz",
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 20,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "if_pan",
"inputTypeMapping": {
"code": "pan",
"type": "pan",
"required": true,
"source": null,
"hint": "PAN",
"placeholder": null,
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": null,
"maxChars": null
},
"sifgMapping": null,
"searchOptions": null,
"required": true,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": [
{
"expression": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "pan_to_check",
"inputField": "pan_to_check"
}
}
],
"standardFunction": "IS_EMPTY",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "pan",
"inputField": "pan"
}
},
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "pan_to_check",
"inputField": "pan_to_check"
}
}
],
"standardFunction": "NOT_EQUALS",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "OR",
"output": null,
"returnType": "bool"
},
"errorMessage": "It looks like you haven't clicked the cloud icon or the PAN changed without validation.",
"disableBackendValidation": false
}
],
"fieldGroup": "jb8-kq7oz",
"readOnly": false,
"hiddenV2": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "screening_outcome",
"inputField": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "Start Onboarding",
"dataType": "text"
}
}
],
"standardFunction": "NOT_EQUALS",
"output": null,
"returnType": "bool"
},
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 25,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "check_pan_status_label",
"inputTypeMapping": {
"code": "check_pan_status_label",
"type": "label",
"required": false,
"source": null,
"hint": "Validate PAN status",
"placeholder": null,
"invisible": false,
"oifOptions": {
"type": "default",
"url": "/portal/oif/panCheck?lob=absli&portalId=abc-recruitment-portal",
"params": [
{
"disabled": false,
"order": null,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"code": "code",
"name": "pan"
}
],
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"value": "Click on the cloud icon beside to check the PAN status"
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "jb8-kq7oz",
"readOnly": false,
"hiddenV2": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "screening_outcome",
"inputField": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "Start Onboarding",
"dataType": "text"
}
}
],
"standardFunction": "NOT_EQUALS",
"output": null,
"returnType": "bool"
},
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": true,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 30,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "li_application_type",
"inputTypeMapping": null,
"sifgMapping": {
"required": false,
"source": null,
"hint": "Application Type",
"oifOptions": null,
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "fresh",
"inputFields": []
},
{
"disabled": false,
"order": 10,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "composite",
"inputFields": []
},
{
"disabled": false,
"order": 20,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "transfer",
"inputFields": []
},
{
"disabled": false,
"order": 30,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "posp",
"inputFields": []
}
],
"$resourceStrings": null
},
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "jb8-kq7oz",
"readOnly": true,
"hiddenV2": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "screening_outcome",
"inputField": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "Start Onboarding",
"dataType": "text"
}
}
],
"standardFunction": "NOT_EQUALS",
"output": null,
"returnType": "bool"
},
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 40,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "remarks_for_candidate",
"inputTypeMapping": {
"code": "remarks_for_candidate",
"type": "text",
"required": false,
"source": null,
"hint": "Remarks for Candidate Screening",
"placeholder": null,
"invisible": false,
"oifOptions": null,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": null,
"maxChars": null,
"regex": null,
"regexHint": null
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "jb8-kq7oz",
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 2140,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "reason_for_dropping_candidate",
"inputTypeMapping": null,
"sifgMapping": {
"required": false,
"source": null,
"hint": "Reason for Dropping Candidate",
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Not contactable",
"inputFields": []
},
{
"disabled": false,
"order": 10,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Invalid",
"inputFields": []
},
{
"disabled": false,
"order": 20,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Not Interested",
"inputFields": []
},
{
"disabled": false,
"order": 30,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Lack of Relevant Experience",
"inputFields": []
},
{
"disabled": false,
"order": 40,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Insufficient qualifications",
"inputFields": []
},
{
"disabled": false,
"order": 50,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Inconsistencies in the application",
"inputFields": []
},
{
"disabled": false,
"order": 60,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Others",
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "other_candidate_drop_reason",
"inputTypeMapping": {
"code": "other_candidate_drop_reason",
"type": "text",
"required": false,
"source": null,
"hint": "If others, please specify",
"placeholder": null,
"invisible": false,
"oifOptions": null,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": null,
"maxChars": null,
"regex": null,
"regexHint": null
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": null,
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": null,
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false
}
]
},
{
"disabled": false,
"order": 70,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "irdai_check_failed",
"inputFields": []
},
{
"disabled": false,
"order": 80,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "not_interested",
"inputFields": []
},
{
"disabled": false,
"order": 90,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "pan_not_found",
"inputFields": []
},
{
"disabled": false,
"order": 100,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "pan_inactive",
"inputFields": []
},
{
"disabled": false,
"order": 110,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "pan_dedupe_failed",
"inputFields": []
},
{
"disabled": false,
"order": 120,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "idle_application",
"inputFields": []
},
{
"disabled": false,
"order": 130,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "no_arn_registration",
"inputFields": []
},
{
"disabled": false,
"order": 140,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "arn_number_expired",
"inputFields": []
},
{
"disabled": false,
"order": 150,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "arn_mismatch",
"inputFields": []
},
{
"disabled": false,
"order": 160,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "arn_number_cancelled",
"inputFields": []
}
],
"$resourceStrings": null
},
"searchOptions": null,
"required": false,
"hidden": true,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "screening_outcome",
"inputField": "screening_outcome"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "Not Interested",
"dataType": null
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "Not Interested",
"dataType": "text"
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "reasons_list_for_dropping_candidate",
"inputField": "reasons_list_for_dropping_candidate"
}
}
],
"standardFunction": "IS_NOT_EMPTY",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "reasons_list_for_dropping_candidate",
"inputField": "reasons_list_for_dropping_candidate"
}
}
],
"standardFunction": "IF",
"output": null,
"returnType": "text"
}
}
}
],
"standardFunction": "IF",
"output": null,
"returnType": "text"
}
}
}
],
"standardFunction": "IS",
"output": null,
"returnType": "text"
},
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "tlitd_pcz",
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": true,
"quickLeadField": false,
"masked": false,
"tooltip": null
}
]
},
"screening": {
"code": "screening",
"deleted": true,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"title": "Screening",
"description": null,
"type": "task",
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"actionCategory": "ActivityScheduleActionCategory",
"variables": null,
"carouselEnabled": false,
"ctas": null,
"horizontalActions": null,
"thresholdAge": {
"maxAllowedDelay": 1,
"unit": "DAYS"
},
"task": "screening"
},
"basic_details": {
"code": "basic_details",
"deleted": false,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"title": "Basic Details",
"description": null,
"type": "profile_integration",
"enableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": null
},
"actionCategory": "PortalInputFormActionCategory",
"variables": {
"autoSubmit": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": true,
"dataType": null
}
},
"carouselEnabled": false,
"ctas": [],
"horizontalActions": null,
"thresholdAge": {
"maxAllowedDelay": 1,
"unit": "DAYS"
},
"inputFieldMappings": [
{
"disabled": false,
"order": 2180,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "drop_lead",
"inputTypeMapping": {
"code": "drop_lead",
"type": "text",
"required": false,
"source": null,
"hint": "Drop Lead",
"placeholder": null,
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": null,
"maxChars": null,
"regex": null,
"regexHint": null
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": true,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "tlitd_pcz",
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": true,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 10,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "title_details",
"inputTypeMapping": null,
"sifgMapping": {
"required": true,
"source": null,
"hint": "Title",
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Mr.",
"inputFields": []
},
{
"disabled": false,
"order": 10,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Mrs.",
"inputFields": []
},
{
"disabled": false,
"order": 20,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Ms.",
"inputFields": []
},
{
"disabled": false,
"order": 30,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Dr.",
"inputFields": []
},
{
"disabled": false,
"order": 40,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Mx.",
"inputFields": []
}
],
"$resourceStrings": null
},
"searchOptions": null,
"required": true,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": [
{
"expression": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "gender_xev4nfroamd",
"inputField": "gender_xev4nfroamd"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "Female",
"dataType": null
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "title_details",
"inputField": "title_details"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "Mr.",
"dataType": null
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "AND",
"output": null,
"returnType": "bool"
},
"errorMessage": "Invalid title for female, Expected Ms or Mrs, but received Mr",
"disableBackendValidation": false
},
{
"expression": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "gender_xev4nfroamd",
"inputField": "gender_xev4nfroamd"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "Male",
"dataType": null
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "title_details",
"inputField": "title_details"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "Mrs.",
"dataType": null
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "AND",
"output": null,
"returnType": "bool"
},
"errorMessage": "Invalid title for Male Expected Mr.",
"disableBackendValidation": false
},
{
"expression": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "gender_xev4nfroamd",
"inputField": "gender_xev4nfroamd"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "Male",
"dataType": null
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "title_details",
"inputField": "title_details"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "Ms.",
"dataType": null
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "AND",
"output": null,
"returnType": "bool"
},
"errorMessage": "Invalid title for Male Expected Mr.",
"disableBackendValidation": false
}
],
"fieldGroup": "0bkz1cmikm",
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 40,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "if_phone",
"inputTypeMapping": {
"code": "phone",
"type": "phone",
"required": false,
"source": null,
"hint": "Phone",
"placeholder": "Enter your mobile number",
"invisible": false,
"oifOptions": null,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": 10,
"maxChars": 10,
"regex": "^[6-9]\\d{9}$",
"regexHint": "Please Enter Valid Number",
"enableCountryCode": true
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": true,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "0bkz1cmikm",
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": true,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 20,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "if_name",
"inputTypeMapping": {
"code": "name",
"type": "text",
"required": true,
"source": null,
"hint": "Full Name",
"placeholder": "Enter name as per PAN",
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": null,
"maxChars": null,
"regex": "^[^\\W\\d_.&\\-/'’]+(?:[.&\\-/'’\\s-][^\\W\\d_.&\\-/'’]+|[.&-/'’])*$",
"regexHint": "Please enter a valid name"
},
"sifgMapping": null,
"searchOptions": null,
"required": true,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": [],
"fieldGroup": "0bkz1cmikm",
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": "Please enter name as per PAN"
},
{
"disabled": false,
"order": 60,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "if_pan",
"inputTypeMapping": {
"code": "pan",
"type": "pan",
"required": true,
"source": null,
"hint": "PAN",
"placeholder": null,
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": null,
"maxChars": null
},
"sifgMapping": null,
"searchOptions": null,
"required": true,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "0bkz1cmikm",
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.pan",
"inputField": "inputs_map.pan",
"voId": null
}
}
],
"standardFunction": "IS_NOT_EMPTY",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "AND",
"output": null,
"returnType": "bool"
},
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 30,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "if_email",
"inputTypeMapping": {
"code": "email",
"type": "email",
"required": true,
"source": null,
"hint": "Email",
"placeholder": "Enter your Email Address",
"invisible": false,
"oifOptions": null,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": null,
"maxChars": null,
"regex": "^[a-zA-Z0-9._%+-]+@(hotmail[.]com|outlook[.]com|gmail[.]com|yahoo[.]com)$",
"regexHint": "You cannot use your ABC email ID for onboarding. Please enter a personal email address"
},
"sifgMapping": null,
"searchOptions": null,
"required": true,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "0bkz1cmikm",
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": "Use your personal email ID"
},
{
"disabled": false,
"order": 80,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "gender_xev4nfroamd",
"inputTypeMapping": null,
"sifgMapping": {
"required": true,
"source": null,
"hint": "Gender",
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "w5ui2ezyt9",
"inputFields": []
},
{
"disabled": false,
"order": 10,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "qxhb35tl29",
"inputFields": []
},
{
"disabled": false,
"order": 20,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "mncshrhjx",
"inputFields": []
}
],
"$resourceStrings": null
},
"searchOptions": null,
"required": true,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "0bkz1cmikm",
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 50,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "if_dob",
"inputTypeMapping": {
"code": "dob",
"type": "dob",
"required": true,
"source": null,
"hint": "Date of Birth",
"placeholder": "Enter DOB",
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"fromAge": 18,
"toAge": 100
},
"sifgMapping": null,
"searchOptions": null,
"required": true,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "0bkz1cmikm",
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": true,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 140,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "pincode_li_recruitment",
"inputTypeMapping": {
"code": "pincode_li_recruitment",
"type": "text",
"required": true,
"source": null,
"hint": "Pincode",
"placeholder": "Enter your pincode",
"invisible": false,
"oifOptions": {
"type": "default",
"url": "/portal/oif/pincode?lob=absli&portalId=abc-recruitment-portal",
"params": [
{
"disabled": false,
"order": null,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"code": "code",
"name": "pincode_li_recruitment"
}
],
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": 6,
"maxChars": 6,
"regex": "^[0-9]{6,6}$",
"regexHint": "Enter a valid pincode"
},
"sifgMapping": null,
"searchOptions": null,
"required": true,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "0bkz1cmikm",
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": "Enter current pincode"
},
{
"disabled": false,
"order": 120,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "would_you_like_to_work_as_a_agent_or_a_posp",
"inputTypeMapping": null,
"sifgMapping": {
"required": true,
"source": null,
"hint": "Would you like to work as a Agent or a Point of Sales Person (POSP)?",
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "agent",
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "identify_transfer_agent",
"inputTypeMapping": null,
"sifgMapping": {
"required": true,
"source": null,
"hint": "Have you been employed as an agent earlier with any other life insurance company?",
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Yes",
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "years_of_experience_in_the_insurance_industry",
"inputTypeMapping": {
"code": "years_of_experience_in_the_insurance_industry",
"type": "number",
"required": false,
"source": null,
"hint": "How many years of experience do you have in the insurance industry?",
"placeholder": null,
"invisible": false,
"oifOptions": null,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": 1,
"maxChars": 40,
"regex": null,
"regexHint": null
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": null,
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": null,
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false
},
{
"disabled": false,
"order": 10,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "years_of_experience_in_bfsi",
"inputTypeMapping": null,
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": null,
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": null,
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false
}
]
},
{
"disabled": false,
"order": 10,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "No",
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "identify_composite_agent",
"inputTypeMapping": null,
"sifgMapping": {
"required": true,
"source": null,
"hint": "Are you currently working with any health insurance or general insurance company?",
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Yes",
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "years_of_experience_in_the_insurance_industry",
"inputTypeMapping": null,
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": null,
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": null,
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false
},
{
"disabled": false,
"order": 10,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "years_of_experience_in_bfsi",
"inputTypeMapping": null,
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": null,
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": null,
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false
}
]
},
{
"disabled": false,
"order": 10,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "No",
"inputFields": []
}
],
"$resourceStrings": null
},
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": null,
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": null,
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false
}
]
}
],
"$resourceStrings": null
},
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": null,
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": null,
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false
}
]
},
{
"disabled": false,
"order": 10,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "posp",
"inputFields": []
}
],
"$resourceStrings": null
},
"searchOptions": null,
"required": true,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "0bkz1cmikm",
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": "A POSP is authorised to sell limited insurance products than fresh certified agent"
},
{
"disabled": false,
"order": 210,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "li_application_type",
"inputTypeMapping": null,
"sifgMapping": {
"required": false,
"source": null,
"hint": "Application Type",
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "fresh",
"inputFields": []
},
{
"disabled": false,
"order": 10,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "composite",
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "years_of_experience_in_the_insurance_industry",
"inputTypeMapping": null,
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": null,
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": null,
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false
}
]
},
{
"disabled": false,
"order": 20,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "transfer",
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "years_of_experience_in_the_insurance_industry",
"inputTypeMapping": null,
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": null,
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": null,
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false
}
]
},
{
"disabled": false,
"order": 30,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "posp",
"inputFields": []
}
],
"$resourceStrings": null
},
"searchOptions": null,
"required": true,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "would_you_like_to_work_as_a_agent_or_a_posp",
"inputField": "would_you_like_to_work_as_a_agent_or_a_posp"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "posp",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "posp",
"dataType": "text"
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "identify_transfer_agent",
"inputField": "identify_transfer_agent"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "Yes",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "transfer",
"dataType": "text"
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "identify_composite_agent",
"inputField": "identify_composite_agent"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "Yes",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "composite",
"dataType": "text"
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "identify_composite_agent",
"inputField": "identify_composite_agent"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "No",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "fresh",
"dataType": "text"
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "",
"dataType": "text"
}
}
],
"standardFunction": "IF",
"output": null,
"returnType": "text"
}
}
}
],
"standardFunction": "IF",
"output": null,
"returnType": "text"
}
}
}
],
"standardFunction": "IF",
"output": null,
"returnType": "text"
}
}
}
],
"standardFunction": "IF",
"output": null,
"returnType": "text"
}
}
}
],
"standardFunction": "IS",
"output": null,
"returnType": "text"
},
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "0bkz1cmikm",
"readOnly": false,
"hiddenV2": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": true,
"dataType": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": true,
"dataType": null
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
},
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": true,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 120,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "portal_url",
"inputTypeMapping": {
"code": "portal_url",
"type": "text",
"required": false,
"source": null,
"hint": "Portal URL",
"placeholder": null,
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": null,
"maxChars": null,
"regex": null,
"regexHint": null
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": true,
"dataType": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": true,
"dataType": null
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "[https://abc-staging.lms.getvymo.com/web-platform/branch/abc/onboarding/#/stepper/lob/action/distributor_login_input](https://abc-staging.lms.getvymo.com/web-platform/branch/abc/onboarding/#/stepper/lob/action/distributor_login_input)",
"dataType": "text"
}
}
],
"standardFunction": "IF",
"output": null,
"returnType": "text"
}
}
}
],
"standardFunction": "IS",
"output": null,
"returnType": "text"
},
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "0bkz1cmikm",
"readOnly": false,
"hiddenV2": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": true,
"dataType": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": true,
"dataType": null
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
},
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": true,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 190,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "reason_for_dropping_candidate",
"inputTypeMapping": null,
"sifgMapping": {
"required": false,
"source": null,
"hint": "Reason for Dropping Candidate",
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Not contactable",
"inputFields": []
},
{
"disabled": false,
"order": 10,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Invalid",
"inputFields": []
},
{
"disabled": false,
"order": 20,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Not Interested",
"inputFields": []
},
{
"disabled": false,
"order": 30,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Lack of Relevant Experience",
"inputFields": []
},
{
"disabled": false,
"order": 40,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Insufficient qualifications",
"inputFields": []
},
{
"disabled": false,
"order": 50,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Inconsistencies in the application",
"inputFields": []
},
{
"disabled": false,
"order": 60,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Others",
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "other_candidate_drop_reason",
"inputTypeMapping": {
"code": "other_candidate_drop_reason",
"type": "text",
"required": false,
"source": null,
"hint": "If others, please specify",
"placeholder": null,
"invisible": false,
"oifOptions": null,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": null,
"maxChars": null,
"regex": null,
"regexHint": null
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": null,
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": null,
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false
}
]
},
{
"disabled": false,
"order": 70,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "irdai_check_failed",
"inputFields": []
},
{
"disabled": false,
"order": 80,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "not_interested",
"inputFields": []
},
{
"disabled": false,
"order": 90,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "pan_not_found",
"inputFields": []
},
{
"disabled": false,
"order": 100,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "pan_inactive",
"inputFields": []
},
{
"disabled": false,
"order": 110,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "pan_dedupe_failed",
"inputFields": []
},
{
"disabled": false,
"order": 120,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "idle_application",
"inputFields": []
},
{
"disabled": false,
"order": 130,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "no_arn_registration",
"inputFields": []
},
{
"disabled": false,
"order": 140,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "arn_number_expired",
"inputFields": []
},
{
"disabled": false,
"order": 150,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "arn_mismatch",
"inputFields": []
},
{
"disabled": false,
"order": 160,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "arn_number_cancelled",
"inputFields": []
},
{
"disabled": false,
"order": 170,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "credit_score_check",
"inputFields": []
}
],
"$resourceStrings": null
},
"searchOptions": null,
"required": false,
"hidden": true,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "9d6pthcmzj",
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": true,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 220,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "if_application_number",
"inputTypeMapping": {
"code": "application_number",
"type": "text",
"required": false,
"source": null,
"hint": "Application Number",
"placeholder": null,
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": null,
"maxChars": null,
"regex": null,
"regexHint": null
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "0bkz1cmikm",
"readOnly": false,
"hiddenV2": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.application_number",
"inputField": "inputs_map.application_number",
"voId": null
}
}
],
"standardFunction": "IS_EMPTY",
"output": null,
"returnType": "bool"
}
}
}
],
"standardFunction": "AND",
"output": null,
"returnType": "bool"
},
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": true,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 20,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "remarks_for_dropping_candidate",
"inputTypeMapping": {
"code": "remarks_for_dropping_candidate",
"type": "text",
"required": false,
"source": null,
"hint": "Remarks for Candidate",
"placeholder": null,
"invisible": false,
"oifOptions": null,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": null,
"maxChars": null,
"regex": null,
"regexHint": null
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": true,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "a4atp0p_i",
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": true,
"quickLeadField": false,
"masked": false,
"tooltip": null
}
],
"dppIntegrationEventHandler": "abc-pan-oif-handler",
"async": false,
"numberOfRetries": null,
"retryCtaBlockInterval": null
},
"fetch_kyc_documents": {
"code": "fetch_kyc_documents",
"deleted": true,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"title": "Existing KYC",
"description": null,
"type": "profile_integration",
"enableIf": null,
"applicableIf": {
"stepStatusConditions": null,
"actionStatusConditions": null,
"otherConditions": [
{
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "form",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.etb",
"inputField": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "true",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
]
},
"actionCategory": "PortalProfileIntegrationActionCategory",
"variables": {
"version": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": 1,
"dataType": null
}
},
"carouselEnabled": false,
"ctas": null,
"horizontalActions": null,
"thresholdAge": {
"maxAllowedDelay": 1,
"unit": "DAYS"
},
"inputFieldMappings": [
{
"disabled": false,
"order": 250,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "existing_kyc_address_line_1",
"inputTypeMapping": {
"code": "existing_kyc_address_line_1",
"type": "text",
"required": false,
"source": null,
"hint": "Address Line 1",
"placeholder": null,
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": null,
"maxChars": null,
"regex": "((\\d)|(\\*)|(\\#)|(\\+))?",
"regexHint": "Enter a valid address"
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "yaoqf4cpc",
"readOnly": true,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 260,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "existing_kyc_address_line_2",
"inputTypeMapping": {
"code": "existing_kyc_address_line_2",
"type": "text",
"required": false,
"source": null,
"hint": "Address Line 2",
"placeholder": null,
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": null,
"maxChars": null,
"regex": "((\\d)|(\\*)|(\\#)|(\\+))?",
"regexHint": "Enter a valid address"
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "yaoqf4cpc",
"readOnly": true,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 270,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "existing_kyc_area",
"inputTypeMapping": {
"code": "existing_kyc_area",
"type": "text",
"required": false,
"source": null,
"hint": "Area",
"placeholder": null,
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": null,
"maxChars": null,
"regex": null,
"regexHint": null
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": true,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "yaoqf4cpc",
"readOnly": true,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 280,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "existing_kyc_landmark",
"inputTypeMapping": {
"code": "existing_kyc_landmark",
"type": "text",
"required": false,
"source": null,
"hint": "Landmark",
"placeholder": null,
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": null,
"maxChars": null,
"regex": "^[^\\W\\d_]+(?:\\s[^\\W\\d_]+)*$",
"regexHint": "Please enter a valid landmark"
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "yaoqf4cpc",
"readOnly": true,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 300,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "existing_kyc_city",
"inputTypeMapping": {
"code": "existing_kyc_city",
"type": "text",
"required": false,
"source": null,
"hint": "City",
"placeholder": null,
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": null,
"maxChars": null,
"regex": null,
"regexHint": null
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "yaoqf4cpc",
"readOnly": true,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 310,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "existing_kyc_district",
"inputTypeMapping": {
"code": "existing_kyc_district",
"type": "text",
"required": false,
"source": null,
"hint": "District",
"placeholder": null,
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": null,
"maxChars": null,
"regex": null,
"regexHint": null
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "yaoqf4cpc",
"readOnly": true,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 320,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "existing_kyc_state",
"inputTypeMapping": {
"code": "existing_kyc_state",
"type": "text",
"required": false,
"source": null,
"hint": "State",
"placeholder": null,
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": null,
"maxChars": null,
"regex": null,
"regexHint": null
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "yaoqf4cpc",
"readOnly": true,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 290,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "existing_kyc_pincode",
"inputTypeMapping": {
"code": "existing_kyc_pincode",
"type": "pincode",
"required": false,
"source": null,
"hint": "Pincode",
"placeholder": null,
"invisible": false,
"oifOptions": null,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": null,
"maxChars": null,
"regex": null,
"regexHint": null
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "yaoqf4cpc",
"readOnly": true,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 330,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "existing_kyc_country",
"inputTypeMapping": {
"code": "existing_kyc_country",
"type": "text",
"required": false,
"source": null,
"hint": "Country",
"placeholder": null,
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"minChars": null,
"maxChars": null,
"regex": null,
"regexHint": null
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "yaoqf4cpc",
"readOnly": true,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 1220,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "poi_document_type",
"inputTypeMapping": null,
"sifgMapping": {
"required": true,
"source": null,
"hint": "Document type for Proof Of Identity",
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Aadhar",
"inputFields": []
},
{
"disabled": false,
"order": 10,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Passport",
"inputFields": []
},
{
"disabled": false,
"order": 20,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Voter’s ID",
"inputFields": []
},
{
"disabled": false,
"order": 30,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Driving License",
"inputFields": []
},
{
"disabled": false,
"order": 40,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Job card issued by NREGA",
"inputFields": []
},
{
"disabled": false,
"order": 50,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Letter issued by the National Population Register containing details of name, address",
"inputFields": []
},
{
"disabled": false,
"order": 60,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "PAN",
"inputFields": []
},
{
"disabled": false,
"order": 70,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "03",
"inputFields": []
},
{
"disabled": false,
"order": 80,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "04",
"inputFields": []
},
{
"disabled": false,
"order": 90,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "05",
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "poi_expiration_date",
"inputTypeMapping": {
"code": "poi_expiration_date",
"type": "date",
"required": true,
"source": null,
"hint": "POI Expiration Date",
"placeholder": null,
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"defaultToToday": false,
"showDayMonthYear": null,
"minDate": 15552000000,
"maxDate": 315360000000,
"dateRangeMetaData": null,
"useDateFormat": false
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": null,
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": null,
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false
}
]
},
{
"disabled": false,
"order": 100,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "06",
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "poi_expiration_date",
"inputTypeMapping": {
"code": "poi_expiration_date",
"type": "date",
"required": true,
"source": null,
"hint": "POI Expiration Date",
"placeholder": null,
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"defaultToToday": false,
"showDayMonthYear": null,
"minDate": 15552000000,
"maxDate": 315360000000,
"dateRangeMetaData": null,
"useDateFormat": false
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": null,
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": null,
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false
}
]
},
{
"disabled": false,
"order": 110,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "07",
"inputFields": []
},
{
"disabled": false,
"order": 120,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "08",
"inputFields": []
},
{
"disabled": false,
"order": 130,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "10",
"inputFields": []
},
{
"disabled": false,
"order": 140,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "11",
"inputFields": []
},
{
"disabled": false,
"order": 150,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "35",
"inputFields": []
},
{
"disabled": false,
"order": 160,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "36",
"inputFields": []
},
{
"disabled": false,
"order": 170,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "37",
"inputFields": []
}
],
"$resourceStrings": null
},
"searchOptions": null,
"required": true,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.mark_document_one_as_poi_poa",
"inputField": "null",
"voId": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "POI",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.document_one_type",
"inputField": null,
"voId": null
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.mark_document_two_as_poi_poa",
"inputField": "null",
"voId": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "POI",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.document_two_type",
"inputField": null,
"voId": null
}
}
],
"standardFunction": "IF",
"output": null,
"returnType": "text"
}
}
}
],
"standardFunction": "IF",
"output": null,
"returnType": "text"
}
}
}
],
"standardFunction": "IS",
"output": null,
"returnType": "text"
},
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "xaqnsyucm",
"readOnly": true,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 1230,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "poi_same_as_poa",
"inputTypeMapping": null,
"sifgMapping": {
"required": true,
"source": null,
"hint": "Is your Proof Of Identity same as Proof Of Address?",
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "yes",
"inputFields": []
},
{
"disabled": false,
"order": 10,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "no",
"inputFields": []
}
],
"$resourceStrings": null
},
"searchOptions": null,
"required": true,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "xaqnsyucm",
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 1240,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "poi_upload_front_side",
"inputTypeMapping": {
"code": "poi_upload_front_side",
"type": "multimedia",
"required": true,
"source": null,
"hint": "Proof Of Identity",
"placeholder": null,
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"multiMediaOptions": {
"mediaType": "document",
"mediaTypes": [
"document",
"photo"
],
"minFiles": 1,
"maxFiles": 2,
"maxFileSize": 5120000,
"useInAppViewer": null,
"mimeTypes": [
"PDF",
"PNG",
"JPG",
"JPEG"
],
"access": [
"LOCAL_STORAGE",
"CAMERA",
"GALLERY"
],
"sdkConfig": null
}
},
"sifgMapping": null,
"searchOptions": null,
"required": true,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.mark_document_one_as_poi_poa",
"inputField": "null",
"voId": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "POI",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.document_one_image",
"inputField": null,
"voId": null
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.mark_document_two_as_poi_poa",
"inputField": "null",
"voId": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "POI",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.document_two_image",
"inputField": null,
"voId": null
}
}
],
"standardFunction": "IF",
"output": null,
"returnType": "text"
}
}
}
],
"standardFunction": "IF",
"output": null,
"returnType": "text"
}
}
}
],
"standardFunction": "IS",
"output": null,
"returnType": "text"
},
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "xaqnsyucm",
"readOnly": true,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 1160,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "poa_document_type",
"inputTypeMapping": null,
"sifgMapping": {
"required": true,
"source": null,
"hint": "Document type for Proof Of Address",
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Aadhar",
"inputFields": []
},
{
"disabled": false,
"order": 10,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Passport",
"inputFields": []
},
{
"disabled": false,
"order": 20,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Voter’s ID",
"inputFields": []
},
{
"disabled": false,
"order": 30,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Driving License",
"inputFields": []
},
{
"disabled": false,
"order": 40,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Job card issued by NREGA",
"inputFields": []
},
{
"disabled": false,
"order": 50,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Letter issued by the National Population Register containing details of name, address",
"inputFields": []
},
{
"disabled": false,
"order": 60,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Electricity bill less than two months old",
"inputFields": []
},
{
"disabled": false,
"order": 70,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Telephone bill less than two months old",
"inputFields": []
},
{
"disabled": false,
"order": 80,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Post-paid mobile bill less than two months old",
"inputFields": []
},
{
"disabled": false,
"order": 90,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Phone bill less than two months old",
"inputFields": []
},
{
"disabled": false,
"order": 100,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Piped gas less than two months old",
"inputFields": []
},
{
"disabled": false,
"order": 110,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Water bill less than two months old",
"inputFields": []
},
{
"disabled": false,
"order": 120,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Property or Municipal tax receipt",
"inputFields": []
},
{
"disabled": false,
"order": 130,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Pension or family Pension payment orders (PPOs) if they contain the address",
"inputFields": []
},
{
"disabled": false,
"order": 140,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Letter of allotment of accommodation from employer",
"inputFields": []
},
{
"disabled": false,
"order": 150,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "Any other document as notified by the Central Government",
"inputFields": []
},
{
"disabled": false,
"order": 160,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "04",
"inputFields": []
},
{
"disabled": false,
"order": 170,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "05",
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "poa_expiration_date",
"inputTypeMapping": {
"code": "poa_expiration_date",
"type": "date",
"required": true,
"source": null,
"hint": "POA Expiration Date",
"placeholder": null,
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"defaultToToday": false,
"showDayMonthYear": "DMY",
"minDate": 15552000000,
"maxDate": 315360000000,
"dateRangeMetaData": null,
"useDateFormat": false
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": null,
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": null,
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false
}
]
},
{
"disabled": false,
"order": 180,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "06",
"inputFields": [
{
"disabled": false,
"order": 0,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "poa_expiration_date",
"inputTypeMapping": {
"code": "poa_expiration_date",
"type": "date",
"required": true,
"source": null,
"hint": "POA Expiration Date",
"placeholder": null,
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"defaultToToday": false,
"showDayMonthYear": "DMY",
"minDate": 15552000000,
"maxDate": 315360000000,
"dateRangeMetaData": null,
"useDateFormat": false
},
"sifgMapping": null,
"searchOptions": null,
"required": false,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": null,
"defaultValue": null,
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": null,
"readOnly": false,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false
}
]
},
{
"disabled": false,
"order": 190,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "07",
"inputFields": []
},
{
"disabled": false,
"order": 200,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "08",
"inputFields": []
},
{
"disabled": false,
"order": 210,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "12",
"inputFields": []
},
{
"disabled": false,
"order": 220,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "13",
"inputFields": []
},
{
"disabled": false,
"order": 230,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "14",
"inputFields": []
},
{
"disabled": false,
"order": 240,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "15",
"inputFields": []
},
{
"disabled": false,
"order": 250,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "16",
"inputFields": []
},
{
"disabled": false,
"order": 260,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "17",
"inputFields": []
},
{
"disabled": false,
"order": 270,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "35",
"inputFields": []
},
{
"disabled": false,
"order": 280,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "03",
"inputFields": []
},
{
"disabled": false,
"order": 290,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "36",
"inputFields": []
},
{
"disabled": false,
"order": 300,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"selectionOption": "37",
"inputFields": []
}
],
"$resourceStrings": null
},
"searchOptions": null,
"required": true,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.mark_document_one_as_poi_poa",
"inputField": "null",
"voId": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "POA",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.document_one_type",
"inputField": null,
"voId": null
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.mark_document_two_as_poi_poa",
"inputField": "null",
"voId": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "POA",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.document_two_type",
"inputField": null,
"voId": null
}
}
],
"standardFunction": "IF",
"output": null,
"returnType": "text"
}
}
}
],
"standardFunction": "IF",
"output": null,
"returnType": "text"
}
}
}
],
"standardFunction": "IS",
"output": null,
"returnType": "text"
},
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "damwr3vhd",
"readOnly": true,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 1170,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "upload_poa_front_side",
"inputTypeMapping": {
"code": "upload_poa_front_side",
"type": "multimedia",
"required": false,
"source": null,
"hint": "Proof Of Address",
"placeholder": null,
"invisible": false,
"oifOptions": {
"type": "default",
"minChars": 0,
"debounceMS": 0,
"dynamicOif": false
},
"$resourceStrings": null,
"$editablePropertiesBy": null,
"multiMediaOptions": {
"mediaType": "document",
"mediaTypes": [
"document",
"photo"
],
"minFiles": 1,
"maxFiles": 2,
"maxFileSize": 5120000,
"useInAppViewer": null,
"mimeTypes": [
"PDF",
"PNG",
"JPG",
"JPEG"
],
"access": [
"LOCAL_STORAGE",
"CAMERA",
"GALLERY"
],
"sdkConfig": null
}
},
"sifgMapping": null,
"searchOptions": null,
"required": true,
"hidden": false,
"displayInFormType": null,
"explicitScopes": false,
"scopeMappings": [],
"defaultValue": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.mark_document_one_as_poi_poa",
"inputField": "null",
"voId": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "POA",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.document_one_image",
"inputField": null,
"voId": null
}
},
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "function",
"operator": null,
"operatorRequired": false,
"function": {
"type": "standard",
"inputs": [
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.mark_document_two_as_poi_poa",
"inputField": "null",
"voId": null
}
},
{
"type": "value",
"value": {
"valType": "static",
"operator": null,
"operatorRequired": false,
"value": "POA",
"dataType": "text"
}
}
],
"standardFunction": "EQUALS_IGNORE_CASE",
"output": null,
"returnType": "bool"
}
}
},
{
"type": "value",
"value": {
"valType": "vo",
"operator": null,
"operatorRequired": false,
"attribute": "inputs_map.document_two_image",
"inputField": null,
"voId": null
}
}
],
"standardFunction": "IF",
"output": null,
"returnType": "text"
}
}
}
],
"standardFunction": "IF",
"output": null,
"returnType": "text"
}
}
}
],
"standardFunction": "IS",
"output": null,
"returnType": "text"
},
"placeholderValue": null,
"generatedOptions": null,
"validations": null,
"fieldGroup": "damwr3vhd",
"readOnly": true,
"hiddenV2": null,
"hideInView": null,
"readOnlyV2": null,
"requiredV2": null,
"retainFormContext": false,
"quickLeadField": false,
"masked": false,
"tooltip": null
},
{
"disabled": false,
"order": 1330,
"$resourceStrings": null,
"$editablePropertiesBy": null,
"flowVersion": null,
"productConfig": false,
"journeyIds": null,
"inputField": "change_fetched_documents",
"inputTypeMapping": null,
"sifgMapping": {
"required": false,
"source": null,
"hint": "Do y