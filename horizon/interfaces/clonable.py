import abc


class IClonable(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def clone(self, *args, **kwgs):
        """Clone object.
        """
