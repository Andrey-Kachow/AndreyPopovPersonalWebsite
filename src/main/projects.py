SAMPLE_PROJECT = {
    "class_prefix": "proj",
    "stylesheet_path": "abstract_project.css",
    "logo_url": "#",
    "logo_substitute": None,
    "title": "Some Abstract Project",
    "status": "Unreleased",
    "dates": {
        "since": "1999",
        "until": "Present",
    },
    "keywords": [
        "Java",
        "Python",
        "CI/CD"
    ],
    "repo_link": "#",
    "interesting_things": [ 
        "Something interesting about this projects",
        "Another interesting thing",
        "Third exciting feature"
    ],
    "custom_content": "",
}

def android_app_demo_and_apk_html(class_name, apk_name, youtube_link):
    return f"""
        <div class="proj-download-apk {class_name}-download-apk">
            Download: 
            <a class="{class_name}-link" href="/static/download/{apk_name}" download>
                {apk_name}
            </a>
        </div>
        <div class="proj-youtube-demo-link {class_name}-youtube-demo-link">
            YouTube:
            <a class="{class_name}-link" href="{youtube_link}">
                video Demostration
            </a>
        </div>
    """

def simple_text_header(title, class_name):
    return f"""
        <div class="proj-align-logo-sub {class_name}-align-logo-sub">
            <span class="proj-big-header-logo {class_name}-big-header-logo">
                {title}
            </span>
        </div>
    """

HEALTH_RECIPES = {
    "class_prefix": "recipes",
    "stylesheet_path": "health_recipes.css",
    "logo_url": None,
    "logo_substitute": simple_text_header("Recipes of Health", "recipes"),
    "title": "Android App Project",
    "status": "MVP completed",
    "dates": {
        "since": "07/08/2021",
        "until": "10/08/2021",
    },
    "keywords": [
        "Kotlin",
        "Android",
        "Sqlite"
    ],
    "repo_link": "https://github.com/Andrey-Kachow/HealthRecipes",
    "interesting_things": [ 
        "Food recipes database viewer",
        "Searching and swiping functionality",
    ],
    "custom_content": 
        android_app_demo_and_apk_html(
            'recipes',
            'health_recipes.apk',
            'https://youtu.be/X_IJu1LoQ2w'
        ),
}


KCAL_CALC = {
    "class_prefix": "kcal",
    "stylesheet_path": "kcal_calc.css",
    "logo_url": None,
    "logo_substitute": simple_text_header("Calorie Calculator", "kcal"),
    "title": "Android App Project",
    "status": "MVP completed",
    "dates": {
        "since": "05/08/2021",
        "until": "07/08/2021",
    },
    "keywords": [
        "Kotlin",
        "Android",
        "Sqlite"
    ],
    "repo_link": "https://github.com/Andrey-Kachow/KcalCalc",
    "interesting_things": [ 
        "A simple calorie calculator that takes training time into account",
    ],
    "custom_content": 
        android_app_demo_and_apk_html(
            'kcal',
            'kcal_calc.apk',
            'https://youtu.be/36VbHhkn97s'
        ),
}

BLUE_NOTES = {
    "class_prefix": "blue-notes",
    "stylesheet_path": "blue_notes.css",
    "logo_url": None,
    "logo_substitute": simple_text_header("Blue Notes", "blue-notes"),
    "title": "Android App Project",
    "status": "MVP completed",
    "dates": {
        "since": "01/08/2021",
        "until": "03/08/2021",
    },
    "keywords": [
        "Kotlin",
        "Android",
        "Sqlite"
    ],
    "repo_link": "https://github.com/Andrey-Kachow/BlueNotes.git",
    "interesting_things": [ 
        "A simple TODO list notes beginner app",
        "Self educating project",
    ],
    "custom_content": 
        android_app_demo_and_apk_html(
            'blue-notes',
            'blue_notes.apk',
            'https://youtube.com/shorts/b0XIvoEKtFw?feature=share'
        ),
}

PADAVAN = {
    "class_prefix": "padavan",
    "stylesheet_path": "padavan.css",
    "logo_url": None,
    "logo_substitute": simple_text_header("Padavan", "padavan"),
    "title": "Teaching Resourcecs Repo",
    "status": "Active",
    "dates": {
        "since": "01/02/2022",
        "until": "Present",
    },
    "keywords": [
        "Python",
        "C/C++",
        "Java",
        "Tutoring"
    ],
    "repo_link": "https://github.com/Andrey-Kachow/PadavanPy",
    "interesting_things": [ 
        "Collection of demos and small projects in different languages",
        "Used for teaching my students",
        "Successful exercises are reused and shared with other tutees"
    ],
    "custom_content": ""
}


ANDREY_POPOV_XYZ = {
    "class_prefix": "andrey-popov-xyz",
    "stylesheet_path": "andrey_popov_xyz.css",
    "logo_url": None,
    "logo_substitute": simple_text_header("AndreyPopov.xyz", "andrey-popov-xyz"),
    "title": "Website Project",
    "status": "Released",
    "dates": {
        "since": "17/09/2022",
        "until": "Present",
    },
    "keywords": [
        "Python",
        "Flask",
        "html/css/js",
        "Vim"
    ],
    "repo_link": "https://github.com/Andrey-Kachow/AndreyPopovPersonalWebsite",
    "interesting_things": [ 
        "The website objserved is also my pet project",
    ],
    "custom_content": """
        <div style="width: 100%; height: 12rem; padding: 1rem;">
            {% include 'includes/website_miniature.html' %}
        </div>
    """
}

FRESHLIFE = {
    "class_prefix": "freshlife",
    "stylesheet_path": "freshlife.css",
    "logo_url": None,
    "logo_substitute": simple_text_header("FRESHLIFE", "freshlife"),
    "title": "Web App Project",
    "status": "MVP Completed",
    "dates": {
        "since": "01/09/2018",
        "until": "Present",
    },
    "keywords": [
        "Python",
        "Django",
        "html-css-js"
    ],
    "repo_link": "https://github.com/Andrey-Kachow/NeaFreshLife",
    "interesting_things": [ 
        "Meal Planner and Calorie Calculator with web based interface",
        "A-Level Computer Science NEA Project",
    ],
    "custom_content": "" 
}

SCALING_EXTREME_STARTUP = {
    "class_prefix": "extreme-startup",
    "stylesheet_path": "extreme_startup.css",
    "logo_url": "/static/assets/Scaling_Extreme_Startup_logo.png",
    "logo_substitute": simple_text_header(
        "Scaling <span class=\"extreme-startup-highlight-text\">Extreme</span> Startup",
        "extreme-startup"
    ),
    "title": "Group Project",
    "status": "Published",
    "dates": {
        "display_anyway": True,
        "since": "09/09/2022",
        "until": "06/01/2023",
    },
    "keywords": [
        "Python",
        "Flask",
        "React.js",
        "MongoDB",
        "AWS",
        "Lambda",
    ],
    "repo_link": "https://github.com/mike-sorokin/extreme-startup",
    "interesting_things": [ 
        "Developed software in Scrum framework as a team of six people",
        "Produced an online game for competitive programmers",
        "Managed Frontend and Testing, as well as contributed to Backend and CI/CD",
        """
        The product has been successfully applied at
        <a class="extreme-startup-link" href="https://www.db.com/uk">Deutsche Bank</a>
        CI/CD workshop
        """
    ],
    "custom_content": """
        <div class="extreme-startup-learnmore-wrapper">
            <div class="extreme-startup-learnmore">
                <a href="/scaling-extreme-startup" class="extreme-startup-learnmore-link">
                    Lean More...
                </a>
            </div>
        </div>
    """
}

MMMBOXES = {
    "class_prefix": "mmmboxes",
    "stylesheet_path": "mmmboxes.css",
    "logo_url": "/static/assets/MmmmBoxes_logo.png",
    "logo_substitute": simple_text_header("MmmmBoxes", "mmmboxes"),
    "title": "Group Project",
    "status": "Published",
    "dates": {
        "display_anyway": True,
        "since": "15/05/2022",
        "until": "25/06/2022",
    },
    "keywords": [
        "Python",
        "Flask",
        "JavaScript",
        "PostgreSQL",
    ],
    "repo_link": "https://github.com/Andrey-Kachow/MmmmBoxes",
    "interesting_things": [ 
        "Identified a problem in the managing of package collection at universities",
        "Created a system, in a group of four, that manages deliveries and storage",
        "Deployed an application on Heroku with GitLab CI/CD pipeline being set",
        "Contacted end users regularly for continuous feedback to adapt to their needs"
    ],
    "custom_content":"" 
}

WACC = {
    "class_prefix": "wacc",
    "stylesheet_path": "wacc.css",
    "logo_url": None,
    "logo_substitute": simple_text_header("WACC Compiler", "wacc"),
    "title": "Compliers Group Project",
    "status": "Submitted",
    "dates": {
        "display_anyway": True,
        "since": "14/01/2022",
        "until": "24/03/2022",
    },
    "keywords": [
        "Kotlin",
        "ANTLR",
        "ARM",
        "Python",
        "Tkinter",
    ],
    "repo_link": "#",
    "interesting_things": [ 
        "In a group of four developed a WACC programming language compiler",
        "Implemented translation of a high level language WACC to ARM assembly",
        "Created an IDE for WACC with syntax highlighting and error detection",
        "Built a CI/CD pipeline to support quality control via rich test suite"
    ],
    "custom_content":"" 
}

DEVOPS_CICD = {
    "class_prefix": "devops-cicd",
    "stylesheet_path": "devops_cicd.css",
    "logo_url": None,
    "logo_substitute": simple_text_header("DevOps and CI/CD Project", "devops-cicd"),
    "title": "Group Project",
    "status": "Submitted",
    "dates": {
        "display_anyway": True,
        "since": "01/01/2022",
        "until": "13/01/2022",
    },
    "keywords": [
        "Java",
        "Python",
        "Docker",
        "GitLab-Runner",
        "Haskell",
    ],
    "repo_link": "#",
    "interesting_things": [ 
        "Coordinated a group to deploy a Java servlet Web application on a virtual server",
        "Set a working Build-Test-Deploy pipeline using GitLab-Runner",
        "Used Docker for managing dependencies and extension tools",
        "Implemented additional funcitonalit and Python and combined Docker container"
    ],
    "custom_content":"" 
}

PINTOS = {
    "class_prefix": "pintos",
    "stylesheet_path": "pintos.css",
    "logo_url": None,
    "logo_substitute": simple_text_header("PINTOS", "pintos"),
    "title": "OS Group Project",
    "status": "Submitted",
    "dates": {
        "display_anyway": True,
        "since": "03/10/2021",
        "until": "01/12/2022",
    },
    "keywords": [
        "C",
        "Operating-Systems",
        "x86-Assembly",
    ],
    "repo_link": "#",
    "interesting_things": [ 
        "Worked in a group of four and commited to daily meetings",
        "Extended the source code of an academic operating system PintOS",
        "Implemented priority scheduling, user processes execution and virtual memory",
    ],
    "custom_content":"" 
}

ARM11_EMULATOR = {
    "class_prefix": "arm11-emulator",
    "stylesheet_path": "arm11_emulator.css",
    "logo_url": None,
    "logo_substitute": simple_text_header("ARM11 Emulator and Assembler", "arm11-emulator"),
    "title": "Group Project",
    "status": "Published",
    "dates": {
        "display_anyway": True,
        "since": "12/05/2021",
        "until": "17/06/2021",
    },
    "keywords": [
        "C",
        "Arm-Assembly",
        "Emulation",
    ],
    "repo_link": "https://github.com/DFcupello/ARM-Project",
    "interesting_things": [ 
        "Implemented Arm emulation and Assembly in C programming Language"
        "Commited to a remote group work with a team of four people",
        "Supported a subset of Arm instruction set",
        "Familiarised myself with Git usage for team projects"
    ],
    "custom_content":"" 
}
_SCALING_EXTREME_STARTUP = {
    "class_prefix": "extreme-startup",
    "stylesheet_path": "extreme_startup.css",
    "logo_url": None,
    "logo_substitute": simple_text_header("Scaling Extreme Startup", "extreme-startup"),
    "title": "Group Project",
    "status": "Published",
    "dates": {
        "display_anyway": True,
        "since": "09/09/2022",
        "until": "06/01/2023",
    },
    "keywords": [
        "Python",
        "Flask",
        "React.js",
        "MongoDB",
        "AWS",
        "Lambda",
    ],
    "repo_link": "https://github.com/mike-sorokin/extreme-startup",
    "interesting_things": [ 
        "Developed software in Scrum framework as a team of six people",
        "Produced an online game for competitive programmers",
        "Managed Frontend and Testing, as well as contributed to Backend and CI/CD",
        "Successfully applied the product at CI/CD workshop at Deutsche Bank"
    ],
    "custom_content":"" 
}

PET_PROJECTS = [
        HEALTH_RECIPES, KCAL_CALC,        BLUE_NOTES,
        PADAVAN,        ANDREY_POPOV_XYZ, FRESHLIFE
]
ACADEMIC_PROJECTS = [
        SCALING_EXTREME_STARTUP, MMMBOXES, WACC, 
        DEVOPS_CICD,             PINTOS,   ARM11_EMULATOR
]



