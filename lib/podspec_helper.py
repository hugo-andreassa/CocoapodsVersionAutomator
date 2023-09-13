import os
import re
import shutil

from podspec_model import PodspecModel

REGEX_POD_VERSION = r"\bversion\s*=\s*[\"']([^\"']+)[\"']"
REGEX_POD_LINE_VERSION = r"(\bversion\s*=\s*[\"'][^\"']+[\"'])"
REGEX_CHANGE_POD_VERSION = r"\b\d+\.\d+.\d\b"


class PodspecHelper:

    @staticmethod
    def find_stspec_path(start_folder: str, pod_name: str):
        pod_name = pod_name.replace('.podspec', '')
        for (dir_path, dir_names, filenames) in os.walk(start_folder):
            if pod_name in dir_names:
                return os.path.join(dir_path, pod_name)

        return None

    @staticmethod
    def create_folder(folder_path: str, folder_name: str) -> bool:
        complete_folder_path = os.path.join(folder_path, folder_name)
        if not os.path.exists(complete_folder_path):
            os.mkdir(complete_folder_path)
            return True
        else:
            return False

    @staticmethod
    def copy_podspec_file(podspec_path: str, stspec_path: str, pod_version: str):
        complete_stspec_path = os.path.join(stspec_path, pod_version)

        shutil.copy(podspec_path, complete_stspec_path)

    @staticmethod
    def get_pod_versions(pod_folder_path: str, pod_names: [str]) -> [PodspecModel]:
        podspec_list = []

        for pod_name in pod_names:
            pod_path = PodspecHelper._find_podspec_path(pod_folder_path, pod_name)
            pod_version = PodspecHelper._find_pod_version(pod_path)

            podspec_model = PodspecModel(pod_name, pod_version, pod_path, '')
            podspec_list.append(podspec_model)

        return podspec_list

    @staticmethod
    def change_pod_version(file_path: str, new_version: str):
        with open(file_path, 'r+') as file:
            file_content = file.read()

            version_number_line = re.findall(REGEX_POD_LINE_VERSION, file_content)[0]
            new_version_number_line = re.sub(REGEX_CHANGE_POD_VERSION, f'{new_version}', version_number_line)

            new_file_content = re.sub(REGEX_POD_VERSION, new_version_number_line, file_content)

        with open(file_path, 'w') as file:
            file.truncate(0)
            file.write(new_file_content)

    @staticmethod
    def _find_podspec_path(start_folder: str, pod_name: str):
        for (dir_path, dir_names, filenames) in os.walk(start_folder):
            for file in filenames:
                if file in pod_name:
                    return os.path.join(dir_path, file)

    @staticmethod
    def _find_pod_version(file_path: str):
        with open(file_path, 'r+') as file:
            file_content = file.read()
            version_number = re.findall(REGEX_POD_VERSION, file_content)
            if version_number:
                return version_number[0]

