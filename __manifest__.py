{
    "name": "Tutorial Application",
    "summary": "Tutorial of VyNT",
    "description": """
    ====================
    Long description
    *hello*
    **world**

    Bullet Hell:
    - 1
    - 2
    - 3
    ====================
    """,
    "author": "Nguyen The Vy",
    "website": "https://github.com/vyngt/odoo-sample-app",
    "category": "Services/Library",
    "version": "16.0.1.0.0",
    "depends": ["base"],
    "data": [
        "security/tutorial_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/menu.xml",
        "views/book_list_template.xml",
    ],
    "application": True,
    # "demo": ["demo.xml"],
}
