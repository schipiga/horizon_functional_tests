import abc


class IWebdriverable(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def webdriver(self):
        """
        """
