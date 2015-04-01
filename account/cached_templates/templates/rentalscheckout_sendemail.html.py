# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427926514.270052
_enable_loop = True
_template_filename = 'C:\\Users\\Bruce\\Desktop\\winter semester 2015\\IS 413\\chef-masterspr3\\chef-master\\account\\templates/rentalscheckout_sendemail.html'
_template_uri = 'rentalscheckout_sendemail.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
    return runtime._inherit_from(context, '/base_app/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
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
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t<table class="table table-hover table-bordered" >\r\n\t\t<thead>\r\n\t\t\t<tr>\r\n\t\t\t\t<th>\r\n\t\t\t\t\tquality\r\n\t\t\t\t</th>\r\n\t\t\t\t<th>\r\n\t\t\t\t\thello\r\n\t\t\t\t</th>\r\n\t\t\t\t<th>\r\n\t\t\t\t\tname\r\n\t\t\t\t</th>\r\n\t\t\t</tr>\r\n\t\t</thead>\r\n\t\t<tbody>\r\n\t\t\t<tr>\r\n\t\t\t\t<td>\r\n\t\t\t\t\tBruce\r\n\t\t\t\t</td>\r\n\t\t\t\t<td>\r\n\t\t\t\tDErik\r\n\t\t\t\t</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t\tJohn\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n\r\n\t\t</tbody>\r\n\r\n\t</table>\r\n\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Bruce\\Desktop\\winter semester 2015\\IS 413\\chef-masterspr3\\chef-master\\account\\templates/rentalscheckout_sendemail.html", "source_encoding": "ascii", "line_map": {"51": 11, "34": 7, "35": 9, "57": 51, "27": 0, "45": 11}, "uri": "rentalscheckout_sendemail.html"}
__M_END_METADATA
"""
