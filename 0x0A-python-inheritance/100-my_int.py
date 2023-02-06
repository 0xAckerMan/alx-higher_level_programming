#!/usr/bin/python3
"""
Contains subclass of class int
"""


class MyInt(int):
    """
    class MyInt inherits class int
    """
    def __eq__(self, value):
        """
        Works inversly to that of class int
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """
        Works inversly to that of class int
        """
        return super().__eq__(value)
