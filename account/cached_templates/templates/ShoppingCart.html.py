# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427928138.971317
_enable_loop = True
_template_filename = 'C:\\Users\\Bruce\\Desktop\\winter semester 2015\\IS 413\\chef-masterspr3\\chef-master\\account\\templates/ShoppingCart.html'
_template_uri = 'ShoppingCart.html'
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
        items = context.get('items', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        str = context.get('str', UNDEFINED)
        int = context.get('int', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        items = context.get('items', UNDEFINED)
        def content():
            return render_content(context)
        str = context.get('str', UNDEFINED)
        int = context.get('int', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\t<div class="full-width-container">\n\t\t\n')
        __M_writer('\t\t<div class="row">\n\t\t\t\n')
        __M_writer('\t\t\t<div class="table-responsive">\n\t\t\t\t<table class="table table-hover table-bordered">\n\t\t\t\t\t<thead>\n\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t<th>\n\t\t\t\t\t\t\t\tType\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t<th>\n\t\t\t\t\t\t\t\tProduct\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t<th class="quantity">\n\t\t\t\t\t\t\t\tQuantity\t\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t<th class="price">\n\t\t\t\t\t\t\t\tPrice\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t<th>\n\t\t\t\t\t\t\t\tActions\t\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t</tr>\n\t\t\t\t\t</thead>\n\t\t\t\t\t<tbody>\n\t\t\t\t\t\t')
        total = 0 
        
        __M_writer('\n')
        for item in items:
            __M_writer('\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t\t\t')
            __M_writer(str( item.specs.name ))
            __M_writer('\n\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t\t<td class="quantity">\n\t\t\t\t\t\t\t\t\t')
            __M_writer(str( items[item] ))
            __M_writer('\n\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t\t<td class="price">\n\t\t\t\t\t\t\t\t\t')
            __M_writer(str( item.specs.price * int(items[item]) ))
            __M_writer('\n\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t\t\t<paper-button raised data-id="')
            __M_writer(str( item.id ))
            __M_writer('" class="delete_button">Remove</paper-button>\n\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t')
            total += (item.specs.price * items[item]) 
            
            __M_writer('\n')
        __M_writer('\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t<th>\n\t\t\t\t\t\t\t\tTotal Price\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t<th>\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t<th class="total_price">\n\t\t\t\t\t\t\t\t')
        __M_writer(str( total ))
        __M_writer('\n\t\t\t\t\t\t\t\t')
        request.session['total'] = {} 
        
        __M_writer('\n\t\t\t\t\t\t\t\t')
        request.session['total'] = str(total) 
        
        __M_writer('\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t</tr>\n\t\t\t\t\t</tbody>\n\t\t\t\t</table>\n\t\t\t</div>\n')
        __M_writer('\n\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t<div class="row">\n\t\t\t\n\t\t\t<div class="check_button_cont">\n\t\t\t\t\n\t\t\t\t<a class="button" href="/account/ShoppingCart.checkout/')
        __M_writer(str( total ))
        __M_writer('">\n\t\t\t\t\t<paper-button raised class="create_button" id="checkout_button">Check Out</paper-button>\n\t\t\t\t</a>\n\n\t\t\t</div>\n\n\t\t</div>\n')
        __M_writer('\n\t</div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Bruce\\Desktop\\winter semester 2015\\IS 413\\chef-masterspr3\\chef-master\\account\\templates/ShoppingCart.html", "uri": "ShoppingCart.html", "line_map": {"65": 42, "66": 43, "67": 44, "68": 49, "69": 49, "70": 52, "71": 52, "72": 55, "73": 55, "74": 58, "75": 58, "76": 61, "78": 61, "79": 63, "80": 71, "81": 71, "82": 72, "84": 72, "85": 73, "87": 73, "88": 80, "89": 83, "90": 85, "27": 0, "92": 89, "93": 97, "94": 100, "91": 89, "100": 94, "38": 7, "39": 9, "49": 11, "59": 11, "60": 14, "61": 17, "62": 20, "63": 42}, "source_encoding": "ascii"}
__M_END_METADATA
"""
