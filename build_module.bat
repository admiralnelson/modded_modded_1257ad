@echo off
@del /Q /F /S  *.pyc
py -2  process_init.py
py -2  process_global_variables.py
py -2  process_strings.py
py -2  process_skills.py
py -2  process_music.py
py -2  process_animations.py
py -2  process_meshes.py
py -2  process_sounds.py
py -2  process_skins.py
py -2  process_map_icons.py
py -2  process_factions.py
py -2  process_items.py
py -2  process_scenes.py
py -2  process_troops.py
py -2  process_particle_sys.py
py -2  process_scene_props.py
py -2  process_tableau_materials.py
py -2  process_presentations.py
py -2  process_party_tmps.py
py -2  process_parties.py
py -2  process_quests.py
py -2  process_info_pages.py
py -2  process_scripts.py
py -2  process_mission_tmps.py
py -2  process_game_menus.py
py -2  process_simple_triggers.py
py -2  process_dialogs.py
py -2  process_global_variables_unused.py
py -2  process_postfx.py
@del /Q /F /S  *.pyc


cd module_data
py -2  flora_kinds.py
py -2  ground_specs.py
copy flora_kinds.txt E:\modded 1257 source\1257AD FROM SOURCE\etc\
copy ground_specs.txt E:\modded 1257 source\1257AD FROM SOURCE\etc\
cd ..

echo Script processing has ended.
echo.
echo ______________________________
echo.
rem BEEP:
echo 
echo Press any key to exit. . .
pause>nul
