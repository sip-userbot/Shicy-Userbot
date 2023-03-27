import sys

from ShicyXd import DEVS, LOAD, LOGS, NO_LOAD
from ShicyXd.shicy._baseyins import ShicyDB

adB = ShicyDB()


def __list_all_modules():
    import glob
    from os.path import basename, dirname, isfile

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    if LOAD or NO_LOAD:
        to_load = LOAD
        if to_load:
            if not all(
                any(mod == module_name for module_name in all_modules)
                for mod in to_load
            ):
                LOGS.error("Nama Modules yang anda masukan salah.")
                sys.exit(1)
        else:
            to_load = all_modules
        if NO_LOAD:
            LOGS.info("Modules No Load : {}".format(NO_LOAD))
            return [item for item in to_load if item not in NO_LOAD]
        return to_load
    return all_modules


ALL_MODULES = sorted(__list_all_modules())
LOGS.info(f"Connecting to {adB.name}...")
if adB.ping():
    LOGS.info(f"Connected to {adB.name} Successfully!")
LOGS.info("Starting To Load Plugins")
LOGS.info(
    f"Succesfully Load {len(ALL_MODULES)} Plugins",
)
__all__ = ALL_MODULES + ["ALL_MODULES"]
