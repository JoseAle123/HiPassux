from app.domain.entities.friendRequest import FriendRequest, RequestStatus ,db

class FriendRequestRepository:

    @staticmethod
    def get_all_friend_requests():
        return FriendRequest.query.all()

    @staticmethod
    def get_friend_request_by_id(request_id):
        return FriendRequest.query.get(request_id)

    @staticmethod
    def get_requests_by_sender(sender_id):
        return FriendRequest.query.filter_by(sender_id=sender_id).all()

    @staticmethod
    def get_requests_by_receiver(receiver_id):
        return FriendRequest.query.filter_by(receiver_id=receiver_id).all()

    @staticmethod
    def create_friend_request(sender_id, receiver_id):
        new_request = FriendRequest(sender_id=sender_id, receiver_id=receiver_id)
        db.session.add(new_request)
        db.session.commit()
        return new_request

    @staticmethod
    def update_friend_request(request_id, status):
        request_obj = FriendRequest.query.get(request_id)
        if request_obj:
            request_obj.status = status
            db.session.commit()
        return request_obj

    @staticmethod
    def delete_friend_request(request_id):
        request_obj = FriendRequest.query.get(request_id)
        if request_obj:
            db.session.delete(request_obj)
            db.session.commit()
        return request_obj