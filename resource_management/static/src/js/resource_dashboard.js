odoo.define('resource_management.dashboard', function (require) {
"use strict";
var core = require('web.core');
var formats = require('web.formats');
var Model = require('web.Model');
var session = require('web.session');
var KanbanView = require('web_kanban.KanbanView');

var QWeb = core.qweb;

var _t = core._t;
var _lt = core._lt;

var ResourceDashboardView = KanbanView.extend({
    display_name: _lt('Dashboard'),
    icon: 'fa-dashboard',
    searchview_hidden: true,
    events: {
        'click .o_dashboard_action': 'on_dashboard_action_clicked',
        'click .o_target_to_set': 'on_dashboard_target_clicked',
    },

    fetch_data: function() {
        return new Model('task.schedule')
            .call('retrieve_resource_dashboard', []);
    },
    render: function() {
        var super_render = this._super;
        var self = this;
        return this.fetch_data().then(function(result){
            self.show_demo = result && result.nb_opportunities === 0;
            self.show_demo = false

            var resource_dashboard = QWeb.render('resource_management.ResourceDashboard', {
                widget: self,
                show_demo: self.show_demo,
                values: result,
            });
            super_render.call(self);
            $(resource_dashboard).prependTo(self.$el);
        });
    },

    on_dashboard_action_clicked: function(ev){
        ev.preventDefault();
        var $action = $(ev.currentTarget);
        var action_name = $action.attr('name');
        var action_extra = $action.data('extra');
        var additional_context = {};

        // TODO: find a better way to add defaults to search view
        if (action_name === 'resource_management.task_schedule_action_dashboard') {
        } 
            if (action_extra === 'today_double_booked') {
                additional_context.search_default_today_double_booked = 1;
            } else if (action_extra === 'tomorrow_double_booked') {
                additional_context.search_default_tomorrow_double_booked = 1;
            } else if (action_extra === 'this_week_double_booked') {
                additional_context.search_default_this_week_double_booked = 1;
            } else if (action_extra === 'next_week_double_booked') {
                additional_context.search_default_next_week_double_booked = 1;
            } else if (action_extra === 'this_month_double_booked') {
                additional_context.search_default_this_month_double_booked = 1;
            } else if (action_extra === 'next_month_double_booked') {
                additional_context.search_default_next_month_double_booked = 1;
            } else if (action_extra === 'today_not_linked') {
                additional_context.search_default_today_not_linked = 1;
            } else if (action_extra === 'tomorrow_not_linked') {
                additional_context.search_default_tomorrow_not_linked = 1;
            } else if (action_extra === 'this_week_not_linked') {
                additional_context.search_default_this_week_not_linked = 1;
            } else if (action_extra === 'next_week_not_linked') {
                additional_context.search_default_next_week_not_linked = 1;
            } else if (action_extra === 'this_month_not_linked') {
                additional_context.search_default_this_month_not_linked = 1;
            } else if (action_extra === 'next_month_not_linked') {
                additional_context.search_default_next_month_not_linked = 1;
            } else if (action_extra === 'today_planned_hours') {
                additional_context.search_default_today_planned_hours = 1;
            } else if (action_extra === 'tomorrow_planned_hours') {
                additional_context.search_default_tomorrow_planned_hours = 1;
            } else if (action_extra === 'this_week_planned_hours') {
                additional_context.search_default_this_week_planned_hours = 1;
            } else if (action_extra === 'next_week_planned_hours') {
                additional_context.search_default_next_week_planned_hours = 1;
            } else if (action_extra === 'this_month_planned_hours') {
                additional_context.search_default_this_month_planned_hours = 1;
            } else if (action_extra === 'next_month_planned_hours') {
                additional_context.search_default_next_month_planned_hours = 1;
            } else if (action_extra === 'assigned_to_last_hour') {
                additional_context.search_default_last_hour_assigned_to = 1;
            } else if (action_extra === 'close_last_hour') {
                additional_context.search_default_last_hour_close = 1;
            } else if (action_extra === 'next_hour_deadline') {
                additional_context.search_default_deadline_next_hour = 1;
            } else if (action_extra === 'today_deadline') {
                additional_context.search_default_deadline_today = 1;
            } else if (action_extra === 'tomorrow_deadline') {
                additional_context.search_default_deadline_tomorrow = 1;
            } else if (action_extra === 'week_deadline') {
                additional_context.search_default_deadline_week = 1;
            } else if (action_extra === 'assigned_to') {
                additional_context.search_default_assigned_to = 1;
            } else if (action_extra === 'deadline') {
                additional_context.search_default_deadline = 1;
            } else if (action_extra === 'next_hour_to_assign') {
                additional_context.search_default_to_assign_next_hour = 1;
            } else if (action_extra === 'today_to_assign') {
                additional_context.search_default_to_assign_today = 1;
            } else if (action_extra === 'tomorrow_to_assign') {
                additional_context.search_default_to_assign_tomorrow = 1;
            } else if (action_extra === 'week_to_assign') {
                additional_context.search_default_to_assign_week = 1;
            }

        if (action_name === 'resource_management.project_task_action_dashboard'){
        }
            if (action_extra === 'today_planned_hours') {
                additional_context.search_default_today_planned_hours = 1;
            } else if (action_extra === 'tomorrow_planned_hours') {
                additional_context.search_default_tomorrow_planned_hours = 1;
            } else if (action_extra === 'this_week_planned_hours') {
                additional_context.search_default_this_week_planned_hours = 1;
            } else if (action_extra === 'next_week_planned_hours') {
                additional_context.search_default_next_week_planned_hours = 1;
            } else if (action_extra === 'this_month_planned_hours') {
                additional_context.search_default_this_month_planned_hours = 1;
            } else if (action_extra === 'next_month_planned_hours') {
                additional_context.search_default_next_month_planned_hours = 1;
            } else if (action_extra === 'yesterday_planned_hours') {
                additional_context.search_default_yesterday_planned_hours = 1;
            } else if (action_extra === 'last_week_planned_hours') {
                additional_context.search_default_last_week_planned_hours = 1;
            } else if (action_extra === 'last_month_planned_hours') {
                additional_context.search_default_last_month_planned_hours = 1;
            } else if (action_extra === 'today_scheduled_hours') {
                additional_context.search_default_today_scheduled_hours = 1;
            } else if (action_extra === 'tomorrow_scheduled_hours') {
                additional_context.search_default_tomorrow_scheduled_hours = 1;
            } else if (action_extra === 'this_week_scheduled_hours') {
                additional_context.search_default_this_week_scheduled_hours = 1;
            } else if (action_extra === 'next_week_scheduled_hours') {
                additional_context.search_default_next_week_scheduled_hours = 1;
            } else if (action_extra === 'this_month_scheduled_hours') {
                additional_context.search_default_this_month_scheduled_hours = 1;
            } else if (action_extra === 'next_month_scheduled_hours') {
                additional_context.search_default_next_month_scheduled_hours = 1;
            } else if (action_extra === 'yesterday_scheduled_hours') {
                additional_context.search_default_yesterday_scheduled_hours = 1;
            } else if (action_extra === 'last_week_scheduled_hours') {
                additional_context.search_default_last_week_scheduled_hours = 1;
            } else if (action_extra === 'last_month_scheduled_hours') {
                additional_context.search_default_last_month_scheduled_hours = 1;
            } else if (action_extra === 'today_task_needed') {
                additional_context.search_default_today_task_needed = 1;
            } else if (action_extra === 'tomorrow_task_needed') {
                additional_context.search_default_tomorrow_task_needed = 1;
            } else if (action_extra === 'this_week_task_needed') {
                additional_context.search_default_this_week_task_needed = 1;
            } else if (action_extra === 'next_week_task_needed') {
                additional_context.search_default_next_week_task_needed = 1;
            } else if (action_extra === 'this_month_task_needed') {
                additional_context.search_default_this_month_task_needed = 1;
            } else if (action_extra === 'next_month_task_needed') {
                additional_context.search_default_next_month_task_needed = 1;
            } else if (action_extra === 'today_task_overplanned') {
                additional_context.search_default_today_task_overplanned = 1;
            } else if (action_extra === 'tomorrow_task_overplanned') {
                additional_context.search_default_tomorrow_task_overplanned = 1;
            } else if (action_extra === 'this_week_task_overplanned') {
                additional_context.search_default_this_week_task_overplanned = 1;
            } else if (action_extra === 'next_week_task_overplanned') {
                additional_context.search_default_next_week_task_overplanned = 1;
            } else if (action_extra === 'this_month_task_overplanned') {
                additional_context.search_default_this_month_task_overplanned = 1;
            } else if (action_extra === 'next_month_task_overplanned') {
                additional_context.search_default_next_month_task_overplanned = 1;
            } else if (action_extra === 'next_week_realized_hours') {
                additional_context.search_default_next_week_realized_hours = 1;
            } else if (action_extra === 'this_month_realized_hours') {
                additional_context.search_default_this_month_realized_hours = 1;
            } else if (action_extra === 'next_month_realized_hours') {
                additional_context.search_default_next_month_realized_hours = 1;
            } else if (action_extra === 'yesterday_realized_hours') {
                additional_context.search_default_yesterday_realized_hours = 1;
            } else if (action_extra === 'last_week_realized_hours') {
                additional_context.search_default_last_week_realized_hours = 1;
            } else if (action_extra === 'last_month_realized_hours') {
                additional_context.search_default_last_month_realized_hours = 1;
            } else if (action_extra === 'new_task') {
                additional_context.search_default_new_task = 1;
            } else if (action_extra === 'task_no_team') {
               additional_context.search_default_task_no_team = 1;
            } else if (action_extra === 'task_overdue') {
               additional_context.search_default_task_overdue = 1;
            }

        if (action_name === 'resource_management.action_resource_resource_tree_dashboard'){
        }
            if (action_extra === 'today_resource_available') {
                additional_context.search_default_today_resource_available = 1;
            } else if (action_extra === 'tomorrow_resource_available') {
                additional_context.search_default_tomorrow_resource_available = 1;
            } else if (action_extra === 'this_week_resource_available') {
                additional_context.search_default_this_week_resource_available = 1;
            } else if (action_extra === 'next_week_resource_available') {
                additional_context.search_default_next_week_resource_available = 1;
            } else if (action_extra === 'this_month_resource_available') {
                additional_context.search_default_this_month_resource_available = 1;
            } else if (action_extra === 'next_month_resource_available') {
                additional_context.search_default_next_month_resource_available = 1;
            } else if (action_extra === 'today_resource_booked') {
                additional_context.search_default_today_resource_booked = 1;
            } else if (action_extra === 'tomorrow_resource_booked') {
                additional_context.search_default_tomorrow_resource_booked = 1;
            } else if (action_extra === 'this_week_resource_booked') {
                additional_context.search_default_this_week_resource_booked = 1;
            } else if (action_extra === 'next_week_resource_booked') {
                additional_context.search_default_next_week_resource_booked = 1;
            } else if (action_extra === 'this_month_resource_booked') {
                additional_context.search_default_this_month_resource_booked = 1;
            } else if (action_extra === 'next_month_resource_booked') {
                additional_context.search_default_next_month_resource_booked = 1;
            }
        this.do_action(action_name, {additional_context: additional_context});
        
    },

    on_change_input_target: function(e) {
        var self = this;
        var $input = $(e.target);
        var target_name = $input.attr('name');
        var target_value = $input.val();

        if(isNaN(target_value)) {
            this.do_warn(_t("Wrong value entered!"), _t("Only Integer Value should be valid."));
        } else {
            this._updated = new Model('crm.lead')
                            .call('modify_target_sales_dashboard', [target_name, parseInt(target_value)])
                            .then(function() {
                                return self.render();
                            });
        }
    },

    on_dashboard_target_clicked: function(ev){
        if (this.show_demo) {
            // The user is not allowed to modify the targets in demo mode
            return;
        }

        var self = this;
        var $target = $(ev.currentTarget);
        var target_name = $target.attr('name');
        var target_value = $target.attr('value');

        var $input = $('<input/>', {type: "text"});
        $input.attr('name', target_name);
        if (target_value) {
            $input.attr('value', target_value);
        }
        $input.on('keyup input', function(e) {
            if(e.which === $.ui.keyCode.ENTER) {
                self.on_change_input_target(e);
            }
        });
        $input.on('blur', function(e) {
            self.on_change_input_target(e);
        });

        $.when(this._updated).then(function() {
            $input.replaceAll(self.$('.o_target_to_set[name=' + target_name + ']')) // the target may have changed (re-rendering)
                  .focus()
                  .select();
        });
    },

    render_monetary_field: function(value, currency_id) {
        var currency = session.get_currency(currency_id);
        var digits_precision = currency && currency.digits;
        value = formats.format_value(value || 0, {type: "float", digits: digits_precision});
        if (currency) {
            if (currency.position === "after") {
                value += currency.symbol;
            } else {
                value = currency.symbol + value;
            }
        }
        return value;
    },
});

core.view_registry.add('resource_management', ResourceDashboardView);

return ResourceDashboardView;

});



