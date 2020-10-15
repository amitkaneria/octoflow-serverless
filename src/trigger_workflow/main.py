import json
import os
from typing import Tuple, Union, Any

import boto3

from utils import Response


# Create an SNS client
sns = boto3.client("sns")


def send_to_events_queue(instance_id: str) -> Any:
    """
    Send message to events topic, which passes message to EventsQueue eventually
    :param message:
    :return:
    """
    EVENTS_TOPIC_ARN = os.environ.get("EVENTS_TOPIC_ARN")
    response = sns.publish(TopicArn=EVENTS_TOPIC_ARN, Message=instance_id)
    return response


def lambda_handler(event, context):
    """

    :param event:
    :param context:
    :return:
    """
    print(event)

    # TODO: Update this stub and add Steps to execute user's input

    # Step 1: Parse JSON data into dict
    data = None
    try:
        data = json.loads(event.get("body"))
    except Exception as exc:
        print(f"Exception caught! :{exc}")
        return Response(
            {"message": "Failed to parse Json data", "reason": f"{exc}"}, 400
        )

    # Step 2: Validate Json

    # Step 3: Persist data!

    # Step 4: Send to SNS Topic for further processing
    response = send_to_events_queue("pass_some_instance_id")
    print(response)
    return Response({"message": "I've got your back!", "input_data": data})
