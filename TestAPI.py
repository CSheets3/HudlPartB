import unittest
import main


# You could also import Json for this project and sift through the information that way
# On success all cases would throw a 200 code
class APITest(unittest.TestCase):
    def test_get_request(self):
        # If this test succeeds then the user would be able to look at the team information in the object
        # If this test does NOT succeed then the user wouldn't be able to see anything and an error would pop up
        if main.hudl_get_response() == 200:
            print('Code 200 -  Test Success')

    def test_put_request(self):
        # If this test succeeds then the user would be able to create / update the object
        # If this test throw a 404 error then the object won't be updated.
        # You can call the same Put requests multiple times and get the SAME result
        if main.hudl_put_response() == 404:
            print('Code 404 - Not Found')

    def test_post_request(self):
        # If this test succeeds then the user would also be able to create / update the object
        # If this tests throws a 404 error then the object won't be updated
        # The data sent to the server with Post is stored within the request body of the http request
        # You can call the same Post request multiple times but will NOT get the same result
        if main.hudl_put_response() == 404:
            print ('Code 404 -  Not Found')

    def test_delete_request(self):
        # If this tests succeeds then the user could delete the specified object
        # If this test doesn't succeed then the user would not be able to delete anything
        # This might throw up a 401 error as the user wouldn't be authorized to delete anything, only change it.
        # It may also throw up a 403 error as it's forbidden to delete the object.
        if main.hudl_delete_response() == 404:
            print('Code 404 - Not Found')

# I know how API's work, but I wasn't exactly sure what Part B was asking for so I made this program in hope that
# it's close
