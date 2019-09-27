import requests

# Creating the url
url = "https://api.github.com"


def hudl_get_response():
    res_get = requests.get(url).status_code
    print(res_get)


# hudl_get_response()


def hudl_put_response():
    res_put = requests.put(url).status_code
    print(res_put)


# hudl_put_response()


def hudl_post_response():
    res_post = requests.post(url).status_code
    print(res_post)


# hudl_post_response()

def hudl_delete_response():
    res_delete = requests.delete(url).status_code
    print(res_delete)

# hudl_delete_response()
