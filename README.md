Morevars plugin for Pelican
===========================

This plugin add variables to all context (Common variables) for debug purpose.

Remeber to keep this plugin as last of the pluginlist in your pelican config file

    PLUGINS = [
    ...
        'morevars'
    ]

put into your template some lines

    <h2>{{ morevars_version }}</h2>
    <pre>
    {{ morevars_debug }}
    </pre>

you also have

    {{ article.morevars_debug }}

and so on.
