from flask import Blueprint, jsonify, request
from app.domain.services.friendRequest_service import FriendRequestService

friend_request_api = Blueprint('friend_request_api', __name__, url_prefix='/api/friend_requests')

@friend_request_api.route('/', methods=['POST'])
def send_friend_request():
    data = request.json
    sender_id = data.get('sender_id')
    receiver_id = data.get('receiver_id')

    result = FriendRequestService.send_friend_request(sender_id, receiver_id)
    if isinstance(result, str):  # Error message
        return jsonify({'error': result}), 400
    return jsonify(result.to_dict()), 201

@friend_request_api.route('/<int:request_id>', methods=['PUT'])
def respond_to_friend_request(request_id):
    data = request.json
    action = data.get('action')

    result = FriendRequestService.respond_to_friend_request(request_id, action)
    if isinstance(result, str):  # Error message
        return jsonify({'error': result}), 400
    return jsonify(result.to_dict()), 200

@friend_request_api.route('/<int:request_id>', methods=['GET'])
def get_friend_request(request_id):
    request_obj = FriendRequestService.get_all_friend_requests().query.get(request_id)
    if request_obj:
        return jsonify(request_obj.to_dict())
    return jsonify({'error': 'Friend request not found.'}), 404

@friend_request_api.route('/', methods=['GET'])
def list_friend_requests():
    requests = FriendRequestService.get_all_friend_requests()
    return jsonify([request.to_dict() for request in requests])