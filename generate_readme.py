#! /usr/bin/python
"""
readme file editor reference: https://readme.so/editor
write and read file with python: https://www.pythontutorial.net/python-basics/python-write-text-file/

You can double click this file if Python already installed and added in your Windows path.
Or you can use the command line: python generate_readme.py / python3 generate_readme.py

v.1.1.3
"""
import directory_reader
import kattis_scrapper
from datetime import date

inputSource = directory_reader.ListingDirectory('source')
dictSource = inputSource.make_dictionary()

def linkProblems(first_problem_solution):
    problem_link = 'https://open.kattis.com/problems/{}'.format(first_problem_solution)
    return problem_link

def linkSolutions(problem_name, solution):
    if ' ' in problem_name:
        problem_name = problem_name.replace(' ', '%20')
    link = 'https://github.com/robertusbagaskara/kattis-solutions/blob/master/source/{}/{}'.format(problem_name, solution)
    extension = None
    if '.py' in solution:
        extension = 'Python'
    elif '.cpp' in solution:
        extension = 'C++'
    elif '.c' in solution:
        extension = 'C'
    elif '.js' in solution:
        extension = 'Javascript'
    elif '.java' in solution:
        extension = 'Java'
    elif '.kt' in solution:
        extension = 'Kotlin'
    elif '.go' in solution:
        extension = 'Go'
    elif '.rs' in solution:
        extension = 'Rust'
    elif '.rb' in solution:
        extension = 'Ruby'
    elif '.vb' in solution:
        extension = 'Visual Basic'
    readme_link = '[{}]({})'.format(extension, link)
    return readme_link

def writingReadme(option):
    if option.lower() == 'y':
        scrapper = kattis_scrapper.PointScrapper()
    with open('README.md', 'w', encoding='UTF-8') as f:
        tmp = 0
        f.write('# Kattis Problem Solution \n')
        f.write('This repository contains with my solutions that solve some problem in [Kattis Problem Archive](https://open.kattis.com/). \n\n')
        f.write('Score updated on: ' + str(date.today().strftime("%B %d, %Y")) + '\n\n')
        if option.lower() == 'y':
            f.write(' | No | Problems Name | Solutions | Difficulty |\n')
            f.write(' | -- | ------------- | --------- | ---------- |\n')
        else:
            f.write(' | No | Problems Name | Solutions |\n')
            f.write(' | -- | ------------- | --------- |\n')
        for key in dictSource:
            list_tmp = dictSource[key]
            tmp += 1
            f.write(' | '+str(tmp))
            target = list_tmp[0].split('.')
            target = target[0]
            problem_link = linkProblems(target)
            f.write(' | [{}]({}) | '.format(key, problem_link))
            for i in range(len(list_tmp)):
                if i == len(list_tmp)-1:
                    f.write(linkSolutions(key, list_tmp[i])+' ')
                else:
                    f.write(linkSolutions(key, list_tmp[i])+', ')
            f.write('|')
            if option.lower() == 'y':
                f.write(scrapper.getPoints(problem_link))
                f.write('|')
                print(problem_link)
                print(f"scrapping {tmp} from total {len(dictSource)}")
            f.write('\n')
        f.write('\n\n')

        f.write('## Author:\n')
        f.write('- [Robertus Bagaskara](https://open.kattis.com/users/robertusbagaskara)')

        print('\nREADME.MD Successfully Generated/Updated \n')
        userExit = input('Press ENTER to exit..')


if __name__ == '__main__':
    userInput = input("Do you want to show 'Difficulty' or not (y/n)? ")
    writingReadme(userInput)