#Yilun Fu,Mu Li

from makeWebsite import *
import unittest

class TestResume(unittest.TestCase):
    def setUp(self):
        self.lines1 = ["fsdfasdf sdfasf\r\n", "sadfsd@1.com\r\n", "courses-: sdafsdf, Sdfd,A d daf\r\n",
                       "\r\n", "sdafasdfsdf\r\n", "dsafsfge\r\n","----------\r\n","Education\r\n",
                       "university of pennsylvania, master's degree\r\n",
                       "university of pennsylvania, bachelor's degree\r\n"]
        self.lines2 = ["Efsdf Efsfs\r\n", "asdfasdf@sdfa.edu\r\n", "Courses- dasfsdf, dsfefsfs,sdfsfe,sdfsd\r\n",
                       "Projects\r\n", "sdffdfsdfs\r\n", "asdfegwegiwef\r\n", "\r\n",
                       "----------\r\n", "Education\r\n", "university of philadelphia, Master's degree\r\n",
                       "university of philadelphia, bachelor's degree\r\n"]
        self.lines3 = ["@gmail.com","Projects"]
        self.lines4 = ["@gmail.cn"]
        self.lines5 = [""]

    def testisFile(self):
        self.assertEqual(True, isFile("resume.txt"))
        self.assertEqual(False, isFile("xxx.html"))

    def testdetecting_name(self):
        self.assertEqual("Efsdf Efsfs\r\n", detecting_name(self.lines2),'check finding the name')
        self.assertRaises(RuntimeError, detecting_name, self.lines1)

    def testdetecting_email(self):
        self.assertEqual("asdfasdf@sdfa.edu", detecting_email(self.lines2),'check if the email_address is found')
        self.assertEqual("no emails found", detecting_email(self.lines1),'check if the email address is not valid')
        self.assertEqual("no emails found", detecting_email(self.lines3),'check if the email address is not valid')
        self.assertEqual("no emails found", detecting_email(self.lines4),'check if the email address is not valid')
        self.assertEqual("no emails found", detecting_email(self.lines5),'check if no emails found')

    def testdetecting_courses(self):
        self.assertEqual("sdafsdf, Sdfd, A d daf\r\n", detecting_courses(self.lines1),'check the courses in lines1')
        self.assertEqual("dasfsdf, dsfefsfs, sdfsfe, sdfsd\r\n", detecting_courses(self.lines2),'check the courses in lines2')
        self.assertEqual('no courses found',detecting_courses(self.lines3),'check if no courses found')
        
    def testdetecting_project(self):
        self.assertEqual(['no project found'], detecting_project(self.lines1),'check if no project is found')
        self.assertEqual(["sdffdfsdfs\r\n", "asdfegwegiwef\r\n"], detecting_project(self.lines2),'check if we find the project')
        self.assertEqual(['no project found'], detecting_project(self.lines3),'check if "Projects" is the last element in list')
        
    def testdetecting_education(self):
        self.assertEqual(["no degree found"], detecting_education(self.lines1),'check if no degress found')
        self.assertEqual(["university of philadelphia, Master's degree\r\n"], detecting_education(self.lines2),'check the degree in lines2')

    def testsurround_block_text(self):
        self.assertEqual(["<tag>", "tom","</tag>"], surround_block_text("tag","tom"),'check if tag tom->[<tag>,tom,</tag>]')
        self.assertEqual(["<tag>", "Efsdf Efsfs\r\n", "</tag>"], surround_block_text("tag", detecting_name(self.lines2)),'check if this works fine')

    def testsurround_block_list(self):
        self.assertEqual(["<tag>", "sdfsf\r\n", "fsdaf\r\n", "</tag>"], surround_block_list("tag", ["sdfsf\r\n", "fsdaf\r\n"]),'check if this works fine')
        self.assertEqual(["<tag>", "sdffdfsdfs\r\n", "asdfegwegiwef\r\n","</tag>"], surround_block_list("tag", detecting_project(self.lines2)),'check if this works fine')

    def testbuilding_name_and_email(self):
        name_block = building_name_and_email('Yilun Fu','Jinpingxi@gov.cn')
        self.assertEqual(['<div>', '<h1>', 'Yilun Fu', '</h1>', '<p>', 'Email:Jinpingxi@gov.cn', '</p>', '</div>']
                         ,name_block,'check if the building block is working')
        name_block = building_name_and_email('Mu Li','ao@gmail.com')
        self.assertEqual(['<div>', '<h1>', 'Mu Li', '</h1>', '<p>', 'Email:ao@gmail.com', '</p>', '</div>']
                         ,name_block,'check if the building block is working')

    def testbuilidng_education(self):
        education_block = building_education(['Upenn','Tongji'])
        self.assertEqual(['<div>', '<h2>', 'Education', '</h2>', '<ul>', '<li>', 'Upenn', '</li>', '<li>', 'Tongji', '</li>', '</ul>', '</div>']
                         ,education_block,'check if the building block is working')
        education_block = building_education(['Harverd','Yale'])
        self.assertEqual(['<div>', '<h2>', 'Education', '</h2>', '<ul>', '<li>', 'Harverd', '</li>', '<li>', 'Yale', '</li>', '</ul>', '</div>']
                         ,education_block,'check if the building block is working')
        
    def testbuilding_project(self):
        project_block = building_project(['doing optimization','doing discount'])
        self.assertEqual(['<div>', '<h2>', 'Projects', '</h2>', '<ul>', '<li>', '<p>', 'doing optimization', '</p>', '</li>', '<li>', '<p>', 'doing discount', '</p>', '</li>', '</ul>', '</div>']
                         ,project_block,'check if the building block is working')
        project_block = building_project(['merge sort','quick sort'])
        self.assertEqual(['<div>', '<h2>', 'Projects', '</h2>', '<ul>', '<li>', '<p>', 'merge sort', '</p>', '</li>', '<li>', '<p>', 'quick sort', '</p>', '</li>', '</ul>', '</div>']
                         ,project_block,'check if the building block is working')

    def testbuildng_course(self):
        course_block = building_course('cit590,acct613')
        self.assertEqual(['<div>', '<h3>', 'Courses', '</h3>', '<span>', 'cit590,acct613', '</span>', '</div>']
                          ,course_block,'check if the building block is working')
        course_block = building_course('cit597,acct618')
        self.assertEqual(['<div>', '<h3>', 'Courses', '</h3>', '<span>', 'cit597,acct618', '</span>', '</div>']
                          ,course_block,'check if the building block is working')        
        
        
        
        
unittest.main()
