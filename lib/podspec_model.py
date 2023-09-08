class PodspecModel:
    def __init__(self, name, version, path, stspec_path):
        self.name = name
        self.version = version
        self.path = path
        self.stspec_path = stspec_path

    def get_version_splitted(self):
        return self.version.split('.')

    def get_name_without_suffix(self):
        return self.name.replace('.podspec', '')
