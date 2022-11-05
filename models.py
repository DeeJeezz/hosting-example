from marshmallow import Schema, ValidationError, fields, validates_schema


VALID_CMD = ('filter', 'map', 'unique', 'sort', 'limit')


class RequestParams(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values, *args, **kwargs):
        if values['cmd'] not in VALID_CMD:
            raise ValidationError('"cmd" contains invalid value')


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)
