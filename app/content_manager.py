# Resource for advanced content management: https://www.youtube.com/watch?v=xdstIR3prSk&index=22&list=PLQVvvaa0QuDc_owjTbIY4rbgXOFkUYOUB

def Content():
    TOPIC_DICT = { "Application Settup": [["Installation", "/topics/installing-components/"],
                                          ["Architecture", "/topics/app-architecture/"],
                                          ["Coding Basics", "/topics/coding-basics/"],
                                          ["Conclusion", "/topics/app-setup-conclusion/"]
                                         ],
                   "App Layout": [["Introduction to Bootstrap", "/topics/about-bootstrap/"],
                                  ["Conclusion", "/topics/bootstrap-conclusion/"]
                                         ],
                   "Jinja2 Templating": [["Overview", "/topics/what-is-jinja2/"],
                                         ["Implementation", "/topics/how-to-jinja/"],
                                         ["Conclusion", "/topics/jinja2-conclusion/"]
                                        ],
                   "Users": [["SQLAlchemy Database", "/topics/sqlite-alchemy/"],
                             ["Database Models", "/topics/db-models/"],
                             ["Flask Forms", "/topics/flask-forms/"],
                             ["Conclusion", "/topics/database-conclusion/"]
                            ]
                 }
    
    return TOPIC_DICT