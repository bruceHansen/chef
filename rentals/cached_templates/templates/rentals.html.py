# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427846535.953405
_enable_loop = True
_template_filename = 'C:\\Users\\Bruce\\Desktop\\winter semester 2015\\IS 413\\chef-masterspr3\\chef-master\\rentals\\templates/rentals.html'
_template_uri = 'rentals.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        non_wardrobe = context.get('non_wardrobe', UNDEFINED)
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        wardrobe = context.get('wardrobe', UNDEFINED)
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        non_wardrobe = context.get('non_wardrobe', UNDEFINED)
        def page_title():
            return render_page_title(context)
        wardrobe = context.get('wardrobe', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t\n')
        __M_writer('\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\t<h3 class="table_title">Non Wardrobe Items</h3>\n')
        __M_writer('\n')
        for item in non_wardrobe:
            __M_writer('\n\t\t<div class="item_box">\n\n')
            __M_writer('\t\t\t<a href="/rentals/rentals.details/')
            __M_writer(str( item.id ))
            __M_writer('"><h4>')
            __M_writer(str( item.specs.name ))
            __M_writer('</h4></a>\n')
            __M_writer('\n\t\t\t<div class="spacer"></div>\n\t\t\t\n')
            __M_writer('\t\t\t<a href="/rentals/rentals.details/')
            __M_writer(str( item.id ))
            __M_writer('"><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer(str( item.specs.photograph.image ))
            __M_writer('" class="rental_image"/></a>\n')
            __M_writer('\n\t\t</div>\n\n')
        __M_writer('\n')
        __M_writer('\t<div class="clearfix"></div>\n')
        __M_writer('\n')
        __M_writer('\t<hr>\n')
        __M_writer('\n')
        __M_writer('\t<h3 class="table_title clearfix">Wardrobe Items</h3>\n')
        __M_writer('\n')
        for item in wardrobe:
            __M_writer('\n\t\t<div class="item_box">\n\n')
            __M_writer('\t\t\t<a href="/rentals/rentals.details/')
            __M_writer(str( item.id ))
            __M_writer('"><h4>')
            __M_writer(str( item.specs.name ))
            __M_writer('</h4></a>\n')
            __M_writer('\n\t\t\t<div class="spacer"></div>\n\t\t\t\n')
            __M_writer('\t\t\t<a href="/rentals/rentals.details/')
            __M_writer(str( item.id ))
            __M_writer('"><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer(str( item.specs.photograph.image ))
            __M_writer('" class="rental_image"/></a>\n')
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
        __M_writer('\n  \tRentals\n')
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
        __M_writer('\t\t\t<div class="col-md-8">\n\t\t\t\t<h1>View Rentals Available</h1>\n\t\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<div class="col-md-4">\n\t\t\t\t<paper-button class="create_button search_button" raised>Search</paper-button>\n\t\t\t\t<a href="/rentals/rentals.rental_return">\n\t\t\t\t\t<paper-button class="create_button search_button" raised>Return Rentals</paper-button>\n\t\t\t\t</a>\n\t\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\n\t\t\t\t\n\n')
        __M_writer('\n\t\t</div>\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"131": 11, "137": 18, "143": 18, "144": 22, "145": 26, "146": 28, "147": 35, "148": 37, "149": 41, "27": 0, "155": 149, "41": 7, "42": 9, "47": 13, "57": 15, "68": 15, "69": 18, "74": 43, "75": 45, "76": 47, "77": 49, "78": 51, "79": 52, "80": 56, "81": 56, "82": 56, "83": 56, "84": 56, "85": 58, "86": 62, "87": 62, "88": 62, "89": 62, "90": 62, "91": 62, "92": 64, "93": 69, "94": 71, "95": 73, "96": 75, "97": 77, "98": 79, "99": 81, "100": 83, "101": 84, "102": 88, "103": 88, "104": 88, "105": 88, "106": 88, "107": 90, "108": 94, "109": 94, "110": 94, "111": 94, "112": 94, "113": 94, "114": 96, "115": 101, "116": 103, "117": 105, "118": 107, "119": 111, "125": 11}, "uri": "rentals.html", "filename": "C:\\Users\\Bruce\\Desktop\\winter semester 2015\\IS 413\\chef-masterspr3\\chef-master\\rentals\\templates/rentals.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
