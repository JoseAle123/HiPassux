from app.domain.repositories.friendRequest_repository import FriendRequestRepository, RequestStatus

class FriendRequestService:

    @staticmethod
    def get_all_friend_requests():
        return FriendRequestRepository.get_all_friend_requests()

    @staticmethod
    def send_friend_request(sender_id, receiver_id):
        if sender_id == receiver_id:
            return "No puedes enviarte una solicitud a ti mismo."

        existing_request = FriendRequestRepository.get_requests_by_sender(sender_id)
        if any(request.receiver_id == receiver_id for request in existing_request):
            return "Ya has enviado una solicitud a este usuario."

        new_request = FriendRequestRepository.create_friend_request(sender_id, receiver_id)
        return new_request

    @staticmethod
    def respond_to_friend_request(request_id, action):
        request_obj = FriendRequestRepository.get_friend_request_by_id(request_id)
        if not request_obj:
            return "Solicitud no encontrada."

        if action == 'accept':
            request_obj = FriendRequestRepository.update_friend_request(request_id, RequestStatus.ACCEPTED)
        elif action == 'reject':
            request_obj = FriendRequestRepository.update_friend_request(request_id, RequestStatus.REJECTED)
        else:
            return "Acción inválida."

        return request_obj