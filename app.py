import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Alvi Khan Chowdhury
##### *Resume* 
''')

image = Image.open('Resources/circle_profile_new_image_background_removed.png')
st.image(image, width=150)


#####################
# Custom function for printing text

def txt(a, b, c):
  col1, col2, col3 = st.columns([7,6,4])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

def txt2(a, b, c):
  col1, col2, col3 = st.columns([4,4,4])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

def txt3(a, b):
  col1, col2 = st.columns([7,3])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt4(a, b):
  col1, col2 = st.columns([1,3])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)


#####################
st.markdown('''
## PERSONAL INFORMATION
''')

st.markdown('''
- Date of Birth: 12th December, 1999
- Nationality: Bangladeshi
- Current Address: Taman Mutiara Barat 56000 Kuala Lumpur, Malaysia
- Phone: +60169144899
- Email: alviavailable@gmail.com
- Skype: live:alviavailable
''')

#####################
st.markdown('''
## EDUCATION
''')

txt3('**Bachelor of Science with Honors** (Mechatronic Engineering), *UCSI University*, Kuala Lumpur, Malaysia',
'September 2019 - August 2023')
st.markdown('''
- Current CGPA: `3.64`
''')

txt3('**Cambridge International Examination** (Cambridge International Advanced Level), *Cardiff International School Dhaka*, Dhaka, Bangladesh',
'May 2017 - November 2018')
st.markdown('''
- GPA: `3.23`
''')

txt3('**Cambridge International Examination** (Cambridge International Ordinary Level), *Cardiff International School Dhaka*, Dhaka, Bangladesh',
'May 2015 - June 2016')
st.markdown('''
- GPA: `3.55`
''')


#####################
st.markdown('''
## SKILLS
''')


st.markdown('''
### Computer Skills
''')

txt( '**Skills**', '**Platform**', '**Proficiency**')
txt('ASSEMBLY Programming Language (PIC18F452 Microcontroller Programming)', 'MPLAB X IDE', 'Intermediate' )
txt('C/C++ Programming Language (PIC18F452 Microcontroller Programming)', 'CodeBlocks, MicroC Pro for PIC', 'Intermediate' )
txt('PYTHON Programming Language (Data Visualization, Data Analysis, Machine Learning, Computer Vision, Web App and Chatbot) ', 'Google Colaboratory, Jupyter Notebook, VS Code, Pycharm', 'Intermediate')
txt('SQL Programming Language', 'MYSQL', 'Basic')
txt('DART Programming Language (Android App Development using Flutter)', 'Android Studio', 'Basic')
txt('HTML, CSS and JAVA Script (Web Development)', 'Visual Studio', 'Intermediate')
txt('MATLAB Programming Language', 'MATLAB', 'Intermediate')
txt('Electrical Circuit and PCB Design with Simulations ', ' MATLAB SIMULINK, PSPICE, MULTISIM LIVE, EASY EDA','Excellent')
txt('CAD Design', 'AUTOCAD, SOLIDWORKS, ANSYS', 'Intermediate')
txt('MS Word, MS Excel, MS PowerPoint, PDF, Etcetera', 'MS OFFICE', 'Excellent')
txt('Emails, Presentations, Video Conference, Etcetera', 'Not Applicable', 'Excellent')

st.markdown('''
### Languange Proficiency
''')

txt2('Language', 'Speaking/Hearing', 'Writing/Reading')
txt2('Bengali (Native)', 'Excellent', 'Basic')
txt2('English', 'Excellent', 'Excellent')
txt2('Hindi', 'Intermediate', 'Non-existent')
txt2('Urdu', 'Intermediate', 'Non-existent')

st.markdown('''
### Traits
''')

st.markdown('''
- Great Leader
- Great Listener and Communicator
- People Management Skills
- Self-Learner
- Great Team Player
''')

###################

st.markdown('''
## WORK EXPERIENCE & OTHER ACTIVITIES
''')

st.markdown('''
- Travelled to Singapore, Thailand, Bhutan, Nepal, India, Egypt, Saudi Arabia, Indonesia and most parts of Malaysia.
- Outstanding Volunteer Award from IEEERAS Malaysia Chapter.
- A.T.M TRAVELS and TOURS LTD. Sales Person (October 2018 to December 2018)
- Cakeology BD Sales and Managing Person (February 2019 to April 2019)
- Participant in the Global Project-Based Learning Program 2020 (Online), hosted by Shibaura Institute of Technology, Japan.
- Peer Assisted Learning (PAL) Program Mentor (September 2020 to August 2021)
- Breadboard Incubation Program Senior Committee (September 2020 to August 2021)
- Earned a valid international driving license in Malaysia since January, 2021
- Project Manager for Smart Phone Based Digital Multi-meter Project. (May 2021 to August 2021)
- Completed the Machine Learning with Python course in Japan-Bangladesh Robotics and Technology LTD, JBRTL. (September 2021 to November 2021)
- Finalist at Nott-A-Code: Project-Based Programming Competition. (8th to 27th November, 2021)
- Intern at Japan-Bangladesh Robotics and Advanced Technology Research Centre, JBRATRC. (September 2021 to December 2021)
- General Committee Member at IEEE HKN MU ALPHA, Student Branch, UCSI University. (September 2021 to April 2022)
- Semi-Finalist at TheGreatLab (TGL) Grand Design Challenge 2022. (Team Code: TGD2208) (April 2022 to May 2022)
- Participant in the Apps Innovation Challenge (Online), hosted by Malaysia-Japan International Institute of Technology (MJIIT), Malaysia. (May 2022 to March 2023)
- Executive Committee Member at IEEE HKN MU ALPHA, Student Branch, UCSI University (May 2022 to August 2023)
- Intern at IDEA PLT. (September 2022 to November 2022)
''')

#################

st.markdown('''
## REFERENCES
''')

st.markdown('''
- Dr. Zuliani Binti Zulkoffli, Lecturer, Department of Mechanical and Mechatronic Engineering, UCSI University. (Email: zuliani@ucsiuniversity.edu.my)
- Mr. Manickam Ramasamy, C++/Microprocessor Systems/ Embedded Systems Design Lecturer, Department of Electrical and Electronic Engineering, UCSI University. (Email: ManickamRamasamy@ucsiuniversity.edu.my)
- Assistant Professor Dr Mohamed Khan Afthab Ahamed Khan, IEEERAS Malaysia Chairman (2021-2022), Lecturer, Department of Mechanical and Mechatronic Engineering, UCSI University. (Phone: +60122305451 (Whatsapp))
- Associate Professor Ir Dr Rodney Tan Hean Gay, Smart Multi-meter Supervisor, Lecturer, Department of Electrical and Electronic Engineering, UCSI University. (Email: rodneytan@ucsiuniversity.edu.my)
- Ts Dr. Sarah Atifah Binti Saruchi, TheGreatLab (TGL) Grand Design Challenge Supervisor, Lecturer, Department of Mechanical Engineering, UCSI University. (Email: atifah@ucsiuniversity.edu.my)
- Chai Siew Mei, Peer Assistant Learning Administrator, UCSI University. (Email: chaism@ucsiuniversity.edu.my)
- Lim Jek Shen, Breadboard club Senior, UCSI University. (Email: jekshen00@gmail.com)
- Stephen Yong Luo Sheng, Global Project-Based Learning Program Coordinator, UCSI University. (Email: stph0812@yahoo.com)
- Abul Kalam Azad, A.T.M TRAVELS and TOURS LTD. Owner. (Phone: +8801911351984 (Whatsapp), +8801713005821 (Whatsapp))
- Syed Khalidul Arifeen, Cakeology BD Owner. (Phone: +8801963636364, Email: cakeologybd@gmail.com / sk_arifeen@yahoo.com)
- Nousin Tasnia, Machine Learning with Python Course Instructor. (Email: nousin.tasnia@gmail.com)
- Engineer Mohamad Farhan Ferdous, Founder and Internship Supervisor, JBRATRC. (Email: jbratrc2018@gmail.com)
- Lee Chen Yuek, Technical Support Engineer and Internship Supervisor, IDEA PLT. (Email: walter.lee@idea-plt.com)

''')

##################

st.markdown('''
## SOCIAL MEDIA
''')

txt4('LINKEDIN', 'https://www.linkedin.com/in/alvi-khan-chowdhury-329247214')
txt4('SKYPE', 'https://join.skype.com/invite/WqSUz1bIN38d')
txt4('GitHub', 'https://github.com/AlviKhan99')