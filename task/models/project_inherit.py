from odoo import models, fields, api, _

class HrEmployee(models.Model):
    _inherit = 'project.project'

    customer_id = fields.Many2one('res.partner', string='Customer')
    paid_unpaid = fields.Selection([('unpaid', 'Unpaid'), ('paid', 'Paid')], string='Paid/Unpaid')
    create_line = fields.One2many('create.order', 'create_id')
    salee_id = fields.Many2one('sale.order', readonly=True)

    def sale_order(self):
        sale_list = []
        for sale in self.create_line:
            sale_list.append(
                (0, 0, {
                    'product_id': sale.product_id.id,
                    'product_uom_qty': sale.quantity_id,
                    'price_unit': sale.price_id,
                    'name': sale.description,
                })
            )
        sale_id = self.env['sale.order'].create({
            'partner_id': self.partner_id.id,
            # 'date_order': self.date_id,
            'order_line': sale_list,
        })
        self.salee_id = sale_id.id

class Create_Lines(models.Model):
    _name = 'create.order'
    _description = 'Create order'
    product_id = fields.Many2one('product.product', string='Products')
    quantity_id = fields.Integer(string="Quantity")
    price_id = fields.Integer(string="Price")
    description = fields.Text(string="Description")
    create_id = fields.Many2one('project.project')
