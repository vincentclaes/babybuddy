# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import plotly.offline as plotly
import plotly.graph_objs as go

from reports import utils


def weight_weight(objects):
    """
    Create a graph showing weight over time.
    :param objects: a QuerySet of Weight instances.
    :returns: a tuple of the the graph's html and javascript.
    """
    objects = objects.order_by('-date')

    trace = go.Scatter(
        name='Weight',
        x=list(objects.values_list('date', flat=True)),
        y=list(objects.values_list('weight', flat=True)),
        fill='tozeroy',
    )

    layout_args = utils.default_graph_layout_options()
    layout_args['barmode'] = 'stack'
    layout_args['title'] = '<b>Weight</b>'
    layout_args['xaxis']['title'] = 'Date'
    layout_args['xaxis']['rangeselector'] = utils.rangeselector_date()
    layout_args['yaxis']['title'] = 'Weight'

    fig = go.Figure({
        'data': [trace],
        'layout': go.Layout(**layout_args)
    })
    output = plotly.plot(fig, output_type='div', include_plotlyjs=False)
    return utils.split_graph_output(output)
