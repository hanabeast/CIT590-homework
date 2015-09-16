#makeWebsite.py
#Yilun Fu, Mu Li
def isFile(string):
    '''It tells whether the entered file exists or not'''
    try:
        open(string)
        return True
    except IOError:
        return False
    


def detecting_name(lines):
    '''detects name and returns a string'''
    if lines[0][0] in map(chr, range(65, 91)):
        return lines[0]
    else:
        raise RuntimeError, "The first character should be an upper letter "


def detecting_email(lines):
    '''detects email and returns a string. '''
    for word in lines:
        if "@" in word:
            idx = word.index("@")
            while word[-1] in [' ','\n','\r']:
                word = word[:-1]
            if (word[idx+1] in map(chr, range(97, 123))) and idx != 0 and (type(word[(idx+1):-4]) == str) and ((word[-4:] == ".edu") or (word[-4:] == ".com")):
                return word #string
    return "no emails found"

def detecting_courses(lines):
    '''detect courses and returns a string'''
    for line in lines:
        if "Courses" in line or "courses" in line:
            idx = line.index("-")
            new_line = line[idx+1:-2]
            lst_course = []
            for course in new_line.split(","):
                i = 0
                while (course[i] not in map(chr, range(65, 91))) and (course[i] not in map(chr, range(97, 123))):
                    i += 1
                course = course[i:]
                lst_course.append(course)
            return ", ".join(lst_course) + "\r\n"#returns a string
    return "no courses found"

def detecting_project(lines):
    '''detects projects and returns a list of strings'''
    lst_project = []
    for line in lines:
            if 'Projects' in line:
                idx = lines.index(line)
                break
    if line != lines[-1]:                   #if we find 'Projects' before the last line, we should make a project list
        for line in lines[idx+1:]:
            if "----------" not in line:
                if line != "\r\n" and line != "\n":
                    lst_project.append(line)
            else:
                break
        return lst_project#list
    else:
        return ['no project found']    #if we don't find 'Projects' before line reachs the last element of lines, no project is found
    
def detecting_education(lines):
    '''detects degrees and returns a list of degrees'''
    lst_edu = []
    for line in lines:
        if "University" in line or "university" in line:
            if "Bachelor" in line or "Master" in line or "Doctor" in line:
                lst_edu.append(line)
    if lst_edu == []:
        return ["no degree found"]
    return lst_edu#list


def surround_block_text(tag, line):#tag is a string, and line is a string
    '''add tag to a string, and returns a list'''
    lines = []
    lines = ["<" + tag + ">", line, "</" + tag + ">"]
    return lines#list

def surround_block_list(tag, lst): #lst is a list
    '''add tag to a list'''
    lst.insert(0, "<" + tag + ">")
    lst.append("</" + tag + ">")
    return lst
    
def building_name_and_email(name, email):
    '''build name and email block in .html'''
    name_line = surround_block_text('h1', name)
    email_address = 'Email:'+email
    email_line = surround_block_text('p', email_address)
    name_email_block = surround_block_list('div', name_line+email_line)
    return name_email_block

def building_education(education):
    '''build education block in .html'''
    degree = []
    first_block = surround_block_text('h2', 'Education')
    for line in education:
        degree.extend(surround_block_text('li', line))
    second_block = surround_block_list('ul', degree)
    education_block = surround_block_list('div', first_block+second_block)
    return education_block

def building_project(project):
    '''build project block in .html'''
    project_list = []
    first_block = surround_block_text('h2', 'Projects')
    for line in project:
        project_list.extend(surround_block_list('li', surround_block_text('p', line)))
    second_block = surround_block_list('ul',project_list)
    project_block = surround_block_list('div', first_block+second_block)
    return project_block

def building_course(course):
    '''bulid course block in .html'''
    first_block = surround_block_text('h3','Courses')
    second_block = surround_block_text('span',course)
    course_block = surround_block_list('div', first_block+second_block)
    return course_block
    
    
def main():
    if isFile('resume_initial.html') and isFile('resume.html'):
        f1 = open('resume_initial.html','r')
        f2 = open('resume.html','r+')
        arrays = f1.readlines()
        f1.close
        f2.seek(0)
        f2.truncate()
        del arrays[-1]
        del arrays[-1]
        f2.writelines(arrays)

    if isFile('resume.txt'):
        fo = open('resume.txt','r')
        lines = fo.readlines()
        name = detecting_name(lines)
        email = detecting_email(lines)
        courses = detecting_courses(lines)
        project = detecting_project(lines)
        education = detecting_education(lines)
        
    name_block = building_name_and_email(name,email)
    if education != ["no degree found"]:
        education_block = building_education(education)
    else:
        education_block = []
    if project != ["no project found"]:
        project_block = building_project(project)
    else:
        project_block = []
    if courses != 'no courses found':
        course_block = building_course(courses)
    else:
        course_block = []
    final_block = ['<div id="page-wrap">\r\n']+name_block+education_block+project_block+course_block+['</div>\r\n','</body>\r\n','</html>\r\n']


    f2.writelines(final_block)
    f2.close()

if __name__ == '__main__':
    main()
    
   
    
            
