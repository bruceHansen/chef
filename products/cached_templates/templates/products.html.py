# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427839578.488216
_enable_loop = True
_template_filename = 'C:\\Users\\Bruce\\Desktop\\winter semester 2015\\IS 413\\chef-masterspr3\\chef-master\\products\\templates/products.html'
_template_uri = 'products.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'tab_title', 'page_title']


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
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        s_items = context.get('s_items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        bulk_items = context.get('bulk_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        def page_title():
            return render_page_title(context)
        bulk_items = context.get('bulk_items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        s_items = context.get('s_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t\n')
        __M_writer('\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\t<h3 class="table_title">Bulk Items</h3>\n')
        __M_writer('\n')
        for item in bulk_items:
            __M_writer('\n\t\t<div class="item_box">\n\n')
            __M_writer('\t\t\t<a href="/products/products.details/')
            __M_writer(str( item.id ))
            __M_writer('"><h4>')
            __M_writer(str( item.specs.name ))
            __M_writer('</h4></a>\n')
            __M_writer('\n\t\t\t<div class="spacer"></div>\n\t\t\t<div class="spacer"></div>\n\t\t\t<div class="spacer"></div>\n\t\t\t\n')
            __M_writer('\t\t\t<a href="/products/products.details/')
            __M_writer(str( item.id ))
            __M_writer('"><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer(str( item.specs.photograph.image ))
            __M_writer('" class="product_image"/></a>\n')
            __M_writer('\n\t\t</div>\n\n')
        __M_writer('\n')
        __M_writer('\t<div class="clearfix"></div>\n')
        __M_writer('\n')
        __M_writer('\t<hr>\n')
        __M_writer('\n')
        __M_writer('\t<h3 class="table_title clearfix">Individualized Items</h3>\n')
        __M_writer('\n')
        for item in s_items:
            __M_writer('\n\t\t<div class="item_box">\n\n')
            __M_writer('\t\t\t<a href="/products/products.details/')
            __M_writer(str( item.id ))
            __M_writer('"><h4>')
            __M_writer(str( item.specs.name ))
            __M_writer('</h4></a>\n')
            __M_writer('\n\t\t\t<div class="spacer"></div>\n\t\t\t<div class="spacer"></div>\n\t\t\t<div class="spacer"></div>\n\t\t\t\n')
            __M_writer('\t\t\t<a href="/products/products.details/')
            __M_writer(str( item.id ))
            __M_writer('"><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer(str( item.specs.photograph.image ))
            __M_writer('" class="product_image"/></a>\n')
            __M_writer('\n\t\t</div>\n\n')
        __M_writer('\n')
        __M_writer('\t<div class="clearfix"></div>\n')
        __M_writer('\n')
        __M_writer('\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        __M_writer = context.writer()
        __M_writer('\n  Products\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t<div class="row">\n\t\t\t\n')
        __M_writer('\t\t\t<div class="col-md-8">\n\t\t\t\t<h1>View Items</h1>\n\t\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<div class="col-md-4">\n\t\t\t\t<paper-button class="create_button search_button" raised>Search</paper-button>\n\t\t\t</div>\n')
        __M_writer('\n\t\t</div>\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"131": 11, "137": 18, "143": 18, "144": 22, "145": 26, "146": 28, "147": 32, "153": 147, "27": 0, "41": 7, "42": 9, "47": 13, "57": 15, "68": 15, "69": 18, "74": 34, "75": 36, "76": 38, "77": 40, "78": 42, "79": 43, "80": 47, "81": 47, "82": 47, "83": 47, "84": 47, "85": 49, "86": 55, "87": 55, "88": 55, "89": 55, "90": 55, "91": 55, "92": 57, "93": 62, "94": 64, "95": 66, "96": 68, "97": 70, "98": 72, "99": 74, "100": 76, "101": 77, "102": 81, "103": 81, "104": 81, "105": 81, "106": 81, "107": 83, "108": 89, "109": 89, "110": 89, "111": 89, "112": 89, "113": 89, "114": 91, "115": 96, "116": 98, "117": 100, "118": 102, "119": 106, "125": 11}, "filename": "C:\\Users\\Bruce\\Desktop\\winter semester 2015\\IS 413\\chef-masterspr3\\chef-master\\products\\templates/products.html", "uri": "products.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
