from flask import Blueprint
from flask import current_app
from flask import json
from flask import request, jsonify

from app.errors import InvalidRequest, register_errors
from app.notifications.process_client_response import validate_callback_data, process_sms_client_response

sms_callback_blueprint = Blueprint("sms_callback", __name__, url_prefix="/notifications/sms")
register_errors(sms_callback_blueprint)


@sms_callback_blueprint.route('/telstra/<notification_id>', methods=['POST'])
def process_telstra_response(notification_id):
    client_name = 'Telstra'
    data = json.loads(request.data)
    errors = validate_callback_data(data=data,
                                    fields=['messageId', 'deliveryStatus'],
                                    client_name=client_name)
    if errors:
        raise InvalidRequest(errors, status_code=400)

    success, errors = process_sms_client_response(status=str(data.get('deliveryStatus')),
                                                  provider_reference=notification_id,
                                                  client_name=client_name)

    redacted_data = data.copy()
    redacted_data.pop("to")
    current_app.logger.debug(
        "Full delivery response from {} for notification: {}\n{}".format(client_name, notification_id, redacted_data))
    if errors:
        raise InvalidRequest(errors, status_code=400)
    else:
        return jsonify(result='success', message=success), 200


@sms_callback_blueprint.route('/twilio/<notification_id>', methods=['POST'])
def process_twilio_response(notification_id):
    client_name = 'Twilio'

    data = request.values
    errors = validate_callback_data(
        data=data,
        fields=['MessageStatus', 'MessageSid'],
        client_name=client_name
    )

    if errors:
        raise InvalidRequest(errors, status_code=400)

    success, errors = process_sms_client_response(
        status=data.get('MessageStatus'),
        provider_reference=notification_id,
        client_name=client_name
    )

    redacted_data = dict(data.items())
    redacted_data.pop('To', None)
    current_app.logger.debug(
        "Full delivery response from {} for notification: {}\n{}".format(client_name, notification_id, redacted_data))
    if errors:
        raise InvalidRequest(errors, status_code=400)
    else:
        return jsonify(result='success', message=success), 200


@sms_callback_blueprint.route('/mmg', methods=['POST'])
def process_mmg_response():
    client_name = 'MMG'
    data = json.loads(request.data)
    errors = validate_callback_data(data=data,
                                    fields=['status', 'CID'],
                                    client_name=client_name)
    if errors:
        raise InvalidRequest(errors, status_code=400)

    success, errors = process_sms_client_response(status=str(data.get('status')),
                                                  provider_reference=data.get('CID'),
                                                  client_name=client_name)

    redacted_data = data.copy()
    redacted_data.pop("MSISDN")
    current_app.logger.debug(
        "Full delivery response from {} for notification: {}\n{}".format(client_name, request.form.get('CID'),
                                                                         redacted_data))
    if errors:
        raise InvalidRequest(errors, status_code=400)
    else:
        return jsonify(result='success', message=success), 200


@sms_callback_blueprint.route('/firetext', methods=['POST'])
def process_firetext_response():
    client_name = 'Firetext'
    errors = validate_callback_data(data=request.form,
                                    fields=['status', 'reference'],
                                    client_name=client_name)
    if errors:
        raise InvalidRequest(errors, status_code=400)
    redacted_data = dict(request.form).copy()
    redacted_data.pop('mobile')
    current_app.logger.debug(
        "Full delivery response from {} for notification: {}\n{}".format(client_name, request.form.get('reference'),
                                                                         redacted_data))
    success, errors = process_sms_client_response(status=request.form.get('status'),
                                                  provider_reference=request.form.get('reference'),
                                                  client_name=client_name)
    if errors:
        raise InvalidRequest(errors, status_code=400)
    else:
        return jsonify(result='success', message=success), 200
