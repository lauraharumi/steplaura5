#!/usr/bin/env python
# -*- coding: utf-8 -*-

import main
import webtest


def test_get():
    app = webtest.TestApp(step-hello.app)

    response = app.get('/step-hello?a=cat&b=dog')

    assert response.status_int == 200
    assert response.content_type == 'text/html'
    assert response.body.contains('cdaotg')
