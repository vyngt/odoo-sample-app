from odoo import models, fields


class Partner(models.Model):
    _inherit = "res.partner"
    published_book_ids = fields.One2many(
        "tutorial.library.book", "publisher_id", "Published Books"
    )

    book_ids = fields.Many2many(
        "tutorial.library.book",
        relation="author_rel",
    )
