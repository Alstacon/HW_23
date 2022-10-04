from marshmallow import Schema, fields, validates_schema, ValidationError

VALID_CMD = (
    'filter',
    'sort',
    'map',
    'limit',
    'unique'
)


class RequestParams(Schema):
    """ class for validation income cmds, values"""
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values, *args, **kwargs):
        if values['cmd'] not in VALID_CMD:
            raise ValidationError('cmd contains invalid value')
        return values


class ManyRequestsParams(Schema):
    queries = fields.Nested(RequestParams, many=True)
