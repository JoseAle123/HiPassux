from flask import Blueprint, jsonify, request
from app.domain.services.post_service import PostService

post_api = Blueprint('post_api', 'post_api', url_prefix='/api/posts')

error_post = 'Post not found'

@post_api.route('/', methods=['GET'])
def get_posts():
    posts = PostService.get_all_posts()
    return jsonify([post.to_dict() for post in posts])

@post_api.route('/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = PostService.get_post_by_id(post_id)
    if post:
        return jsonify(post.to_dict())
    return jsonify({'error': error_post}), 404

@post_api.route('/user/<int:user_id>', methods=['GET'])
def get_post_by_user(user_id):
    posts = PostService.get_posts_by_user(user_id)
    return jsonify([post.to_dict() for post in posts])

@post_api.route('/', methods=['POST'])
def create_post():
    data = request.json
    new_post = PostService.create_post(
        data.get('content'),
        data.get('user_id')
    )
    return jsonify(new_post.to_dict()), 201

@post_api.route('/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.json
    updated_post = PostService.update_post(post_id, data)
    if updated_post:
        return jsonify(updated_post.to_dict())
    return jsonify({'error': error_post}), 404

@post_api.route('/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    success = PostService.delete_post(post_id)
    if success:
        return jsonify({'message': 'Post deleted successfully'})
    return jsonify({'error': error_post}), 404