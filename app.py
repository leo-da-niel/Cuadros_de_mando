streamlit.errors.StreamlitDuplicateElementId: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).

Traceback:
File "/mount/src/cuadros_de_mando/app.py", line 55, in <module>
    st.plotly_chart(fig)
File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/metrics_util.py", line 410, in wrapped_func
    result = non_optional_func(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/elements/plotly_chart.py", line 509, in plotly_chart
    plotly_chart_proto.id = compute_and_register_element_id(
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/elements/lib/utils.py", line 225, in compute_and_register_element_id
    _register_element_id(ctx, element_type, element_id)
File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/elements/lib/utils.py", line 131, in _register_element_id
    raise StreamlitDuplicateElementId(element_type)
