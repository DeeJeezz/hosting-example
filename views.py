from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from builder import query_builder
from models import BatchRequestParams

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    try:
        # TODO: Проверить на ошибки.
        params = BatchRequestParams().load(data=request.json)
    except ValidationError as error:
        return jsonify(error.messages), 400

    # TODO: Вернуть данные по запросу.
    result = None
    for query in params['queries']:
        result = query_builder(
            cmd=query['cmd'],
            value=query['value'],
            data=result,
        )

    return jsonify(result)
