import argparse
import sys
import re


def getparser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input', '-i',
        type=str, default=None,
        help='File, where to read the text')
    parser.add_argument(
        '--output', '-o',
        type=str, default=None,
        help='File, where to write formatted text')
    parser.add_argument(
        '--line-length', '-l',
        type=int, default=None,
        help='The maximum length of a string for formatted text')
    parser.add_argument(
        '--paragraph-spaces', '-p',
        type=int, default=None,
        help='Number of spaces for indenting in a new paragraph')
    parser.parse_args()
    return parser


def readinput(input_file):
    regular = re.compile('(\w+|[,.?!-:\'])')
    textlist = ['\n']

    for line in input_file:
        if line == '\n':
            if textlist[len(textlist)-1] != '\n':
                textlist.append('\n')
        else:
            splitedline = regular.findall(line)
            for element in splitedline:
                if element != '\n':
                    textlist.append(element)

    return textlist


def main():
    args = getparser().parse_args()
    line_length = args.line_length
    paragraph_spaces = str(args.paragraph_spaces)
    inputfile = args.input
    outputfile = str(args.output)
    if inputfile is None:
        input_file = sys.stdin  # read from stdin
    else:
        input_file = open(inputfile, 'r')  # read from file

    textlist = readinput(input_file)

    if outputfile == 'None':
        output_file = sys.stdout
    else:
        output_file = open(outputfile, 'w')

    currentstringlength = 0

    comas = [',', '.', '?', '!', '-', ':', '\\', '\'']

    for iterator in range(len(textlist)):
        if len(textlist[iterator]) > int(line_length) or int(paragraph_spaces) > int(line_length):
            sys.exit(1)

        if textlist[iterator] == '\n':  # beggining of file
            if iterator == 0:
                outputstring = " "*int(paragraph_spaces)
                if int(paragraph_spaces) + len(textlist[1]) > int(line_length):
                    sys.exit(1)
            elif iterator == len(textlist)-1:  # end of file
                continue
            else:
                outputstring = '\n' + " "*int(paragraph_spaces)
            output_file.write(outputstring)
            currentstringlength = int(paragraph_spaces)
        else:
            if textlist[iterator] in comas:
                if currentstringlength < line_length and currentstringlength != 0:
                    output_file.write(textlist[iterator])
                    currentstringlength += 1
                elif currentstringlength == line_length or currentstringlength == 0:
                    if textlist[iterator - 1] == 'stories':
                        print('currentstringlength', currentstringlength)
                    templist = [textlist[iterator]]
                    tempiterator = iterator-1
                    while textlist[tempiterator] in comas:
                        templist.append(textlist[iterator-1])
                        tempiterator -= 1
                    templist.append(textlist[tempiterator])

                    if textlist[iterator - 1] == 'stories':
                        print(templist[1])

                    templist.reverse()
                    tempsum = 0
                    for element in templist:
                        tempsum += len(element)
                    if tempsum > line_length:
                        sys.exit(1)
                    currentstringlength = tempsum
                    outputstring = '\n'
                    for element in templist:
                        outputstring += element
                    output_file.write(outputstring)
                else:
                    sys.exit(1)
            else:
                if textlist[iterator-1] != '\n':
                    outputstring = ' ' + textlist[iterator]
                    if int(currentstringlength) + len(outputstring) < int(line_length):
                        if currentstringlength == 0:
                            output_file.write(outputstring[1:])
                            currentstringlength += len(outputstring) - 1
                        else:
                            output_file.write(outputstring)
                            currentstringlength += len(outputstring)
                    elif int(currentstringlength) + len(outputstring) == int(line_length) and textlist[iterator+1]\
                            not in comas:
                        outputstring += '\n'
                        output_file.write(outputstring)
                        currentstringlength = 0
                    else:
                        outputstring = '\n' + outputstring[1:]
                        output_file.write(outputstring)
                        currentstringlength = len(outputstring)-1
                else:
                    if int(paragraph_spaces) + len(textlist[iterator]) > int(line_length):
                        sys.exit(1)
                    output_file.write(textlist[iterator])
                    currentstringlength += len(textlist[iterator])

main()
