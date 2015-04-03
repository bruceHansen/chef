# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428021895.585363
_enable_loop = True
_template_filename = 'C:\\Users\\Bruce\\Desktop\\winter semester 2015\\IS 413\\chef-masterspr3\\chef-master\\reports\\templates/Report.html'
_template_uri = 'Report.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['view_table', 'tab_title', 'page_title_h1']


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
        def view_table():
            return render_view_table(context._locals(__M_locals))
        thirty = context.get('thirty', UNDEFINED)
        def page_title_h1():
            return render_page_title_h1(context._locals(__M_locals))
        report_name = context.get('report_name', UNDEFINED)
        ninety_plus = context.get('ninety_plus', UNDEFINED)
        sixty = context.get('sixty', UNDEFINED)
        ninety = context.get('ninety', UNDEFINED)
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title_h1'):
            context['self'].page_title_h1(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'view_table'):
            context['self'].view_table(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_view_table(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        sixty = context.get('sixty', UNDEFINED)
        def view_table():
            return render_view_table(context)
        ninety = context.get('ninety', UNDEFINED)
        thirty = context.get('thirty', UNDEFINED)
        ninety_plus = context.get('ninety_plus', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t\n')
        __M_writer('\t<div class="table-responsive">\n\t\t<table class="table table-hover table-bordered">\n\t\t\t<thead>\n\t\t\t\t<tr>\n\t\t\t\t\t<th>\n\t\t\t\t\t\t\n\t\t\t\t\t</th>\n\t\t\t\t\t<th>\n\t\t\t\t\t\tItem Name\n\t\t\t\t\t</th>\n\t\t\t\t\t<th>\n\t\t\t\t\t\tCustomer\n\t\t\t\t\t</th>\n\t\t\t\t\t<th>\n\t\t\t\t\t\tDue Date\n\t\t\t\t\t</th>\n\t\t\t\t\t<th>\n\t\t\t\t\t\tDays Overdue\n\t\t\t\t\t</th>\n\t\t\t\t</tr>\n\t\t\t</thead>\n\t\t\t<tbody>\n')
        for item in thirty:
            __M_writer('\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<paper-checkbox></paper-checkbox>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.item.specs.name ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.transaction.customer.get_full_name() ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.due_date.strftime('%b %d, %Y') ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t30\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>\n')
        for item in sixty:
            __M_writer('\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<paper-checkbox></paper-checkbox>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.item.specs.name ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.transaction.customer.get_full_name() ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.due_date.strftime('%b %d, %Y') ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t60\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>\n')
        for item in ninety:
            __M_writer('\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<paper-checkbox></paper-checkbox>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.item.specs.name ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.transaction.customer.get_full_name() ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.due_date.strftime('%b %d, %Y') ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t90\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>\n')
        for item in ninety_plus:
            __M_writer('\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<paper-checkbox></paper-checkbox>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.item.specs.name ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.transaction.customer.get_full_name() ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.due_date.strftime('%b %d, %Y') ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t90+\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>\n')
        __M_writer('\t\t\t</tbody>\n\t\t</table>\t\n\t</div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        report_name = context.get('report_name', UNDEFINED)
        def tab_title():
            return render_tab_title(context)
        __M_writer = context.writer()
        __M_writer('\n  ')
        __M_writer(str( report_name ))
        __M_writer(' Report\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title_h1(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        report_name = context.get('report_name', UNDEFINED)
        def page_title_h1():
            return render_page_title_h1(context)
        __M_writer = context.writer()
        __M_writer('\n\t<h1>')
        __M_writer(str( report_name ))
        __M_writer(' Report</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"130": 15, "137": 15, "138": 16, "139": 16, "145": 139, "27": 0, "43": 7, "44": 9, "49": 13, "54": 17, "64": 19, "74": 19, "75": 22, "76": 44, "77": 45, "78": 50, "79": 50, "80": 53, "81": 53, "82": 56, "83": 56, "84": 63, "85": 64, "86": 69, "87": 69, "88": 72, "89": 72, "90": 75, "91": 75, "92": 82, "93": 83, "94": 88, "95": 88, "96": 91, "97": 91, "98": 94, "99": 94, "100": 101, "101": 102, "102": 107, "103": 107, "104": 110, "105": 110, "106": 113, "107": 113, "108": 120, "109": 124, "115": 11, "122": 11, "123": 12, "124": 12}, "filename": "C:\\Users\\Bruce\\Desktop\\winter semester 2015\\IS 413\\chef-masterspr3\\chef-master\\reports\\templates/Report.html", "source_encoding": "ascii", "uri": "Report.html"}
__M_END_METADATA
"""
