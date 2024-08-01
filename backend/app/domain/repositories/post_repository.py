from app.domain.entities.post import db, Post

class PostRepository:

    @staticmethod
    def get_all_posts():
        return Post.query.all()
    
    @staticmethod
    def get_posts_by_user(user_id):
        """Retrieve all posts for a specific user."""
        return Post.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def get_post_by_id(post_id):
        """Retrieve a single post by its ID."""
        return Post.query.get(post_id)
    
    @staticmethod
    def add(post):
        db.session.add(post)
        db.session.commit()
        # Añade un usuario a la base de datos y confirma la transacción.

    @staticmethod
    def update_post(post_id, updated_data):
        """
        Update an existing post with new data.
        
        Args:
            post_id: The ID of the post to be updated.
            updated_data: A dictionary with the updated fields.
        """
        post = Post.query.get(post_id)
        if post:
            for key, value in updated_data.items():
                setattr(post, key, value)
            db.session.commit()
        return post

    @staticmethod
    def delete_post(post_id):
        """Delete a post from the database."""
        post = Post.query.get(post_id)
        if post:
            db.session.delete(post)
            db.session.commit()
        return post
