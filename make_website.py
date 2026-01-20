from soupsieve.util import lower
import string

stream = []


def read_file(file):
    """
    Does the following:
    1. Opens file (primarily resume.txt)
    2. Reads the line of the file and initializes it towards variable resume_ls
    3. Appends the contents to list stream
    """

    # Reads file into resume_ex
    resume_ex = open(file, 'r')

    # Reads the lines of file into a list
    resume_ls = resume_ex.readlines()

    # Appends the contents of the file into list stream (presumably will use this function primarily for resume.txt)
    for line in resume_ls:
        stream.append(" ".join(line.split()))


def surround_block(tag, text):
    """
    Surrounds the given text with the given html tag and returns the string.
    """
    html_tag = "<" + tag + ">\n" + text + "</" + tag + ">\n"

    return html_tag

def create_email_link(email_address):
    """
    Creates an email link with the given email_address.
    To cut down on spammers harvesting the email address from the webpage,
    displays the email address with [aT] instead of @.

    Example: Given the email address: lbrandon@wharton.upenn.edu
    Generates the email link: <a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>

    Note: If, for some reason the email address does not contain @,
    use the email address as is and don't replace anything.
    """

    # Modified email address from extract_email
    email_address_mod = email_address

    # Replaces @ with [aT]
    if "@" in email_address_mod:
        email_address_mod = email_address_mod.replace("@", "[aT]")
    else:
        return

    # Initializes variable to have correct <a> html tag
    email_tag = "<a " + "href=\"mailto:" + email_address + "\">" + email_address_mod + "</a>"

    # If a number appears in the email address (which is invalid), then the email tag is an empty string
    for number in string.digits:
        if number in email_address_mod:
            email_tag = ""
        else:
            continue

    return email_tag


def extract_email():

    """
    Does the following
    1. Looks for line that has email address
    2. Nested Loop : Checks if it has '.com' or '.edu' and if the domain letter (the letter after @) is lowercase
    3. For other cases that do not have @, gets lines for .edu or .com to see if they are email address. Uses the length of each item
        to figure out the email
    """


    domain_ls = []
    element_index = 0
    email = ""
    for line in stream:
        if "@" in (line):
            # Gets the first letter of the domain (e.g. g in gmail.com)
            domain_letter_index = line.index("@") + 1
            # Gets the domain letter
            domain_letter = line[domain_letter_index]

            # Checks to see if the first domain letter is lowercase
            if line[-4:] in (".com",".edu"):
                # If it is, then email = email address
                if domain_letter.islower():
                        email = line

        # Case when there is no @ in elements. Checks to see if there are .edu or .com cases
        elif ".edu" in (line) or ".com" in (line):
            # Appends those elements to domain_ls list
            domain_ls.append(line)
            item_len = len(domain_ls[0])

            # Iterates over the list to check smallest element
            for item in domain_ls:
                if len(item) <= item_len:
                    element_index = domain_ls.index(item)

            # Smallest element in list is the email address
            email = domain_ls[element_index]

    return email


def extract_name():
    """
    Extracts the name from the first element of the stream list
    """
    resume_orig = stream[0]
    # If the name is lowercase, then it is invalid
    if resume_orig.islower():
        return "invalid"
    # If not, then return resume_orig
    else:
        return resume_orig


def extract_courses():
    """
    Obtains the courses in the Courses element. The following steps are:
    1. Checks the element in Stream for "Courses"
    2. Filters out the random punctuation in the element by checking if there are characters after "Courses"
    3. Get the first element within that Courses line (in this case 'P'), then break out of the loop
    4. Returns the list everything after and including that element
    """
    courses = ""
    first_letter_index = 0
    for line in stream:
        # Checks the "Courses" line
        if "Courses" in line:
            courses = line
            for char in line[7:]:
                # If a character is any letter after 'Courses"
                if char in string.ascii_letters:
                    # Then get the first element that is a character and initialize it
                    first_letter_index = line.index(char)
                    break
    # Return everything after and including that index
    return courses[first_letter_index:]


def extract_projects():
    """
    Extracts the list of projects and appends them into a list
    1. Checks the "Projects" line
    2. As long as the "----------" element has not been reached, continue. If it has been reach, break out of the loop
    3. If an element is blank, ignore it and continue the loop
    4. If there is an element, then append that to the list
    """

    project_line = []
    i = stream.index("Projects")
    for line in stream[i:]:
        # As long as the line is not "----------"
        if "----------" not in (line):
            # If blank, then continue the loop
            if line == "":
                continue
            else:
            # If there is a non-blank, element, append to list
                project_line.append(line)
        # If we hit the element with the dashed line, break out of the loop
        else:
            break

    # Return list of project
    return project_line


def read_write_file(file1, file2, add_text):

    """
    Reads and write to a new file
    1. Open and reads a file and initializes a variable with it
    2. Creates and writes to a new file
    3. Closes the file
    """

    with open(file1) as readfile:

        # reads file1 and initializes text
        text = readfile.read()

        # opens a new file
        write_html = open(file2, 'w')

        # copies the text from the first file to the second file
        write_html.write(text)

        # writes additional text into the new file
        write_html.write(add_text)


        # closes the second file
        write_html.close()


def generate_html(txt_input_file, html_output_file):
    """
    Loads given txt_input_file,
    gets the name, email address, list of projects, and list of courses,
    then writes the info to the given html_output_file.
    """
    courses_str = ""
    projects_str = ""

    # Reads the text file
    read_file(txt_input_file)

    # Obtains the name
    name = extract_name()

     # Obtains the email link
    email_link = create_email_link(extract_email())

    # Gets the list of projects
    projects = extract_projects()

    # Calls to get list of courses
    courses = extract_courses()

    # Inserts lists of courses in string
    for item in extract_courses():
        courses_str += item

    # For loop to iterate over the N number of projects and then calling surround_block("ls", project) N times
    for proj in extract_projects():
        if proj == "Projects":
            continue
        else:
            projects_str += surround_block("li", proj)

    # Initial div tag
    div_tag = "< div id=\"page-wrap\">"

    # Basic information including name and email
    basic_info = surround_block("div",surround_block("h1",name) + surround_block("p", "Email: " + email_link))

    # List of projects calling surround_block()
    projects_ls = surround_block("div",surround_block("h2","Projects") + surround_block("ul", projects_str))

    # List of courses calling surround block
    courses_ls = surround_block("div", surround_block("h3","Courses") + surround_block("span", courses_str))

    full_resume_html = basic_info + projects_ls + courses_ls + "</body>\n" + "</html>\n"

    read_write_file('resume_template.html', html_output_file, full_resume_html)


def main():

    # DO NOT REMOVE OR UPDATE THIS CODE
    # generate resume.html file from provided sample resume.txt
    generate_html('resume.txt', 'resume.html')


    #print(stream[5])
    # DO NOT REMOVE OR UPDATE THIS CODE.
    # Uncomment each call to the generate_html function when you’re ready
    # to test how your program handles each additional test resume.txt file
    #generate_html('TestResumes/resume_bad_name_lowercase/resume.txt', 'TestResumes/resume_bad_name_lowercase/resume.html')
    #generate_html('TestResumes/resume_courses_w_whitespace/resume.txt', 'TestResumes/resume_courses_w_whitespace/resume.html')
    #generate_html('TestResumes/resume_courses_weird_punc/resume.txt', 'TestResumes/resume_courses_weird_punc/resume.html')
    #generate_html('TestResumes/resume_projects_w_whitespace/resume.txt', 'TestResumes/resume_projects_w_whitespace/resume.html')
    #generate_html('TestResumes/resume_projects_with_blanks/resume.txt', 'TestResumes/resume_projects_with_blanks/resume.html')
    #generate_html('TestResumes/resume_template_email_w_whitespace/resume.txt', 'TestResumes/resume_template_email_w_whitespace/resume.html')
    #generate_html('TestResumes/resume_wrong_email/resume.txt', 'TestResumes/resume_wrong_email/resume.html')

    # If you want to test additional resume files, call the generate_html function with the given .txt file
    # and desired name of output .html file

if __name__ == '__main__':
    main()