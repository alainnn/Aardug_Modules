# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

from odoo import models, fields, api, _


class ProcurementOrderInherit(models.Model):
    _inherit = 'procurement.order'

    def _create_service_task(self):
        project = self._get_project()
        planned_hours = self._convert_qty_company_hours()
        nameContent = []
        nameContent.append(self.sale_line_id.order_id.partner_id.city or '')
        nameContent.append(self.sale_line_id.order_id.partner_id.name or '')
        nameContent.append(self.origin or '')
        nameContent.append(self.product_id.name or '')
        name = ' - '.join([x for x in nameContent if x])
        task = self.env['project.task'].create({
            'name': name,
            'date_deadline': self.date_planned,
            'planned_hours': planned_hours,
            'remaining_hours': planned_hours,
            'partner_id': self.sale_line_id.order_id.partner_id.id or self.partner_dest_id.id,
            'user_id': self.env.uid,
            'procurement_id': self.id,
            'description': self.name + '<br/>',
            'project_id': project.id,
            'company_id': self.company_id.id,
        })
        self.write({'task_id': task.id})

        msg_body = _("Task Created (%s): <a href=# data-oe-model=project.task data-oe-id=%d>%s</a>") % (self.product_id.name, task.id, task.name)
        self.message_post(body=msg_body)
        if self.sale_line_id.order_id:
            self.sale_line_id.order_id.message_post(body=msg_body)
            task_msg = _("This task has been created from: <a href=# data-oe-model=sale.order data-oe-id=%d>%s</a> (%s)") % (self.sale_line_id.order_id.id, self.sale_line_id.order_id.name, self.product_id.name)
            task.message_post(body=task_msg)

        return task
