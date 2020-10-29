"""
Module to test trigger_workflow service
"""
import json
import os

import boto3
import pytest
from botocore.stub import Stubber

from src.trigger_workflow.main import send_to_events_queue, sns, lambda_handler
import os


@pytest.fixture(scope="function")
def instance_id():
    return "urn:takorun:1:instance:12345678910"


@pytest.fixture(scope="function")
def event_without_body():
    return {
        "body": None,
        "resource": "/{proxy+}",
        "path": "/path/to/resource",
        "httpMethod": "POST",
        "queryStringParameters": {"foo": "bar"},
    }


def test_send_sns_topic(instance_id):
    """
    Mock test to send instance id to events-sns-topic
    :param instance_id:
    :return:
    """
    response = {"MessageId": instance_id}
    EVENTS_TOPIC_ARN = "arn_will_go_here"
    os.environ["EVENTS_TOPIC_ARN"] = EVENTS_TOPIC_ARN
    expected_params = {"TopicArn": EVENTS_TOPIC_ARN, "Message": instance_id}
    events_sns = Stubber(sns)
    events_sns.add_response("publish", response, expected_params)
    events_sns.activate()

    response = send_to_events_queue(instance_id)
    assert response.get("MessageId"), "Response should contain message id"


def test_without_body_in_json_event(event_without_body):
    """
    Test event without any body specified

    :param event_without_body:
    :return:
    """
    response = lambda_handler(event_without_body, {})
    assert response.get("statusCode") == 400, "Status code should be 400"

    response_body = response.get("body")
    assert response_body, "Response body should not be empty"
    error_message = json.loads(response_body)

    assert (
        error_message.get("message") == "Failed to parse Json data"
    ), "Response message should be there"
