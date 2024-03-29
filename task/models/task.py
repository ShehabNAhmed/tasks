from odoo import models, fields, api

class TaskTest(models.Model):
    _name = 'task.test'
    _description = 'Task to hiring'

    name = fields.Char(string='Task Name')
    paid_unpaid = fields.Selection([('unpaid', 'Unpaid'), ('paid', 'Paid')], string='Paid/Unpaid')
    customer_id = fields.Many2one('res.partner', string='Customer')
    company_id = fields.Many2one('res.company', string='Company')
    order_line_id = fields.Many2one('sale.order.line', string='Order Line')
    product_id=fields.Many2one('product.product', string='Product', required=True)
    create_line = fields.One2many('create.lines', 'create_id')
    sale_id = fields.Many2one('sale.order', readonly=True)

    def sale_order(self):
        sale_list = []
        for sale in self.create_line:
            sale_list.append(
                (0, 0, {
                    'product_id': sale.product_id.id,
                    'product_uom_qty': sale.quantity_id,
                    'price_unit': sale.price_id,
                })
            )
        sale_id = self.env['sale.order'].create({
            'partner_id': self.customer_id.id,
            # 'date_order': self.date_id,
            'order_line': sale_list,
        })
        self.sale_id = sale_id.id


    def Order_Line(self):
       print("task")

    @api.onchange('paid_unpaid')
    def _onchange_paid_unpaid(self):
        if self.paid_unpaid == 'unpaid':
            self.order_line_id = False




class Create_Lines(models.Model):
    _name = 'create.lines'
    _description = 'Create Lines'

    product_id = fields.Many2one('product.product', string='Product')

    quantity_id = fields.Integer(string="Quantity")
    price_id = fields.Integer(string="Price")
    description = fields.Text(string="Description")
    create_id = fields.Many2one('task.test')





