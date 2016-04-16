import abc


class IElement(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def parent(self):
        """
        """

    @abc.abstractmethod
    def set_text(self, text):
        """
        """

    @abc.abstractproperty
    def text(self):
        """
        """

    @abc.abstractmethod
    def click(self):
        """
        """

    @abc.abstractmethod
    def right_click(self):
        """
        """

    @abc.abstractmethod
    def double_click(self):
        """
        """

    @abc.abstractproperty
    def is_present(self):
        """
        """

    @abc.abstractproperty
    def is_checked(self):
        """
        """

    @abc.abstractproperty
    def is_enabled(self):
        """
        """

    @abc.abstractproperty
    def is_visible(self):
        """
        """
