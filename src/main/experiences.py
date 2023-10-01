from flask import url_for


SAMPLE_EXPERIENCE = {
    "class_prefix": "testpr",
    "stylesheet_path": "abstract_experience.css",
    "reference_url": "#",
    "logo_path": "#",
    "title": {
        "prefix": "Software Engineering",
        "highlight": "Pro",
    },
    "duration": "100 yrs",
    "start_date": "31/10/1999",
    "end_date": "31/10/2099",
    "responsibilities": [
        "Was cool and fun",
        "Did interesting projects",
        "Something sample third",
        "Mo idea what is supposed to be here"
    ]
}


MINIMAX_LABS = {
    "class_prefix": "mmx",
    "stylesheet_path": "minimaxlabs.css",
    "reference_url": "https://www.minimaxlabs.com/",
    "logo_path": "./static/assets/mmx_logo_white.svg",
    "title": {
        "prefix": "Software Engineering",
        "highlight": "Intern",
    },
    "duration": "6 mos",
    "start_date": "03/04/2023",
    "end_date": "29/09/2023",
    "responsibilities": [
        "Developed Eclipse Desktop Application using the Java programming language",
        "Created new views/reports/tools for LNG optimization as well as maintained existing ones",
        "Acquired experience with EMF framework",
        "Worked on a brand new company website using HTML/CSS/JS"
    ]
}


IMPERIAL_PPT = {
    "class_prefix": "imperial",
    "stylesheet_path": "imperial_ppt_uta.css",
    "reference_url": "https://www.imperial.ac.uk/",
    "logo_path": "./static/assets/imperial_logo.svg",
    "title": {
        "prefix": "PPT - Undergraduate",
        "highlight": "Teaching Assistant",
    },
    "duration": "6 mos",
    "start_date": "29/09/2022",
    "end_date": "23/03/2023",
    "responsibilities": [
        "Worked as a Personal Programming Tutor and provided teaching support",
        "Tutored Java, Kotlin and Haskell for the assigned group of first year students",
        "Conducted Question-Answer seminars and revision sessions",
        "Reviewed and marked students’ work and provided constructive feedback"
    ]
}


REPETITOR_RU = {
    "class_prefix": "repetitor",
    "stylesheet_path": "repetitor_ru.css",
    "reference_url": "https://repetitor.ru/view/repetitor-po-programmirovaniyu-popov-andrej-konstantinovich-66939",
    "logo_path": "./static/assets/repetitor_ru_mylogo.svg",
    "title": {
        "prefix": "Computer Science",
        "highlight": "Tutor",
    },
    "duration": "3 mos",
    "start_date": "03/07/2022",
    "end_date": "02/10/2023",
    "responsibilities": [
        "Tutored Python, C/C++, and Java",
        "Guided beginners and intermediate level adults and kids",
        "Created lesson plans tailored to the personal requirements of each client",
        "Improved tutees’ academic performance and understanding of the subject"
    ]
}

IMPERIAL = {
    "class_prefix": "imperial",
    "stylesheet_path": "imperial.css",
    "reference_url": "https://www.imperial.ac.uk/",
    "logo_path": "./static/assets/imperial_logo.svg",
    "title": {
        "prefix": "Computing",
        "highlight": "MEng <small>(Expected)</small>",
    },
    "duration": "4 ay",
    "start_date": "01/10/2020",
    "end_date": "01/07/2024",
    "responsibilities": []
}


ASHBOURNE = {
    "class_prefix": "ashbourne",
    "stylesheet_path": "ashbourne.css",
    "reference_url": "https://www.ashbournecollege.co.uk/",
    "logo_path": "./static/assets/ashbourne_logo.svg",
    "title": {
        "prefix": "Mathematics, Physics, Further Mathematics",
        "highlight": "A*A*A*",
    },
    "duration": "1 ay",
    "start_date": "01/01/2020",
    "end_date": "01/07/2020",
    "responsibilities": []
}


IMPERIALa = {
    "class_prefix": "imperial",
    "stylesheet_path": "imperial.css",
    "reference_url": "https://www.imperial.ac.uk/",
    "logo_path": "./static/assets/imperial_logo.svg",
    "title": {
        "prefix": "Computing",
        "highlight": "MEng <small>(Expected)</small>",
    },
    "duration": "4 ay",
    "start_date": "01/10/2020",
    "end_date": "01/07/2024",
    "responsibilities": []
}

SAMPLE_EXPERIENCE = {
    "class_prefix": "testpr",
    "stylesheet_path": "abstract_experience.css",
    "reference_url": "#",
    "logo_path": "#",
    "title": {
        "prefix": "Software Engineering",
        "highlight": "Pro",
    },
    "duration": "100 yrs",
    "start_date": "31/10/1999",
    "end_date": "31/10/2099",
    "responsibilities": [
        "Was cool and fun",
        "Did interesting projects",
        "Something sample third",
        "Mo idea what is supposed to be here"
    ]
}

SAMPLE_EXPERIENCE = {
    "class_prefix": "testpr",
    "stylesheet_path": "abstract_experience.css",
    "reference_url": "#",
    "logo_path": "#",
    "title": {
        "prefix": "Software Engineering",
        "highlight": "Pro",
    },
    "duration": "100 yrs",
    "start_date": "31/10/1999",
    "end_date": "31/10/2099",
    "responsibilities": [
        "Was cool and fun",
        "Did interesting projects",
        "Something sample third",
        "Mo idea what is supposed to be here"
    ]
}

SAMPLE_EXPERIENCE = {
    "class_prefix": "testpr",
    "stylesheet_path": "abstract_experience.css",
    "reference_url": "#",
    "logo_path": "#",
    "title": {
        "prefix": "Software Engineering",
        "highlight": "Pro",
    },
    "duration": "100 yrs",
    "start_date": "31/10/1999",
    "end_date": "31/10/2099",
    "responsibilities": [
        "Was cool and fun",
        "Did interesting projects",
        "Something sample third",
        "Mo idea what is supposed to be here"
    ]
}

WORK_EXPERIENCES = [MINIMAX_LABS, IMPERIAL_PPT, REPETITOR_RU]
EDUCATION_EXPERIENCES = [IMPERIAL, ASHBOURNE] # ADD SCHOOLS AND SUMMER SCHOOLS
# RESEARCH_EXPERIENCES = [ALGOWIKI_ARTICLE]
# ACADEMIC_PROJECTS = [EXPREME_RESTARTUP, MMMBOXES, WACC, DEVOPS_PROJECT, PINTOS, ARM11_EMULATOR]
'''
PET_PROJECTS = [
    # TIC_TAC_TOE_ULTIMATE_GODOT, # ?? note yet started
    # TIC_TAC_TOE_ULTIMATE_ANDROID, # ? not yet started
    # TIC_TAC_TOE_ULTIMATE_CPP, # ? not yet started
    APOPOV_WEBSITE, 
    PADAVAN_PY, 
    HEALTH_RECIPES, 
    KCAL_CALC,
    BLUE_NOTES, 
    NEA_FRESH_LIFE, # ?
    BLOB_OF_FURY, # ??
]
'''
# TUTEES?
