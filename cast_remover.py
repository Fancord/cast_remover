import fileinput
import sys
from os import listdir
from os.path import isfile, join
from typing import cast

if len(sys.argv) == 1:
    print('Insert a path to directory! \n'
          'Example: python cast_remover.py --path <path to project>')
else:
    parameter = sys.argv[1]
    path_to_project = sys.argv[2]

    if parameter == "--path":
        list_of_project_files = [f for f in listdir(path_to_project) if isfile(join(path_to_project, f))]

        for file_name in list_of_project_files:
            with fileinput.FileInput(f'{path_to_project}\\{file_name}', inplace=True, backup='.bak') as file:

                for line in file:
                    if 'cast(' in line:
                        variable = list(line.split())[0]
                        values = eval(' '.join(list(line.split())[2:]))
                        print(f"{variable} = {values}", end='\n')
                    else:
                        print(line, end='')
    else:
        print(f'Unknown parameter {parameter}')