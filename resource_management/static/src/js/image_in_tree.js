odoo.define('web.WebTreeImage', function (require) {
    "use strict";
    var core = require('web.core');
    var session = require('web.session');
    var QWeb = core.qweb;
    var list_widget_registry = core.list_widget_registry;

    var WebTreeImage = list_widget_registry.get('field.binary').extend({
        format: function (line, options) {
            if (!line[this.id] || !line[this.id].value) {
                return '';
            }
            var value = line[this.id].value, src;
            if (this.type === 'binary') {
                if (value && value.substr(0, 10).indexOf(' ') === -1) {
                    src = "data:image/png;base64," + value;
                } else {
                    var imgArgs = {
                        model: options.model,
                        field: this.id,
                        id: options.id
                    }
                    if (this.resize) {
                        imgArgs.resize = this.resize;
                    }
                    src = session.url('/web/binary/image', imgArgs);
                }
            } else {
                if (!/\//.test(line[this.id].value)) {
                    src = '/web/static/src/img/icons/' + line[this.id].value + '.png';
                } else {
                    src = line[this.id].value;
                }
            }
            return QWeb.render('ListView.row.image', {widget: this, src: src});
        }
    });

    list_widget_registry.add('field.image', WebTreeImage)
});
