# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428199601.951022
_enable_loop = True
_template_filename = 'C:\\Users\\Bruce\\Desktop\\winter semester 2015\\IS 413\\chef-masterspr3\\chef-master\\rentals\\templates/return_item.html'
_template_uri = 'return_item.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['tab_title', 'content', 'page_title']


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
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        item = context.get('item', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
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
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  \tReturn: ')
        __M_writer(str( item.specs.name ))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        def page_title():
            return render_page_title(context)
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n')
        __M_writer('\r\n    <h3 class="text-left">Receiving Agent Only:</h3>\r\n\r\n    ')
        __M_writer(str( form ))
        __M_writer('\r\n\r\n')
        __M_writer('\t<div class="spacer"></div>\r\n\t<div class="spacer"></div>\r\n\t<div class="spacer"></div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t<div class="row">\r\n\t\t\t\r\n')
        __M_writer('\t\t\t<div class="col-md-8">\r\n\t\t\t\t<h1>Return: ')
        __M_writer(str( item.specs.name ))
        __M_writer('</h1>\r\n\t\t\t</div>\r\n')
        __M_writer('\r\n\t\t</div>\r\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 12, "65": 12, "71": 15, "81": 15, "82": 18, "87": 28, "88": 30, "89": 33, "90": 33, "91": 36, "97": 18, "27": 0, "40": 7, "41": 9, "106": 23, "107": 23, "108": 26, "46": 13, "104": 18, "114": 108, "105": 22, "56": 11, "63": 11}, "filename": "C:\\Users\\Bruce\\Desktop\\winter semester 2015\\IS 413\\chef-masterspr3\\chef-master\\rentals\\templates/return_item.html", "uri": "return_item.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
