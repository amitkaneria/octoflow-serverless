import json
from typing import Union, Dict

from .helpers import Encoder


def Response(
        data: Union[dict, str, list],
        status_code: int = 200,
        allow_origin: str = "*",
        allow_headers: str = "Content-Type,X-Amz-Date,Authorization,X-Api-Key,x-requested-with",
        allow_methods: str = "GET,POST,PUT,DELETE,OPTIONS"
    ) -> Dict[str, Union[int, str]]:
    """
    Returns a response for API Gateway
    """

    if isinstance(data, str):
        data = {"message": data}

    return {
        "statusCode": status_code,
        "headers": {
            "Access-Control-Allow-Headers": allow_headers,
            "Access-Control-Allow-Origin": allow_origin,
            "Access-Control-Allow-Methods": allow_methods
        },
        "body": json.dumps(data, cls=Encoder)
    }