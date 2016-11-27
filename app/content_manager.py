def Content():
    TOPIC_DICT = { "Application Settup": [["Installation", "/installing-components/"],
                                          ["Architecture", "/app-architecture/"],
                                          ["Coding", "/coding-backend/"],
                                          ["Conclusion", "/app-set-conclusion/"]
                                         ],
                   "App Layout": [["Introduction to Bootstrap", "/about-bootstrap/"],
                                  ["Conclusion", "/bootstrap-conclusion/"]
                                         ],
                   "Jinja2 Templating": [["Overview", "/about-jinja/"],
                                         ["Implementation", "/implement-jinja/"],
                                         ["Conclusion", "/jinja2-conclusion/"]
                                        ],
                   "Users": [["Database", "/sqlite-alchemy/"],
                             ["Database Models", "/db-models/"],
                             ["Flask Forms", "/flask-forms/"],
                             ["Conclusion", "/concluson-on-that/"]
                            ]
                 }
    
    return TOPIC_DICT