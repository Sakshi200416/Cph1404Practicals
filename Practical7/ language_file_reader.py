from programming_language import ProgrammingLanguage


def read_languages(filename):
    languages = []
    with open(filename, 'r') as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split(',')
            name, typing, reflection_str, year_str, pointer_str = parts
            language = ProgrammingLanguage(
                name, typing, reflection_str == 'True', int(year_str), pointer_str == 'True')
            languages.append(language)
    return languages


def main():
    languages = read_languages("languages.csv")
    for language in languages:
        print(language)


if __name__ == '__main__':
    main()
