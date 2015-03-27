# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427488844.604113
_enable_loop = True
_template_filename = 'C:\\Users\\Bruce\\Desktop\\IS 413\\chef-masterspr3\\chef-master\\events\\templates/festival_event.html'
_template_uri = 'festival_event.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['extra_links', 'tab_title', 'page_title', 'paper_elements_import', 'meta_tags', 'content']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def paper_elements_import():
            return render_paper_elements_import(context._locals(__M_locals))
        def meta_tags():
            return render_meta_tags(context._locals(__M_locals))
        def extra_links():
            return render_extra_links(context._locals(__M_locals))
        events = context.get('events', UNDEFINED)
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'paper_elements_import'):
            context['self'].paper_elements_import(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_links'):
            context['self'].extra_links(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'meta_tags'):
            context['self'].meta_tags(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

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


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n  Festival Events\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t<div class="row">\r\n\t\t\t\r\n')
        __M_writer('\t\t\t<div class="col-md-8">\r\n\t\t\t\t<h1>Scheduled Events</h1>\r\n\t\t\t</div>\r\n')
        __M_writer('\r\n')
        __M_writer('\t\t\t<div class="col-md-4">\r\n\t\t\t\t\r\n\t\t\t</div>\r\n')
        __M_writer('\r\n\t\t</div>\r\n\t')
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


def render_meta_tags(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def meta_tags():
            return render_meta_tags(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<meta content="This is the festival events page" name="description">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        events = context.get('events', UNDEFINED)
        def page_title():
            return render_page_title(context)
        def content():
            return render_content(context)
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
        __M_writer('\r\n')
        __M_writer('\t<table class="table table-hover table-bordered">\r\n\t\t<thead>\r\n\t\t\t<tr>\r\n\t\t\t\t<th>\r\n\t\t\t\t\t<paper-button raised class="">Select All</paper-button>\r\n\t\t\t\t</th>\r\n\t\t\t\t<th>\r\n\t\t\t\t\tName\r\n\t\t\t\t</th>\r\n\t\t\t\t<th>\r\n\t\t\t\t\tStart Date\r\n\t\t\t\t</th>\r\n\t\t\t\t<th>\r\n\t\t\t\t\tVenue\r\n\t\t\t\t</th>\r\n\t\t\t\t<th>\r\n\t\t\t\t\tActions\r\n\t\t\t\t</th>\r\n\t\t\t</tr>\r\n\t\t</thead>\r\n\t\t<tbody>\r\n')
        for event in events:
            __M_writer('\t\t\t\t<tr>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<paper-checkbox></paper-checkbox>\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t')
            __M_writer(str( event.name ))
            __M_writer('\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t')
            __M_writer(str( event.start_date.strftime("%B %d, %Y") ))
            __M_writer('\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t')
            __M_writer(str( event.venue.name ))
            __M_writer('\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<a class="button" href="/events/areas.area_user/')
            __M_writer(str( event.id ))
            __M_writer('">\r\n\t\t\t\t\t\t\t<paper-button raised class="success_button">Areas</paper-button>\r\n\t\t\t\t\t\t</a>\r\n\t\t\t\t\t</td>\r\n\t\t\t\t</tr>\r\n')
        __M_writer('\t\t</tbody>\r\n\t</table>\t\r\n')
        __M_writer('\r\n')
        __M_writer('\t<div class="spacer"></div>\r\n\t<div class="spacer"></div>\r\n\t<div class="spacer"></div>\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "festival_event.html", "line_map": {"128": 16, "129": 16, "130": 17, "131": 17, "132": 18, "133": 18, "47": 9, "139": 25, "145": 25, "174": 81, "151": 29, "27": 0, "160": 29, "161": 32, "180": 111, "166": 48, "167": 50, "168": 52, "169": 55, "170": 58, "171": 73, "172": 76, "173": 78, "46": 7, "175": 99, "176": 102, "177": 105, "178": 107, "179": 109, "52": 13, "181": 132, "182": 133, "183": 138, "184": 138, "57": 19, "186": 141, "187": 144, "188": 144, "189": 147, "62": 23, "191": 153, "192": 156, "193": 158, "194": 162, "67": 27, "200": 194, "77": 21, "84": 21, "85": 22, "86": 22, "185": 141, "92": 11, "98": 11, "104": 32, "110": 32, "111": 36, "112": 40, "113": 42, "114": 46, "190": 147, "120": 15, "127": 15}, "source_encoding": "ascii", "filename": "C:\\Users\\Bruce\\Desktop\\IS 413\\chef-masterspr3\\chef-master\\events\\templates/festival_event.html"}
__M_END_METADATA
"""
