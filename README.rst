Welcome to django-bootstrap-span!
=================================

Abstract
--------

This library applies class="spanN" CSS modifiers to a form's fields. 
In conjunction with a bootstrap CSS, these "spanN"  class definitions control how wide a form field is rendered in the HTML.
Expected use is with django-bootstrap application.

This library uses the maximum field widths gleaned from the underlying form or model
to know how to correctly calculate the size of the class span attribute. Thus you do not need to repeat the field max length settings - 
in line with Django's DRY principle - as each field is HTML rendered correctly in the horizontal direction.

Installing
----------

Install **django-bootstrap-span** with
``pip install django-bootstrap-span``.

Requires django-bootstrap (includes Twitter bootstrap v2.0).

Usage
-----

Install the boostrap_span application in your settings file::

    INSTALLED_APPS = (
     ...
        'bootstrap_toolkit',
        'bootstrap_span',
     ...
     )

Install ``apply_bootstrap_span`` form filter in each of your forms template *.html files::

    {% load bootstrap_span %}
    {{ form|apply_bootstrap_span:""| as_bootstrap }}

By default the filter apply_bootstrap_span looks at each field in the form, and decides how many 
spans (span1 to span12) to assign to it.

Up to 12 spans (the default) can be assigned  - calculated depending each fields discovered maximum character width. 

As a span is an arbitrary division of horizontal screen real estate - an adjustment is applied to go from the 
maximum characters width of a fields to get to the number of spans.

This is done using the parameter called characters per span -which has a default value of 5.
    
You can change 
- the maximum number of spans to allocate (in case you are in a part of the HTML which is span-limited) or 
- the characters per span 
in each form. 

If I wanted to render form's fields with a maximum of 11 spans and 3 characters width per span, I would use::

    {{ form|apply_bootstrap_span:"11,3"| as_bootstrap }}

Fuller Example
--------------------------

Here is a fuller example using 11 spans and 6 characters per span::

        {% load bootstrap_toolkit %}
        
        <form method="post" action="." enctype="multipart/form-data">
        {% csrf_token %}
        {% load bootstrap_form_span %}
        {{ form|apply_bootstrap_span:"11,5"|as_bootstrap }}
        
        <input type="submit" class="btn" value="{% trans 'OK' %}" />
        
        </form>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`