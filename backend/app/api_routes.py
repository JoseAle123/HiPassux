from app.api.user_api import user_api
from app.api.post_api import post_api
from app.api.message_api import message_api
from app.api.reaction_api import reaction_api
from app.api.comment_api import comment_api
from app.api.friendRequest_api import friend_request_api

def init_api_routes(app):
    app.register_blueprint(user_api)
    app.register_blueprint(post_api)
    app.register_blueprint(message_api)
    app.register_blueprint(reaction_api)
    app.register_blueprint(comment_api)
    app.register_blueprint(friend_request_api)