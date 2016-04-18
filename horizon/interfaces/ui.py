import abc


class IUi(object):

    __metaclass__ = abc.ABCMeta

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
    def is_enabled(self):
        """
        """

    @abc.abstractproperty
    def is_visible(self):
        """
        """
