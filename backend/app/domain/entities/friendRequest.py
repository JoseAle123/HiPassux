from app.extensions import db
import enum
from datetime import datetime

class RequestStatus(enum.Enum):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'

class FriendRequest(db.Model):
    __tablename__ = 'FRIENDREQUEST'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('USERS.user_id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('USERS.user_id'), nullable=False)
    status = db.Column(db.Enum(RequestStatus), default=RequestStatus.PENDING, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    sender = db.relationship('User', foreign_keys=[sender_id], backref='sent_requests')
    receiver = db.relationship('User', foreign_keys=[receiver_id], backref='received_requests')

    def __repr__(self):
        return f'<FriendRequest {self.sender_id} -> {self.receiver_id} ({self.status})>'

    def to_dict(self):
        return {
            'id': self.id,
            'sender_id': self.sender_id,
            'receiver_id': self.receiver_id,
            'status': self.status.value,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }