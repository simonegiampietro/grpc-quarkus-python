import os

import grpc_tools.protoc as protoc


class DirInitializer:
    def __init__(self):
        # todo: take this from config
        self.package_name = 'grpc_resources'
        self.proto_path = '../grpc-quarkus/src/main/proto'
        if not self.proto_path.endswith('/'):
            self.proto_path = f'{self.proto_path}/'

    def execute(self):
        self._init_dirs()
        self._create_proto_beans()
        self._replace_package_name()

    def _replace_package_name(self):
        dir_content = os.listdir(self.package_name)
        replacing_files = []
        for file in dir_content:
            if os.path.isfile(os.path.join(self.package_name, file)) and file.endswith('grpc.py'):
                replacing_files.append(file)
        print('Affected modules', replacing_files)
        for filename in replacing_files:
            grpc_index = filename.index('_grpc')
            module_name = filename[0: grpc_index]
            print(f'Replacing package name in {filename} -> {module_name}', end='\t')
            with open(os.path.join(self.package_name, filename), 'r') as file:
                file_content = file.read()
            file_content = file_content.replace(f'import {module_name}', f'import {self.package_name}.{module_name}')
            with open(os.path.join(self.package_name, filename), 'w') as file:
                file.write(file_content)
            print('Done!')

    def _create_proto_beans(self):
        path = os.path.abspath(self.proto_path)
        for file in os.listdir(path):
            if file.endswith('.proto'):
                protoc.main([
                    'grpc_tools.protoc',
                    f'-I{path}',
                    f'--python_out=./{self.package_name}',
                    f'--grpc_python_out=./{self.package_name}',
                    f'{os.path.join(path, file)}'
                ])

    def _init_dirs(self):
        package_file = '__init__.py'
        if self.package_name not in os.listdir('.'):
            os.mkdir(self.package_name)
        if package_file not in os.listdir(self.package_name):
            file = open(f'{self.package_name}/{package_file}', 'w')
            file.write('')
            file.close()


def main():
    operator = DirInitializer()
    operator.execute()


if __name__ == '__main__':
    main()
