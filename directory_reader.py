import os 

class ListingDirectory:
    '''
    This class is to reading all the file and folder in directory,
    then append all the file with spesific extension into the list in dictionary.
    
    on this case (Example):

    source (folder):
        ||
        Hello World! (folder):
            ||
            helloworld (file)
            helloworld.class (file)
            helloworld.c (file)
            helloworld.cpp (file)
            helloworld.py (file)
    
    DICTIONARY = {'Hello World!':['helloworld.c', 'helloworld.cpp', 'helloworld.py']}

    v.1 
    '''

    def __init__(self, path_file):
        self.path_file = path_file
    
    def file_extension_checker(self, file_target):
        accepted_extensions = ['py', 'c', 'cpp', 'js', 'java', 'kt']  # change here for another extensions
        if '.' not in file_target:
            return False
        else:
            file_target_split = file_target.split('.')
            target = file_target_split[1]
            if target in accepted_extensions:
                return True 
            else:
                return False
    
    def make_dictionary(self):
        source_code = os.listdir(self.path_file)
        solution_list = []
        for solution in source_code:
            solution_list.append(solution)

        source_file = {}
        for folder in solution_list:
            tmp = []
            path = "{}/{}/".format(self.path_file,folder)  # change here for different path
            solution_code = os.listdir(path)
            for code in solution_code:
                if self.file_extension_checker(code) == True:
                    tmp.append(code)
            source_file[folder] = tmp
        return source_file