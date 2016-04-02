from functools import wraps

from hamcrest import assert_that

from horizon.config import Config


def kwgs_only(*keys):

    @wraps(func)
    def decorator(func):

        def wrapper(*args, **kwgs):
            if set(kwgs.keys()) - set(keys):
                raise KeyError("Keys {!r} are available only".format(keys))

            return func(*args, **kwgs)

        return wrapper

    return decorator


@kwgs_only('screencapture')
def check_that(message, *args, **kwgs):
    args = list(args)
    args.append("Expected that {}, but it wasn't.".format(message))

    screencapture = Config.screencapture and kwgs.pop('screencapture', False)

    with step("Check that {}.".format(message)):
        if screencapture:
            Config.make_screenshot(Config.screenshot_path)
        assert_that(*args)
