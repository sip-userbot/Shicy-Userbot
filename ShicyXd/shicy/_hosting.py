import os


def where_hosted():
    if os.getenv("DYNO"):
        return "heroku"
    if os.getenv("RAILWAY_STATIC_URL"):
        return "railway"
    if os.getenv("KUBERNETES_PORT"):
        return "qovery"
    if os.getenv("WINDOW") and os.getenv("WINDOW") != "0":
        return "windows"
    if os.getenv("RUNNER_USER") or os.getenv("HOSTNAME"):
        return "github actions"
    if os.getenv("ANDROID_ROOT"):
        return "termux"
    return "local"


HOSTED_ON = where_hosted()

if HOSTED_ON == "local":
    def _ask_input():
        # Ask for Input even on Vps and other platforms.
        def new_input(*args, **kwargs):
            raise EOFError("args=" + str(args) + ", kwargs=" + str(kwargs))

        __builtins__["input"] = new_input

    _ask_input()
