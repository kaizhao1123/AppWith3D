# -*- mode: python ; coding: utf-8 -*-


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