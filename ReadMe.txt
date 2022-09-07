https://marknsc0501.medium.com/%E4%BD%BF%E7%94%A8pyinstaller%E5%B0%81%E8%A3%9Dpyqt5-mayavi%E6%87%89%E7%94%A8%E7%A8%8B%E5%BC%8F-b01564c719d2

1. how to package to app using 'pyinstaller'?
	pyinstaller -F -w *.py

************************************************************************
2. packages
	xlrd		2.0.1
	xlutils		2.0.0
	PyQt5		5.9.2
	numpy		1.21.6
	pip		22.1.2
	opencv-python	4.5.5.64
	pyserial	3.5
	scipy		1.2.3
	pillow		9.1.1
	matplotlib	3.5.2	
	pyinstaller 	5.1
	mayavi		4.7.1	
	matplotlib	4.5.2	

	(need to downgrade the version of the following packages)
	apptools==4.5.0
	envisage==4.9.2
	pyface==6.1.2
	traits==6.0.0
	traitsui==6.1.3
	vtk==8.1.2
	
*************************************************************************
3. for spec file:
	pyinstaller *.spec

import os
import pkg_resources
block_cipher = None
hook_ep_packages = dict()
hiddenimports = set()
# List of packages that should have there Distutils entrypoints included.
ep_packages = ["traitsui.toolkits", "pyface.toolkits", "tvtk.toolkits"]
if ep_packages:
    for ep_package in ep_packages:
        for ep in pkg_resources.iter_entry_points(ep_package):
            if ep_package in hook_ep_packages:
                package_entry_point = hook_ep_packages[ep_package]
            else:
                package_entry_point = []
                hook_ep_packages[ep_package] = package_entry_point
            package_entry_point.append("{} = {}:{}".format(
                ep.name, ep.module_name, ep.attrs[0]))
            hiddenimports.add(ep.module_name)
    try:
        os.mkdir('./generated')
    except FileExistsError:
        pass
with open("./generated/pkg_resources_hook.py", "w") as f:
        f.write("""# Runtime hook generated from spec file to support pkg_resources entrypoints.
ep_packages = {}
if ep_packages:
    import pkg_resources
    default_iter_entry_points = pkg_resources.iter_entry_points
def hook_iter_entry_points(group, name=None):
        if group in ep_packages and ep_packages[group]:
            eps = ep_packages[group]
            for ep in eps:
                parsedEp = pkg_resources.EntryPoint.parse(ep)
                parsedEp.dist = pkg_resources.Distribution()
                yield parsedEp
        else:
            return default_iter_entry_points(group, name)
pkg_resources.iter_entry_points = hook_iter_entry_points
""".format(hook_ep_packages))
morehiddenimport = ['pyface.ui.qt4.about_dialog', 'pyface.ui.qt4.application_window', 'pyface.ui.qt4.beep', 'pyface.ui.qt4.clipboard', 'pyface.ui.qt4.confirmation_dialog', 'pyface.ui.qt4.dialog', 'pyface.ui.qt4.directory_dialog', 'pyface.ui.qt4.file_dialog', 'pyface.ui.qt4.gui', 'pyface.ui.qt4.heading_text', 'pyface.ui.qt4.image_cache', 'pyface.ui.qt4.image_resource', 'pyface.ui.qt4.init', 'pyface.ui.qt4.message_dialog', 'pyface.ui.qt4.mimedata', 'pyface.ui.qt4.progress_dialog', 'pyface.ui.qt4.python_editor', 'pyface.ui.qt4.python_shell', 'pyface.ui.qt4.resource_manager', 'pyface.ui.qt4.single_choice_dialog', 'pyface.ui.qt4.splash_screen', 'pyface.ui.qt4.split_widget', 'pyface.ui.qt4.system_metrics', 'pyface.ui.qt4.widget', 'pyface.ui.qt4.window', 'pyface.ui.qt4.__init__', 'pyface.ui.qt4.action.action_item', 'pyface.ui.qt4.action.menu_bar_manager', 'pyface.ui.qt4.action.menu_manager', 'pyface.ui.qt4.action.status_bar_manager', 'pyface.ui.qt4.action.tool_bar_manager', 'pyface.ui.qt4.action.__init__', 'pyface.ui.qt4.code_editor.code_widget', 'pyface.ui.qt4.code_editor.find_widget', 'pyface.ui.qt4.code_editor.gutters', 'pyface.ui.qt4.code_editor.pygments_highlighter', 'pyface.ui.qt4.code_editor.replace_widget', 'pyface.ui.qt4.code_editor.__init__', 'pyface.ui.qt4.code_editor.tests.test_code_widget', 'pyface.ui.qt4.code_editor.tests.__init__', 'pyface.ui.qt4.console.api', 'pyface.ui.qt4.console.bracket_matcher', 'pyface.ui.qt4.console.call_tip_widget', 'pyface.ui.qt4.console.completion_lexer', 'pyface.ui.qt4.console.console_widget', 'pyface.ui.qt4.console.history_console_widget', 'pyface.ui.qt4.console.__init__', 'pyface.ui.qt4.fields.combo_field',
                    'pyface.ui.qt4.fields.field', 'pyface.ui.qt4.fields.spin_field', 'pyface.ui.qt4.fields.text_field', 'pyface.ui.qt4.fields.__init__', 'pyface.ui.qt4.tasks.advanced_editor_area_pane', 'pyface.ui.qt4.tasks.dock_pane', 'pyface.ui.qt4.tasks.editor', 'pyface.ui.qt4.tasks.editor_area_pane', 'pyface.ui.qt4.tasks.main_window_layout', 'pyface.ui.qt4.tasks.split_editor_area_pane', 'pyface.ui.qt4.tasks.task_pane', 'pyface.ui.qt4.tasks.task_window_backend', 'pyface.ui.qt4.tasks.util', 'pyface.ui.qt4.tasks.__init__', 'pyface.ui.qt4.tasks.tests.test_split_editor_area_pane', 'pyface.ui.qt4.tasks.tests.__init__', 'pyface.ui.qt4.tests.bad_import', 'pyface.ui.qt4.tests.test_gui', 'pyface.ui.qt4.tests.test_mimedata', 'pyface.ui.qt4.tests.test_progress_dialog', 'pyface.ui.qt4.tests.test_qt_imports', 'pyface.ui.qt4.tests.__init__', 'pyface.ui.qt4.timer.do_later', 'pyface.ui.qt4.timer.timer', 'pyface.ui.qt4.timer.__init__', 'pyface.ui.qt4.util.event_loop_helper', 'pyface.ui.qt4.util.gui_test_assistant', 'pyface.ui.qt4.util.modal_dialog_tester', 'pyface.ui.qt4.util.testing', 'pyface.ui.qt4.util.__init__', 'pyface.ui.qt4.util.tests.test_gui_test_assistant', 'pyface.ui.qt4.util.tests.test_modal_dialog_tester', 'pyface.ui.qt4.util.tests.__init__', 'pyface.ui.qt4.wizard.wizard', 'pyface.ui.qt4.wizard.wizard_page', 'pyface.ui.qt4.wizard.__init__', 'pyface.ui.qt4.workbench.editor', 'pyface.ui.qt4.workbench.split_tab_widget', 'pyface.ui.qt4.workbench.view', 'pyface.ui.qt4.workbench.workbench_window_layout', 'pyface.ui.qt4.workbench.__init__', 'pyface.ui.qt4.workbench.tests.test_workbench_window_layout', 'pyface.ui.qt4.workbench.tests.__init__', 'pyface.ui.qt4.expandable_panel']
                    
a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=list(hiddenimports)+morehiddenimport,
             hookspath=[],
             runtime_hooks=["./generated/pkg_resources_hook.py"],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='newRecon',
          strip=False,
          debug=False,
          upx=False,
          console=False,
          windowed=True)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='newRecon')
**********************************************************************
5. update pyface/api
	
# ----------------------------------------------------------------------------
# Legacy and Wx-specific imports.
# ----------------------------------------------------------------------------

# These widgets currently only have Wx implementations
# will return Unimplemented for Qt.

# from .expandable_panel import ExpandablePanel
# from .image_widget import ImageWidget
# from .layered_panel import LayeredPanel
# from .mdi_application_window import MDIApplicationWindow
# from .mdi_window_menu import MDIWindowMenu
# from .multi_toolbar_window import MultiToolbarWindow
#
# # This code isn't toolkit widget code, but is wx-specific
# from traits.etsconfig.api import ETSConfig
# if ETSConfig.toolkit == 'wx':
#
#     # Fix for broken Pycrust introspect module.
#     # XXX move this somewhere better? - CJW 2017
#     from .util import fix_introspect_bug
#
# del ETSConfig

import os
os.environ['QT_API'] = 'pyqt5'
os.environ['ETS_TOOLKIT'] = 'qt4'
from traits.etsconfig.api import ETSConfig
ETSConfig.toolkit = 'qt4'
*******************************************************************************

6. update pyface/base_toolkit
	
  plugins = list(pkg_resources.iter_entry_points(entry_point, toolkit_name))
    if len(plugins) == 0:
        msg = 'No {} plugin found for toolkit {}'
        msg = msg.format(entry_point, toolkit_name)
        logger.debug(msg)
        raise RuntimeError(msg)
    elif len(plugins) > 1:
        msg = ("multiple %r plugins found for toolkit %r: %s")
        modules = ', '.join(plugin.module_name for plugin in plugins)
        logger.warning(msg, entry_point, toolkit_name, modules)

    if entry_point in ('traitsui.toolkits'):	####
        return plugins[1].load()	####
    if entry_point in ('pyface.toolkits'):	####
        return plugins[2].load()	####
    if entry_point in ('tvtk.toolkits'):	####
        return plugins[1].load()	####

    for plugin in plugins:
        try:
            toolkit_object = plugin.load()
            return toolkit_object
        except (ImportError, AttributeError) as exc:
            msg = "Could not load plugin %r from %r"
            logger.info(msg, plugin.name, plugin.module_name)
            logger.debug(exc, exc_info=True)

    msg = 'No {} plugin could be loaded for {}'
    msg = msg.format(entry_point, toolkit_name)
    logger.info(msg)
    raise RuntimeError(msg)
**********************************************************************

7. cope mayavi, tvtk and result.xls to dist/newRecon/
**************************************
 