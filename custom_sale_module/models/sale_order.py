from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    responsible_id = fields.Many2one('hr.employee', string='Responsible for issuing goods', required=True)
    test = fields.Char(string='Test', default=lambda self: self._default_test(), readonly=True)

    @api.model
    def _default_test(self):
        import string, random
        return ''.join(random.choice(string.ascii_letters) for _ in range(10))

    @api.onchange('order_line', 'date_order')
    def _onchange_test(self):
        self.test = f'{self.amount_total} - {self.date_order}'

    @api.constrains('test')
    def _check_test(self):
        for record in self:
            if len(record.test) > 50:
                raise ValidationError(_('The length of the text should be less than 50 characters!'))
