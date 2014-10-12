"""
Morevars plugin for Pelican
===========================

This plugin add variables to all context (Common variables) for debug purpose

remeber to keep this plugin as last of the pluginlist in your pelican config file

    PLUGINS = [
    ...
        'morevars'
    ]

put into your template some lines

    <h2>{{ morevars_version }}</h2>
    <pre>
    {{ morevars_debug }}
    </pre>

"""

from pelican import signals
from pprint import pformat
import os

def add_morevars(generator, metadata):
    # aggiunge le variabili all'oggetto del context,
    # es.: article.morevars_debug
    if 'morevars_debug' not in metadata:
        metadata[u"morevars_debug"] = pformat(metadata).replace('<','&lt;').replace('>','&gt;')


def install_addition_template_function(generator):
    #MORE VARIABLES
    if 'morevars_version' not in generator.env.globals:
        generator.env.globals["morevars_version"] = u'1.0.0'

    if 'morevars_debug' not in generator.env.globals:
        generator.env.globals["morevars_debug"] = \
            pformat({ 'generator.env.globals' : generator.env.globals,
                      'generator.env.filters' : generator.env.filters,
                      'generator.env.extensions' : generator.env.extensions,
                      'generator.context' : generator.context,
                   }).replace('<','&lt;').replace('>','&gt;')

def register():
    signals.generator_init.connect(install_addition_template_function)
    signals.article_generator_context.connect(add_morevars)
    signals.page_generator_context.connect(add_morevars)
    signals.static_generator_context.connect(add_morevars)
