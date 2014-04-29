Welcome to django-bootstrap-span!
=================================

Abstract
--------

  This library applies class="spanN" CSS modifiers to a django-bootstrap form's fields.

  These spanN in bootstrap classes control how wide a form field is rendered in the view.

  This library uses the maximum field widths gleaned from the underlying form or model
  to know how to set the class span attribute. Thus you do not need to repeat your field max length settings - 
  in line with Django's DRY principle - and each field is rendered across in the horizontal direction.

Installing
----------

Install **django-bootstrap-span** with
``pip install django-bootstrap-span``.

Requires django-bootstrap (includes Twitter bootstrap v2.0).

Usage
-----

Install in your forms template .html file, as a form filter::

    {% load bootstrap_span %}
    {{ form|apply_bootstrap_span:""| as_bootstrap }}

    By default the filter apply_bootstrap_span applies to each field, up to 
    12 (default) spans depending each fields discovered maximum field width 
    using the default of 5 characters per span.
    
    You can change 
    - the maximum number of spans to allocate or 
    - the characters per span 
    in each form. If I wanted a maximum of 11 spans and 3 characters field width per span, I would use ::

    {{ form|apply_bootstrap_span:"11,3"| as_bootstrap }}

Full Form Template Example
--------------------------

Here is a fuller example using 11 spans and 6 characters per span::

        {% load bootstrap_toolkit %}
        
        <form method="post" action="." enctype="multipart/form-data">
        {% csrf_token %}
        {% load bootstrap_form_span %}
        {{ form|apply_bootstrap_span:"11,5"|as_bootstrap }}
        
        <input type="submit" class="btn" value="{% trans 'OK' %}" />
        
        </form>
