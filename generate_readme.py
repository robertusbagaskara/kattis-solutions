#! /usr/bin/python
"""
readme file editor reference: https://readme.so/editor
write and read file with python: https://www.pythontutorial.net/python-basics/python-write-text-file/

You can double click this file if Python already installed and added in your Windows path.
Or you can use the command line: python generate_readme.py / python3 generate_readme.py

v.1
"""
import directory_reader

inputSource = directory_reader.ListingDirectory('source')
dictSource = inputSource.make_dictionary()

def linkProblems(first_problem_solution):
    problem_link = 'https://open.kattis.com/problems/{}'.format(first_problem_solution)
    return problem_link

def linkSolutions(problem_name, solution):
    if ' ' in problem_name:
        problem_name = problem_name.replace(' ', '%20')
    link = 'https://github.com/robertusbagaskara/kattis-solutions/blob/master/source/{}/{}'.format(problem_name, solution)
    readme_link = '[{}]({})'.format(solution, link)
    return readme_link

    

with open('README.md', 'w') as f:
    tmp = 0
    f.write('# Kattis Problem Solution \n')
    f.write('This repository contains some of [Kattis](https://open.kattis.com/) problems that I solved. \n\n')
    f.write(' | No | Problems Name | Solutions |\n')
    f.write(' | -- | ------------- | --------- |\n')
    for key in dictSource:
        list_tmp = dictSource[key]
        tmp += 1
        f.write(' | '+str(tmp))
        target = list_tmp[0].split('.')
        target = target[0]
        f.write(' | [{}]({}) | '.format(key, linkProblems(target)))
        for i in range(len(list_tmp)):
            if i == len(list_tmp)-1:
                f.write(linkSolutions(key, list_tmp[i])+' ')
            else:
                f.write(linkSolutions(key, list_tmp[i])+', ')
        f.write('|')
        f.write('\n')
    f.write('\n\n')

    f.write('## Author:\n')
    f.write('- [@robertusbagaskara](https://github.com/robertusbagaskara)')

print('\nREADME.MD Successfully Generated/Updated \n')
userExit = input('Press ENTER to exit..')
