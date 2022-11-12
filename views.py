from typing import Dict, Iterable, List, Optional

from flask import Blueprint, Response, jsonify, request
from marshmallow import ValidationError

from builder import query_builder
from models import BatchRequestParams

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Response:
    try:
        # TODO: Проверить на ошибки.
        params: Dict[str, List[Dict[str, str]]] = BatchRequestParams().load(data=request.json)
    except ValidationError as error:
        return Response(response=error.messages, status=400)

    # TODO: Вернуть данные по запросу.
    result: Optional[Iterable[str]] = None
    for query in params['queries']:
        result = query_builder(
            cmd=query['cmd'],
            value=query['value'],
            data=result,
        )

    return jsonify(result)
