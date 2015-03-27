# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427492425.232706
_enable_loop = True
_template_filename = 'C:\\Users\\Bruce\\Desktop\\IS 413\\chef-masterspr3\\chef-master\\events\\templates/area_user.html'
_template_uri = 'area_user.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['paper_elements_import', 'tab_title', 'meta_tags', 'content', 'page_title', 'extra_links']


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
        areas = context.get('areas', UNDEFINED)
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        def extra_links():
            return render_extra_links(context._locals(__M_locals))
        def meta_tags():
            return render_meta_tags(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def paper_elements_import():
            return render_paper_elements_import(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        event = context.get('event', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'meta_tags'):
            context['self'].meta_tags(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'paper_elements_import'):
            context['self'].paper_elements_import(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_links'):
            context['self'].extra_links(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_paper_elements_import(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def paper_elements_import():
            return render_paper_elements_import(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-input/paper-input.html">\r\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-button/paper-button.html">\r\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-checkbox/paper-checkbox.html">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        event = context.get('event', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  Areas for ')
        __M_writer(str( event.name ))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta_tags(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def meta_tags():
            return render_meta_tags(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<meta content="This page is for guest users to view the areas that are located at specific events" name="description">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        areas = context.get('areas', UNDEFINED)
        def content():
            return render_content(context)
        def page_title():
            return render_page_title(context)
        event = context.get('event', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t\r\n')
        __M_writer('\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\t<div class="row">\r\n\t\t\r\n')
        __M_writer('\t\t<div class="col-md-6">\r\n\r\n')
        __M_writer('\t\t\t<h3>Batch Options</h3>\r\n\t\t\t\r\n\t\t\t<div class="dropdown">\r\n\t\t\t\t<button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropwdown" aria-expanded="true">\r\n\t\t\t\t\tBatch Options\r\n\t\t\t\t\t<span class="caret"></span>\r\n\t\t\t\t</button>\r\n\t\t\t\t<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">\r\n\t\t\t\t\t<li role="presentation">Delete</li>\r\n\t\t\t\t</ul>\r\n\t\t\t</div>\r\n\r\n\t\t\t<paper-button class="success_button run_batch" raised>Submit</paper-button>\r\n\r\n')
        __M_writer('\r\n\t\t</div>\r\n')
        __M_writer('\r\n')
        __M_writer('\t\t<div class="col-md-6">\r\n\t\t\t\r\n')
        __M_writer('\t\t\t<h3>Filter Options</h3>\r\n\t\t\t\r\n\t\t\t<div class="dropdown">\r\n\t\t\t\t<button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropwdown" aria-expanded="true">\r\n\t\t\t\t\tFilter Options\r\n\t\t\t\t\t<span class="caret"></span>\r\n\t\t\t\t</button>\r\n\t\t\t\t<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">\r\n\t\t\t\t\t<li role="presentation">Delete</li>\r\n\t\t\t\t</ul>\r\n\t\t\t</div>\r\n\r\n\t\t\t<paper-input-decorator class="short" floatingLabel label="Criteria">\r\n\t\t\t\t<input is="core-input"></input>\r\n\t\t\t</paper-input-decorator>\r\n\r\n\t\t\t<paper-button class="success_button apply_filter" raised>Submit</paper-button>\r\n')
        __M_writer('\r\n\t\t</div>\r\n')
        __M_writer('\r\n\t</div>\r\n')
        __M_writer('\r\n')
        __M_writer('\t<hr>\r\n')
        __M_writer('\t<div id="left_column">\r\n\t\t<h2>Name</h2>\r\n\r\n')
        for area in areas:
            __M_writer('\r\n\t\t<div id="spacer">\r\n\t\t\t')
            __M_writer(str( area.name ))
            __M_writer('\r\n\t\t\t<div id="spacer1">\r\n\t\t\t\tProducts for Sale:\r\n\t\t\t</div>\r\n\t\t</div>\r\n')
        __M_writer('\r\n\r\n\r\n\t</div>\r\n\r\n\t<div id="right_column">\r\n\t\t<h2>Place Number</h2>\r\n\r\n')
        for area in areas:
            __M_writer('\r\n\t\t<div id="spacer">\r\n\t\t\t')
            __M_writer(str( area.place_number ))
            __M_writer('\r\n\t\t</div>\r\n')
        __M_writer('\t</div>\r\n\r\n')
        __M_writer('\t<div class="spacer"></div>\r\n\t<div class="spacer"></div>\r\n\t<div class="spacer"></div>\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        event = context.get('event', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t<div class="row">\r\n\t\t\t\r\n')
        __M_writer('\t\t\t<div class="col-md-8">\r\n\t\t\t\t<h1>Areas for ')
        __M_writer(str( event.name ))
        __M_writer('</h1>\r\n\t\t\t</div>\r\n')
        __M_writer('\r\n')
        __M_writer('\t\t\t<div class="col-md-4">\r\n\t\t\t\t<div class="create_button">\r\n\t\t\t\t\t<a class="button" href="/events/areas.create/')
        __M_writer(str( event.id ))
        __M_writer('">\r\n\t\t\t\t\t\t<paper-button class="create_button" raised>Create new Area</paper-button>\r\n\t\t\t\t\t</a>\r\n\t\t\t\t</div>\r\n\t\t\t\t\r\n\t\t\t</div>\r\n')
        __M_writer('\r\n\t\t</div>\r\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def extra_links():
            return render_extra_links(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_admin/styles/View.css">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Bruce\\Desktop\\IS 413\\chef-masterspr3\\chef-master\\events\\templates/area_user.html", "line_map": {"134": 29, "135": 32, "140": 53, "141": 55, "142": 57, "143": 60, "144": 63, "145": 78, "146": 81, "147": 83, "148": 86, "149": 104, "150": 107, "151": 110, "152": 112, "153": 114, "154": 117, "27": 0, "156": 120, "157": 120, "158": 126, "159": 134, "160": 135, "161": 137, "162": 137, "155": 118, "164": 143, "165": 147, "171": 32, "47": 7, "48": 9, "178": 32, "179": 36, "180": 37, "53": 13, "182": 40, "183": 42, "184": 44, "185": 44, "58": 17, "63": 23, "192": 25, "181": 37, "68": 27, "199": 25, "200": 26, "201": 26, "78": 19, "207": 201, "163": 140, "85": 19, "86": 20, "87": 20, "88": 21, "89": 21, "90": 22, "91": 22, "186": 51, "97": 11, "104": 11, "105": 12, "106": 12, "112": 15, "118": 15, "124": 29}, "uri": "area_user.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
