class Storage:
    """Storage class provides the API to the storage."""

    def __init__(self, session) -> None:
        """Constructor method

        :param session: SQLAlchemy session
        """
        self._session = session

    def auth_user(self, user, password):
        """
        Authenticate user.

        :param user: user name
        :param password: user password
        """
        pass
