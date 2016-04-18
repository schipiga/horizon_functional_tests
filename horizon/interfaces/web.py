import abc


class IWeb(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def locator(self):
        """
        """

    @abc.abstractproperty
    def web_driver(self):
        """
        """

    @abc.abstractproperty
    def web_element(self):
        """
        """
