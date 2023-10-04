SAMPLE_PROJECT = {
    "class_prefix": "proj",
    "stylesheet_path": "abstract_project.css",
    "logo_path": "#",
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
    "logo_path": None,
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
    "logo_path": None,
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
    "logo_path": None,
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

PET_PROJECTS = [HEALTH_RECIPES, KCAL_CALC, BLUE_NOTES]
ACADEMIC_PROJECTS = []



