thonclass InstagramParser:
    def __init__(self, posts_data):
        self.posts_data = posts_data

    def parse_posts(self):
        parsed_posts = []
        for post in self.posts_data:
            parsed_posts.append({
                'username': post.get('username'),
                'id': post.get('id'),
                'shortcode': post.get('shortcode'),
                'dimensions': post.get('dimensions'),
                'displayUrl': post.get('displayUrl'),
                'caption': post.get('caption'),
                'commentsCount': post.get('commentsCount'),
                'likeCount': post.get('likeCount'),
                'owner': post.get('owner'),
                'timestamp': post.get('timestamp'),
                'hashtags': post.get('hashtags'),
                'mentions': post.get('mentions'),
                'isSponsored': post.get('isSponsored'),
                'videoUrl': post.get('videoUrl', None),
                'videoViewCount': post.get('videoViewCount', None),
            })
        return parsed_posts