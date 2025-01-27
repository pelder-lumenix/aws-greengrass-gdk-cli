import gdk.commands.component.project_utils as project_utils
import gdk.common.consts as consts
import gdk.common.utils as utils


def test_get_static_file_path_supported_builds():
    # Integ test for the existence of supported build file even before building the cli tool.
    model_file_path = utils.get_static_file_path(consts.project_build_system_file)
    assert model_file_path is not None
    assert model_file_path.exists()


def test_get_supported_component_builds():
    # Integ test for the correctly parsing the  supported builds json file as dict
    supported_component_builds = project_utils.get_supported_component_builds()
    if supported_component_builds:
        assert type(supported_component_builds) == dict
        assert len(supported_component_builds) > 0
        for k, v in supported_component_builds.items():
            assert "build_folder" in v
            assert "build_command" in v
            assert type(v) == dict
