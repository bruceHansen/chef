# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427910464.028844
_enable_loop = True
_template_filename = 'C:\\Users\\Bruce\\Desktop\\winter semester 2015\\IS 413\\chef-masterspr3\\chef-master\\rentals\\templates/rental_return.html'
_template_uri = 'rental_return.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['tab_title', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base_admin/templates/View.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        r_items = context.get('r_items', UNDEFINED)
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n  \tRental Return\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        r_items = context.get('r_items', UNDEFINED)
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t\r\n\t\r\n\t\t<table class="table table-hover table-bordered">\r\n\t\t\t<thead>\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th>\r\n\t\t\t\t\t\tName\r\n\t\t\t\t\t</th>\r\n\t\t\t\t\t<th>\r\n\t\t\t\t\t\tDue Date\r\n\t\t\t\t\t</th>\r\n\t\t\t\t\t<th>\r\n\t\t\t\t\t\tImage\r\n\t\t\t\t\t</th>\r\n\t\t\t\t\t<th>\r\n\t\t\t\t\t\tActions\r\n\t\t\t\t\t</th>\r\n\t\t\t\t</tr>\r\n\t\t\t</thead>\r\n\r\n\t\t\t<tbody>\r\n')
        for r_item in r_items:
            __M_writer('\t\t\t\t<tr>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t')
            __M_writer(str( r_item.item.specs.name ))
            __M_writer('\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t')
            __M_writer(str( r_item.due_date ))
            __M_writer('\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<img id="image_field" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer(str( r_item.item.specs.photograph.image ))
            __M_writer('" >\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<a class="button" href="/rentals/rentals.item_return/')
            __M_writer(str( r_item.item_id ))
            __M_writer('/')
            __M_writer(str( r_item.id ))
            __M_writer('">\r\n\t\t\t\t\t\t\t<paper-button raised class="edit_button">Return</paper-button>\r\n\t\t\t\t\t\t</a>\r\n\t\t\t\t\t</td>\r\n')
        __M_writer('\t\t\t\t</tr>\r\n\t\t\t</tbody>\r\n\t\t\t\r\n\t\t</table>\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "rental_return.html", "filename": "C:\\Users\\Bruce\\Desktop\\winter semester 2015\\IS 413\\chef-masterspr3\\chef-master\\rentals\\templates/rental_return.html", "line_map": {"66": 15, "74": 15, "75": 37, "76": 38, "77": 40, "78": 40, "79": 43, "80": 43, "81": 46, "82": 46, "83": 46, "84": 49, "85": 49, "86": 49, "87": 49, "88": 54, "27": 0, "94": 88, "38": 7, "39": 9, "44": 13, "54": 11, "60": 11}, "source_encoding": "ascii"}
__M_END_METADATA
"""
