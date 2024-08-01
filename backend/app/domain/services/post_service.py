from app.domain.repositories.post_repository import Post,PostRepository

class PostService:

    @staticmethod
    def get_all_posts():
        return PostRepository.get_all_posts()

    @staticmethod
    def get_post_by_id(post_id):
        return PostRepository.get_post_by_id(post_id)

    @staticmethod
    def create_post(content, user_id):
        new_post = Post(
            content = content,
            user_id = user_id
        )
        PostRepository.add(new_post)
        return new_post
    
    @staticmethod
    def update_post(post_id, updated_data):
        if not post_id or not isinstance(post_id, int):
            raise ValueError("Invalid post_id")
        
        if not updated_data or not isinstance(updated_data, dict):
            raise ValueError("Updated data must be a dictionary")

        post = PostRepository.update_post(post_id, updated_data)
        if post is None:
            raise ValueError("Post not found")
        return post

    @staticmethod
    def delete_post(post_id):
        if not post_id or not isinstance(post_id, int):
            raise ValueError("Invalid post_id")
        
        post = PostRepository.delete_post(post_id)
        if post is None:
            raise ValueError("Post not found")
        return post

    @staticmethod
    def get_posts_by_user(user_id):
        if not user_id or not isinstance(user_id, int):
            raise ValueError("Invalid user_id")
        
        return PostRepository.get_posts_by_user(user_id)
    
