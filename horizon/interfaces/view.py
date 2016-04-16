import abc


class IView(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def position(self):
        """
        """
