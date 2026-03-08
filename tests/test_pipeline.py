from app.validation import validate_post

def test_valid_post():

    post = {
        "id": 1,
        "title": "example",
        "body": "content"
    }

    assert validate_post(post) == True
