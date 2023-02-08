from odoo import models, fields
from odoo.exceptions import ValidationError


class TutorialLibraryBook(models.Model):
    _name = "tutorial.library.book"
    _description = "Model of tutorial App"

    name = fields.Char("Title", required=True)
    isbn = fields.Char("ISBN")
    active = fields.Boolean("Active?", default=True)
    date_publish = fields.Date()
    image = fields.Binary("Cover")
    publisher_id = fields.Many2one("res.partner", string="Publisher")
    author_ids = fields.Many2many("res.partner", string="Authors")

    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            # De cho co thoi
            # ponderations = [1, 3] * 6
            # terms = [a * b for a, b in zip(digits, ponderations)]
            # remain = sum(terms) % 10
            # check = 10 - remain if remain != 0 else 0

            return True  #

    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise ValidationError("Please provide an ISBN for %s" % book.name)
            if book.isbn and not book._check_isbn():
                raise ValidationError("%s ISBN is invalid" % book.isbn)
        return True
