odoo.define('resource_management.resource_availability', function (require){
    "use strict";

    var core = require('web.core');
    var data = require('web.data');
    var ActionManager = require('web.ActionManager');
    var form_common = require('web.form_common');
    var time = require('web.time');
    var Model = require('web.DataModel');
    var _t = core._t;
    var QWeb = core.qweb;

    var ResourceAvailable = form_common.FormWidget.extend(form_common.ReinitializeWidgetMixin, {
        display_name: _t('Form'),
        view_type: "form",
        init: function() {
            this._super.apply(this, arguments);
            if(this.field_manager.model == "resource.availability") {
                $(".oe_view_manager_buttons").hide();
                $(".oe_view_manager_header").hide();
            }
            this.set({
                date_to: false,
                date_from: false,
                resource_header: false,
                resource_info: false,
                resource_header_date: false,
                resource_header_day: false,
            });
            this.resource_header = [];
            this.resource_info = [];
            this.resource_header_date = [];
            this.resource_header_day = [];
            this.field_manager.on("field_changed:date_from", this, function() {
                this.set({"date_from": time.str_to_date(this.field_manager.get_field_value("date_from"))});
            });
            this.field_manager.on("field_changed:date_to", this, function() {
                this.set({"date_to": time.str_to_date(this.field_manager.get_field_value("date_to"))});
            });
            this.field_manager.on("field_changed:resource_header", this, function() {
                this.set({"resource_header": this.field_manager.get_field_value("resource_header")});
            });
            this.field_manager.on("field_changed:resource_info", this, function() {
                this.set({"resource_info":this.field_manager.get_field_value("resource_info")});
            });
            this.field_manager.on("field_changed:resource_header_date", this, function() {
                this.set({"resource_header_date":this.field_manager.get_field_value("resource_header_date")});
            });
            this.field_manager.on("field_changed:resource_header_day", this, function() {
                this.set({"resource_header_day":this.field_manager.get_field_value("resource_header_day")});
            });
        },
        initialize_field: function() {
            form_common.ReinitializeWidgetMixin.initialize_field.call(this);
            var self = this;
            self.on("change:resource_header", self, self.initialize_content);
            self.on("change:resource_info", self, self.initialize_content);
            self.on("change:resource_header_date", self, self.initialize_content);
            self.on("change:resource_header_day", self, self.initialize_content);
        },
        initialize_content: function() {
           var self = this;
           if (self.setting) {
               return;
           }
           
           if (!this.resource_header || !this.resource_info || !this.resource_header_date || !this.resource_header_day) {
                  return;
            }
           // don't render anything until we have resource_header and resource_info
                  
           this.destroy_content();
           if (this.get("resource_header")) {
                this.resource_header = py.eval(this.get("resource_header"));
           }
           if (this.get("resource_info")) {
               this.resource_info = py.eval(this.get("resource_info"));
           }
           if(this.get("resource_header_date")){
              this.resource_header_date = py.eval(this.get("resource_header_date"));
           }
           if(this.get("resource_header_day")){
              this.resource_header_day = py.eval(this.get("resource_header_day"));
           }
           this.renderElement();
           this.view_loading();
           this.view_free();
           this.view_leave();
           this.load_date();
        },

        view_loading: function(r) {
            return this.load_occupied(r);
        },

        view_free: function(r) {
            return this.load_free(r);
        },

        view_leave: function(r) {
            return this.load_leave(r);
        },

        load_date: function(data) {
            self.action_manager = new ActionManager(self);
            this.$el.find(".table_header_date").bind("click", function(event){
                self.action_manager.do_action({
                        type: 'ir.actions.act_window',
                        res_model: "schedule.report",
                        views: [[false, 'form']],
                        context: {'click_date': event.currentTarget.dataset.date},
                        target: 'new',
                });
            });
        },
                
        load_occupied: function(data) {
            self.action_manager = new ActionManager(self);
            this.$el.find(".resource_occupied").bind("click", function(event){
                self.action_manager.do_action({
                        type: 'ir.actions.act_window',
                        res_model: "task.schedule",
                        views: [[false, 'form']],
                        context: {'click_date': this.dataset.date},
                        res_id: parseInt(event.currentTarget.dataset.id),
                        target: 'new',
                });
            });
        },

        load_free: function(data) {
            self.action_manager = new ActionManager(self);
            this.$el.find(".resource_free").bind("click", function(event){
                self.action_manager.do_action({
                        type: 'ir.actions.act_window',
                        res_model: "summary.report",
                        views: [[false, 'form']],
                        context: {'click_date': this.dataset.date},
                        target: 'new',
                });
            });
        },

        load_leave: function(data) {
            self.action_manager = new ActionManager(self);
            this.$el.find(".resource_leave").bind("click", function(event){
                self.action_manager.do_action({
                        type: 'ir.actions.act_window',
                        res_model: "summary.report",
                        views: [[false, 'form']],
                        context: {'click_date': this.dataset.date},
                        res_id: parseInt(event.currentTarget.dataset.id),
                        target: 'new',
                });
            });
        },

        renderElement: function() {
            this.destroy_content();
            this.$el.html(QWeb.render("resourceDetails", {widget: this}));
        }
    });
    core.form_custom_registry.add('Resource_Availability', ResourceAvailable);
});