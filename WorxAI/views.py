import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# DataBase Actions
from WorxAI.db.actions.create_workflow import create_workflow
from WorxAI.db.actions.user_signup import create_or_update_user
from WorxAI.db.actions.get_workflows import get_workflows
from WorxAI.db.actions.get_workflow import get_workflow

# Utilies
from WorxAI.utils.create_node_flow import node_flow_in_order
from WorxAI.utils.flow_execution import flow_execution


@csrf_exempt
def workflow_creation(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        user = data.get("username")
        schema = data.get("schema")

        res = create_workflow(user, schema)

    return JsonResponse({"schema": res})


@csrf_exempt
def workflow_execution(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        api_key = data.get("api_key")
        workflow_id = data.get("workflow_id")
        input = data.get("input")

        response = get_workflow(api_key, workflow_id)
        workflow = response["workflow"]

        if workflow:
            nodes = json.loads(workflow["workflow_schema"]).get("nodes")
            if nodes:
                flow = node_flow_in_order(nodes)
                response = flow_execution(nodes, input)
                return JsonResponse({"response": response})

        else:
            return JsonResponse(response)


@csrf_exempt
def signup(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        email = data.get("email")

        res = create_or_update_user(email)

        return JsonResponse({"user_details": res})


def get_workflows(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        email = data.get("email")

        workflows = get_workflows()

        return JsonResponse(workflows)
