#!/usr/bin/env python
# -*- coding: utf-8 -*-

import main
import webtest


def test_get():
    app = webtest.TestApp(main.app)

    response1 = app.get('/?from=Field+of+Flying+Elephans&to=Nowhere?') #getting normal route 
    response2 = app.get('/?from=Field+of+Flying+Elephants&to=Nowhere&check=true') #outrages

    assert response1.status_int == 200
    assert response1.body.contains('Field of Flying Elephants --> Mount Jub-Jub --> White Manor --> Nowhere -->')

#outrage between White Manor and Mount Jub-Jub
    assert response2.status_int == 200
    assert response2.body.contains('Field of Flying Elephants --> Mount Jub-Jub --> Cacus Race Grounds --> Pool of Tears --> March Manor --> Tulgey Wood --> Guarded Way --> Looking-Glass House --> Living Flower Maze --> City of Charity --> Woods of No Name --> Nowhere -->')
