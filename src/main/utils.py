def learn_more_about_project(css_class, href):
    return f"""
        <div class="{css_class}-learnmore-wrapper">
            <div class="{css_class}-learnmore">
                <a href="{href}" class="{css_class}-learnmore-link">
                    Learn More...
                </a>
            </div>
        </div>
    """