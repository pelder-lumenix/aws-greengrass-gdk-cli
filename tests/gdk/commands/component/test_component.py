from gdk.commands.component import component


def test_component_init(mocker):
    mock_component_init = mocker.patch("gdk.commands.component.init.run", return_value=None)
    d_args = {"init": None}
    component.init(d_args)
    assert mock_component_init.call_count == 1
    mock_component_init.assert_called_with(d_args)


def test_component_build(mocker):
    mock_component_build = mocker.patch("gdk.commands.component.build.run", return_value=None)
    d_args = {"init": None}
    component.build(d_args)
    assert mock_component_build.call_count == 1
    mock_component_build.assert_called_with(d_args)


def test_component_publish(mocker):
    mocker.patch("gdk.commands.component.project_utils.get_service_clients", return_value=None)
    mocker.patch("gdk.commands.component.project_utils.get_project_config_values", return_value={"region": "None"})
    mock_component_publish = mocker.patch("gdk.commands.component.publish.run", return_value=None)
    d_args = {"init": None}
    component.publish(d_args)
    assert mock_component_publish.call_count == 1
    mock_component_publish.assert_called_with(d_args)


def test_component_list(mocker):
    mock_component_list = mocker.patch("gdk.commands.component.list.run", return_value=None)
    d_args = {"list": None}
    component.list(d_args)
    assert mock_component_list.call_count == 1
    mock_component_list.assert_called_with(d_args)
