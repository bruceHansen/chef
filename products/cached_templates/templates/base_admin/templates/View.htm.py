# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425700996.079437
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/base_admin/templates/View.htm'
_template_uri = '/base_admin/templates/View.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'page_title', 'tab_title', 'top_left_column', 'top_right_column', 'paper_elements_import', 'create_button_block', 'view_table', 'page_title_h1']


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
    return runtime._inherit_from(context, '/base_admin/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        def view_table():
            return render_view_table(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def page_title_h1():
            return render_page_title_h1(context._locals(__M_locals))
        def top_left_column():
            return render_top_left_column(context._locals(__M_locals))
        def paper_elements_import():
            return render_paper_elements_import(context._locals(__M_locals))
        def create_button_block():
            return render_create_button_block(context._locals(__M_locals))
        def top_right_column():
            return render_top_right_column(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'paper_elements_import'):
            context['self'].paper_elements_import(**pageargs)
        

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
        def page_title_h1():
            return render_page_title_h1(context)
        def top_left_column():
            return render_top_left_column(context)
        def view_table():
            return render_view_table(context)
        def create_button_block():
            return render_create_button_block(context)
        def top_right_column():
            return render_top_right_column(context)
        __M_writer = context.writer()
        __M_writer('\n\t\n')
        __M_writer('\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\t<div class="row">\n\t\t\n')
        __M_writer('\t\t<div class="col-md-6">\n\n\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_left_column'):
            context['self'].top_left_column(**pageargs)
        

        __M_writer('\n\n\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t<div class="col-md-6">\n\n\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_right_column'):
            context['self'].top_right_column(**pageargs)
        

        __M_writer('\n\n\t\t</div>\n')
        __M_writer('\n\t</div>\n')
        __M_writer('\n')
        __M_writer('\t<hr>\n')
        __M_writer('\n')
        __M_writer('\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'view_table'):
            context['self'].view_table(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        def page_title_h1():
            return render_page_title_h1(context)
        def create_button_block():
            return render_create_button_block(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t<div class="row">\n\t\t\t\n')
        __M_writer('\t\t\t<div class="col-md-8">\n\n\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title_h1'):
            context['self'].page_title_h1(**pageargs)
        

        __M_writer('\n\t\t\t\t\n\t\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<div class="col-md-4">\n\t\t\t\t<div class="create_button">\n\n\t\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'create_button_block'):
            context['self'].create_button_block(**pageargs)
        

        __M_writer('\n\t\t\t\t\t\n\t\t\t\t</div>\n\t\t\t\t\n\t\t\t</div>\n')
        __M_writer('\n\t\t</div>\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        __M_writer = context.writer()
        __M_writer('\n  View\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_left_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_left_column():
            return render_top_left_column(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t\t  \t\n')
        __M_writer('\t\t\t\t<h3>Batch Options</h3>\n\t\t\t\t\n\t\t\t\t<div class="dropdown">\n\t\t\t\t\t<button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropwdown" aria-expanded="true">\n\t\t\t\t\t\tBatch Options\n\t\t\t\t\t\t<span class="caret"></span>\n\t\t\t\t\t</button>\n\t\t\t\t\t<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">\n\t\t\t\t\t\t<li role="presentation">Delete</li>\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\n\t\t\t\t<paper-button class="success_button run_batch" raised>Submit</paper-button>\n')
        __M_writer('\n\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_right_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_right_column():
            return render_top_right_column(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t  \t\n')
        __M_writer('\t\t\t\t<h3>Filter Options</h3>\n\t\t\t\t\n\t\t\t\t<div class="dropdown">\n\t\t\t\t\t<button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropwdown" aria-expanded="true">\n\t\t\t\t\t\tFilter Options\n\t\t\t\t\t\t<span class="caret"></span>\n\t\t\t\t\t</button>\n\t\t\t\t\t<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">\n\t\t\t\t\t\t<li role="presentation">Delete</li>\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\n\t\t\t\t<paper-input-decorator class="short" floatingLabel label="Criteria">\n\t\t\t\t\t<input is="core-input"></input>\n\t\t\t\t</paper-input-decorator>\n\n\t\t\t\t<paper-button class="success_button apply_filter" raised>Submit</paper-button>\n')
        __M_writer('\n\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_paper_elements_import(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def paper_elements_import():
            return render_paper_elements_import(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-input/paper-input.html">\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-button/paper-button.html">\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-checkbox/paper-checkbox.html">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_create_button_block(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def create_button_block():
            return render_create_button_block(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t\t\t\t  \n\t\t\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_view_table(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def view_table():
            return render_view_table(context)
        __M_writer = context.writer()
        __M_writer('\n\t  \n\t\t\t\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title_h1(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title_h1():
            return render_page_title_h1(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t\t\t  \tView\n\t\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/John/DevProjects/Repositories/chef/base_admin/templates/View.htm", "uri": "/base_admin/templates/View.htm", "line_map": {"51": 19, "130": 36, "243": 42, "140": 36, "141": 40, "146": 44, "147": 48, "148": 50, "153": 55, "154": 61, "27": 0, "52": 21, "160": 23, "219": 53, "166": 23, "172": 72, "200": 27, "178": 72, "179": 75, "180": 89, "57": 25, "186": 98, "62": 31, "192": 98, "193": 101, "194": 119, "225": 53, "72": 33, "207": 27, "208": 28, "209": 28, "210": 29, "211": 29, "212": 30, "213": 30, "249": 42, "90": 33, "91": 36, "96": 63, "97": 65, "98": 67, "99": 70, "231": 133, "104": 90, "105": 94, "106": 96, "237": 133, "111": 120, "112": 124, "113": 127, "114": 129, "115": 131, "116": 133, "121": 136, "122": 138, "123": 140, "124": 144, "255": 249}}
__M_END_METADATA
"""
