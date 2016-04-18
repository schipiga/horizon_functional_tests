import abc


class IPage(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def app(self):
        """
        """

    @abc.abstractproperty
    def url(self):
        """
        """
