def learn_more_about_project(css_class, href):
    return f"""
        <div class="proj-learnmore-wrapper {css_class}-learnmore-wrapper">
            <div class="proj-learnmore {css_class}-learnmore">
                <a href="{href}" class="proj-learnmore-link {css_class}-learnmore-link">
                    Learn More...
                </a>
            </div>
        </div>
    """