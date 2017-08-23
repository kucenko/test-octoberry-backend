from .ping_view import ping_get_view
from .user_view import user_add_view, user_edit_view, user_get_list_view
from .article_view import article_add_view, article_get_list_view, article_get_view
from .comment_view import comment_add_view, comment_get_list_view, comment_edit_view


__all__ = [
    'route_views'
]

route_views = [
    ping_get_view,
    user_add_view, user_edit_view, user_get_list_view,
    article_add_view, article_get_list_view, article_get_view,
    comment_add_view, comment_get_list_view, comment_edit_view,
]
