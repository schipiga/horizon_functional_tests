import abc


class IPage(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def app(self):
        """
        """
