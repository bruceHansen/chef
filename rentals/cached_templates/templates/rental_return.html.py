# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428034366.707738
_enable_loop = True
_template_filename = 'C:\\Users\\Bruce\\Desktop\\winter semester 2015\\IS 413\\chef-masterspr3\\chef-master\\rentals\\templates/rental_return.html'
_template_uri = 'rental_return.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'tab_title']


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
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
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


"""
__M_BEGIN_METADATA
{"line_map": {"64": 38, "65": 40, "66": 40, "67": 43, "68": 43, "69": 46, "70": 46, "71": 46, "72": 49, "73": 49, "74": 49, "75": 49, "76": 54, "82": 11, "88": 11, "27": 0, "94": 88, "38": 7, "39": 9, "44": 13, "54": 15, "62": 15, "63": 37}, "source_encoding": "ascii", "uri": "rental_return.html", "filename": "C:\\Users\\Bruce\\Desktop\\winter semester 2015\\IS 413\\chef-masterspr3\\chef-master\\rentals\\templates/rental_return.html"}
__M_END_METADATA
"""
