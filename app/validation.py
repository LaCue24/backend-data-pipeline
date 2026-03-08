def validate_post(post):

    if "id" not in post:
        raise ValueError("Missing id")

    if "title" not in post:
        raise ValueError("Missing title")

    if len(post["title"]) == 0:
        raise ValueError("Title cannot be empty")

    return True
