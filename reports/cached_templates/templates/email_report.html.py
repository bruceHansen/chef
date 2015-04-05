# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428198006.669877
_enable_loop = True
_template_filename = 'C:\\Users\\Bruce\\Desktop\\winter semester 2015\\IS 413\\chef-masterspr3\\chef-master\\reports\\templates/email_report.html'
_template_uri = 'email_report.html'
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
    return runtime._inherit_from(context, '/base_app/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        users = context.get('users', UNDEFINED)
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
        def content():
            return render_content(context)
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h1>Overdue Emails Sent</h1>\r\n\r\n')
        __M_writer('    <div class="table-responsive">\r\n        <table class="table table-hover table-bordered">\r\n            <thead>\r\n                <tr>\r\n                    <th>\r\n                        Sent to the following customers:\r\n                    </th>\r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n')
        for user in users:
            __M_writer('                    <tr>\r\n                        <td>\r\n                            ')
            __M_writer(str( user.first_name ))
            __M_writer(' ')
            __M_writer(str( user.last_name ))
            __M_writer('\r\n                        </td>\r\n                    </tr>\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n    </div>\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n  Overdue Email Report\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "email_report.html", "source_encoding": "ascii", "filename": "C:\\Users\\Bruce\\Desktop\\winter semester 2015\\IS 413\\chef-masterspr3\\chef-master\\reports\\templates/email_report.html", "line_map": {"64": 33, "65": 33, "66": 33, "67": 33, "68": 37, "37": 7, "38": 9, "43": 13, "81": 11, "75": 11, "53": 15, "69": 41, "87": 81, "27": 0, "60": 15, "61": 20, "62": 30, "63": 31}}
__M_END_METADATA
"""
