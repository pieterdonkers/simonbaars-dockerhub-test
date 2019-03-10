import connexion
import six

from swagger_server.models.errorunknown import ERRORUNKNOWN  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.person import Person  # noqa: E501
from swagger_server.models.persons import Persons  # noqa: E501
from swagger_server import util


def images_image_id_get(User_Agent, imageId):  # noqa: E501
    """Gets an image

     # noqa: E501

    :param User_Agent: 
    :type User_Agent: str
    :param imageId: 
    :type imageId: str

    :rtype: None
    """
    return 'do some magic!'


def images_post(User_Agent, image=None):  # noqa: E501
    """Uploads an image

     # noqa: E501

    :param User_Agent: 
    :type User_Agent: str
    :param image: 
    :type image: werkzeug.datastructures.FileStorage

    :rtype: ERRORUNKNOWN
    """
    return 'do some magic!'


def persons_get(User_Agent, pageSize=None, PageNumber=None):  # noqa: E501
    """Gets some persons

    Returns a list containing all persons. # noqa: E501

    :param User_Agent: 
    :type User_Agent: str
    :param pageSize: Number of persons returned
    :type pageSize: int
    :param PageNumber: Page number
    :type PageNumber: int

    :rtype: Persons
    """
    return 'do some magic!'


def persons_post(User_Agent, person=None):  # noqa: E501
    """Creates a person

    Adds a new person to the persons list. # noqa: E501

    :param User_Agent: 
    :type User_Agent: str
    :param person: The person to create.
    :type person: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        person = Person.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def persons_username_delete(username):  # noqa: E501
    """Deletes a person

    Delete a single person indentified via its username # noqa: E501

    :param username: The persons&#39;s username
    :type username: str

    :rtype: None
    """
    return 'do some magic!'


def persons_username_friends_get(username, pageSize=None, PageNumber=None):  # noqa: E501
    """Gets a person&#39;s friends

    Returns a list containing all persons. The list supports paging. # noqa: E501

    :param username: The persons&#39;s username
    :type username: str
    :param pageSize: Number of persons returned
    :type pageSize: int
    :param PageNumber: Page number
    :type PageNumber: int

    :rtype: Persons
    """
    return 'do some magic!'


def persons_username_get(username):  # noqa: E501
    """Gets a person

    Returns a single person for its username. # noqa: E501

    :param username: The persons&#39;s username
    :type username: str

    :rtype: Person
    """
    return 'do some magic!'
