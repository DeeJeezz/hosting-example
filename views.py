from flask import Blueprint, Response, jsonify, request
from marshmallow import ValidationError

from builder import build_query
from db import db
from models import BatchRequestParams

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Response:
    try:
        params = BatchRequestParams().load(request.json)
    except ValidationError as error:
        return Response(response=error.messages, status=400)

    result = None
    for query in params['queries']:
        result = build_query(
            cmd=query['cmd'],
            param=query['value'],
            data=result,
        )

    return jsonify(result)


@main_bp.route('/test_db')
def test_db():
    result = db.session.execute(
        'SELECT 34543575675678'
    ).scalar()

    return jsonify(
        {
            'result': result,
        }
    )
