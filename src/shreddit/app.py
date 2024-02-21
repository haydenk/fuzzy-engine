from argparse import ArgumentParser
from os.path import isfile, realpath

from appdirs import user_config_dir

from shreddit.config import Config
from shreddit.shredder import Shredder


def entry():
    parser = ArgumentParser(description="Command-line frontend to the shreddit library.")
    parser.add_argument("-v", "--verbose", help="Override log level to increase output verbosity",
                        default=False, action="store_true")
    parser.add_argument("-c", "--config", help="Config file to use instead of the default shreddit.yml")
    parser.add_argument("-g", "--generate-configs", help="Write shreddit and praw config files to current directory.",
                        action="store_true")
    parser.add_argument("-u", "--user", help="User section from praw.ini if not default", default="default")
    args = parser.parse_args()

    config_filename = user_config_dir("shreddit/shreddit.yml")

    if args.config is not None:
        config_filename = realpath(args.config)

    if not isfile(config_filename):
        print("No shreddit configuration file was found or provided. Run this script with -g to generate one.")
        return

    config: Config = Config(config_filename=config_filename)

    shredder = Shredder(config=config, user=args.user, verbose=args.verbose)
