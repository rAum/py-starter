def test_template_generation(cookies):
    pypkg_name = "test"
    result = cookies.bake(extra_context={"project_fullname": "Example Project" ,
                                         "python_package_name": "pypkg_name"})
    
    assert result.exit_code == 0
    assert result.exception is None