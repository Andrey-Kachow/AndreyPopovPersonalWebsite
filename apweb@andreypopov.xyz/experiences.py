from flask import url_for

from main.utils import *

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
        "No idea what is supposed to be here?"
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
        "Tutored Java, Kotlin and Haskell for the assigned group of first-year students",
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
    "duration": "<2 yrs",
    "start_date": "03/07/2022",
    "end_date": "Present",
    "responsibilities": [
        "Tutored Python, C/C++, and Java for more than 20 students",
        "Guided beginners and intermediate level adults and kids",
        "Created lesson plans tailored to the personal requirements of each client",
        "Improved tutees’ academic performance and understanding of the subject",
    ],
    "custom_content": learn_more_about_project("repetitor", "/tutoring-journey"),
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
    "responsibilities": [
        "After successful three years, currently on a target to 2:1",
        "Industrial Placement as a part of a course"# ,
        #"""
        #    <span>
        #        View 
        #    </span>
        #    <a class="imperial-link" href="/icmodules">
        #        summary<!--          
        #    --></a>
        #    <span>
        #        of courses completed
        #    </span>
        #"""
    ]
}


ASHBOURNE = {
    "class_prefix": "ashbourne",
    "stylesheet_path": "ashbourne.css",
    "reference_url": "https://www.ashbournecollege.co.uk/",
    "logo_path": "./static/assets/ashbourne_logo.svg",
    "title": {
        "prefix": "A-Level",
        "highlight": "A*A*A*",
    },
    "duration": "1 ay",
    "start_date": "02/09/2019",
    "end_date": "01/07/2020",
    "responsibilities": [
        "Mathematics, Physics, Further Mathematics"
    ]
}


WELLINGTON = {
    "class_prefix": "wellington",
    "stylesheet_path": "wellington.css",
    "reference_url": "https://www.wellingtoncollege.org.uk/?source=logo",
    "logo_path": "./static/assets/wellington_logo.png",
    "title": {
        "prefix": "AS-Level",
        "highlight": "",
    },
    "duration": "<span class=\"wellington-orange\">1 ay</span>",
    "start_date": "<span class=\"wellington-yellow\">01/09/2017</span>",
    "end_date": "<span class=\"wellington-cyan\">25/06/2018</span>",
    "responsibilities": [
        "Math, Further Math, Computer Science, Physics",
        "Prize Winner. Awarded on Speech Day 2018"
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
        "No idea what is supposed to be here?"
    ]
}

MENG_PROJECT_SAT = {
    "class_prefix": "sat",
    "stylesheet_path": "meng_sat.css",
    "reference_url": "#",
    "logo_path": "#",
    "title": {
        "prefix": "Self-Attachment Technique",
        "highlight": "MEng Project",
    },
    "duration": "1ay",
    "start_date": "01/11/2023",
    "end_date": "24/06/2024",
    "responsibilities": [
        "TODO",
        "TODO",
        "TODO",
        "TODO"
    ]
}

ALGOWIKI_ARTICLE = {
    "class_prefix": "algowiki",
    "stylesheet_path": "algowiki.css",
    "reference_url": "https://www.semanticscholar.org/paper/Formal-Model-of-Problems-%2C-Methods-%2C-Algorithms-and-Popov-Nikitenko/f3796fec3ef7f4ab165992cada3993f6426197fa",
    "logo_path": "./static/assets/nivts.jpeg",
    "title": {
        "prefix": "Research Computing Center of Lomonosov",
        "highlight": "Moscow State University",
    },
    "duration": "1 mos",
    "start_date": "01/07/2018",
    "end_date": "01/08/2018",
    "responsibilities": [
        "Co-authored the article \"Formal Model of Problems, Methods, Algorithms and Implementations in the Advancing AlgoWiki Open Encyclopedia\"",
        "<a class=\"algowiki-link\" href=\"https://www.semanticscholar.org/paper/Formal-Model-of-Problems-%2C-Methods-%2C-Algorithms-and-Popov-Nikitenko/f3796fec3ef7f4ab165992cada3993f6426197fa\">The article can be found here</a>"
    ]
}

WORK_EXPERIENCES = [MINIMAX_LABS, IMPERIAL_PPT, REPETITOR_RU]
EDUCATION_EXPERIENCES = [IMPERIAL, ASHBOURNE, WELLINGTON] # ADD SCHOOLS AND SUMMER SCHOOLS
RESEARCH_EXPERIENCES = [ALGOWIKI_ARTICLE]

