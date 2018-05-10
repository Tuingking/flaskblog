from flaskblog.models import Post

posts = Post.query.paginate(page=1, per_page=10, error_out=False)

# DEMO
posts.total                                     # int, total items
posts.pages                                     # int, total pages
posts.page                                      # int, default=1
posts.per_page                                  # int, default=20
posts.iter_pages(left_edge=1, right_edge=1)     # generator

posts.has_next                                  # Bool, True|False
posts.has_prev                                  # Bool, True|False
posts.prev_num                                  # int, None if no prev page
posts.next_num                                  # int, None if no next page

posts.items                                     # List all items
