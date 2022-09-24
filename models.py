from typing import Any, Dict, Iterable

from marshmallow import Schema, ValidationError, fields, validates_schema

VALID_CMD_PARAMS: Iterable[str] = (
    'filter',
    'sort',
    'map',
    'unique',
    'limit',
    'regex',
)


class RequestParams(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values: Dict[str, str], *args: Any, **kwargs: Any) -> Dict[str, str]:
        if values['cmd'] not in VALID_CMD_PARAMS:
            raise ValidationError('"cmd" contains invalid value')

        return values


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)
