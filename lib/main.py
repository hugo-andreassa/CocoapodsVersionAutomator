#!/usr/bin/python3
import os
import sys
import argparse

from os.path import abspath

from podspec_helper import PodspecHelper
from podspec_model import PodspecModel


def main(pods_path: str, spec_path: str, pod_names: []):
    pod_names = [name + '.podspec' for name in pod_names if not name.endswith('.podspec')]

    try:
        podspec_list: [PodspecModel] = PodspecHelper.get_pod_versions(pods_path, pod_names)
        for item in podspec_list:
            print(f'Current version of {item.name} -> {item.version}')
            item.version = input(f'Version to which you want to change the {item.name} -> ')

            item.stspec_path = spec_path
            item.stspec_path = PodspecHelper.find_stspec_path(item.stspec_path, item.name)

            if not PodspecHelper.create_folder(item.stspec_path, item.version):
                print('This version already exists in the STSpec.')
                continue

            PodspecHelper.change_pod_version(item.path, item.version)
            PodspecHelper.copy_podspec_file(item.path, item.stspec_path, item.version)
    except KeyboardInterrupt:
        print('Quitting')
        sys.exit()
    except:
        print('There was an error with the paths you provide')
        sys.exit()


def validate_file(filename):
    if not os.path.exists(filename):
        raise argparse.ArgumentTypeError(f"{filename} does not exist. Please provide a valid path")

    return filename


if __name__ == '__main__':

    # ASCII_art = pyfiglet.figlet_format("VersionAutomator", font='graffiti', width=120)
    # print(ASCII_art)

    parser = argparse.ArgumentParser(description='Foo')
    parser.add_argument("-pP", "--pods-path", dest='podsPath', help="path to your pods folder",
                        type=validate_file, required=True)
    parser.add_argument("-sP", "--spec-path", dest='specPath', help="path to your stSpec folder",
                        type=validate_file, required=True)
    parser.add_argument("-p", "--pods", dest='pods', help="name of the pods you want to change version",
                        nargs='+', default=[], required=True)
    args = parser.parse_args()

    main(abspath(args.podsPath), abspath(args.specPath), [name.strip() for name in args.pods])
