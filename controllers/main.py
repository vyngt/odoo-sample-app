from odoo import http


class Books(http.Controller):
    @http.route("/tutorial-library/books")
    def list(self):
        Book = http.request.env["tutorial.library.book"]
        books = Book.search([])
        return http.request.render(
            "tutorial.book_list_template",
            {"books": books},
        )
