# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428201920.167706
_enable_loop = True
_template_filename = 'C:\\Users\\Bruce\\Desktop\\winter semester 2015\\IS 413\\chef-masterspr3\\chef-master\\reports\\templates/Report.html'
_template_uri = 'Report.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['view_table', 'page_title', 'tab_title', 'page_title_h1']


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
        ninety_plus = context.get('ninety_plus', UNDEFINED)
        ninety = context.get('ninety', UNDEFINED)
        def view_table():
            return render_view_table(context._locals(__M_locals))
        def page_title_h1():
            return render_page_title_h1(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        sixty = context.get('sixty', UNDEFINED)
        report_name = context.get('report_name', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title_h1'):
            context['self'].page_title_h1(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'view_table'):
            context['self'].view_table(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_view_table(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        ninety_plus = context.get('ninety_plus', UNDEFINED)
        ninety = context.get('ninety', UNDEFINED)
        def view_table():
            return render_view_table(context)
        sixty = context.get('sixty', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        __M_writer('\t<div class="table-responsive">\n\t\t<table class="table table-hover table-bordered">\n\t\t\t<thead>\n\t\t\t\t<tr>\n\t\t\t\t\t<th>\n\t\t\t\t\t\t\n\t\t\t\t\t</th>\n\t\t\t\t\t<th>\n\t\t\t\t\t\tItem Name\n\t\t\t\t\t</th>\n\t\t\t\t\t<th>\n\t\t\t\t\t\tCustomer\n\t\t\t\t\t</th>\n\t\t\t\t\t<th>\n\t\t\t\t\t\tDue Date\n\t\t\t\t\t</th>\n\t\t\t\t\t<th>\n\t\t\t\t\t\tDays Overdue\n\t\t\t\t\t</th>\n\t\t\t\t</tr>\n\t\t\t</thead>\n\t\t\t<tbody>\n')
        for item in sixty:
            __M_writer('\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<paper-checkbox></paper-checkbox>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.item.specs.name ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.transaction.customer.get_full_name() ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.due_date.strftime('%b %d, %Y') ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t30 - 60 days overdue\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>\n')
        for item in ninety:
            __M_writer('\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<paper-checkbox></paper-checkbox>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.item.specs.name ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.transaction.customer.get_full_name() ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.due_date.strftime('%b %d, %Y') ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t60 - 90 days overdue\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>\n')
        for item in ninety_plus:
            __M_writer('\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<paper-checkbox></paper-checkbox>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.item.specs.name ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.transaction.customer.get_full_name() ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.due_date.strftime('%b %d, %Y') ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\tMore than 90 days overdue\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>\n')
        __M_writer('\t\t\t</tbody>\n\t\t</table>\t\n\t</div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('\n\t<a href="/reports/rentals.email_overdue">\n\t\t<paper-button class="create_button search_button" raised>Send Overdue Emails</paper-button>\n\t</a>\n')
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
{"line_map": {"131": 11, "132": 12, "133": 12, "139": 15, "146": 15, "147": 16, "148": 16, "154": 148, "27": 0, "44": 7, "45": 9, "50": 13, "55": 17, "60": 23, "70": 25, "79": 25, "80": 29, "81": 51, "82": 52, "83": 57, "84": 57, "85": 60, "86": 60, "87": 63, "88": 63, "89": 70, "90": 71, "91": 76, "92": 76, "93": 79, "94": 79, "95": 82, "96": 82, "97": 89, "98": 90, "99": 95, "100": 95, "101": 98, "102": 98, "103": 101, "104": 101, "105": 108, "106": 112, "112": 19, "118": 19, "124": 11}, "filename": "C:\\Users\\Bruce\\Desktop\\winter semester 2015\\IS 413\\chef-masterspr3\\chef-master\\reports\\templates/Report.html", "source_encoding": "ascii", "uri": "Report.html"}
__M_END_METADATA
"""
