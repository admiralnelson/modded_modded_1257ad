# -*- coding: utf-8 -*-

from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [
  ("bogus", "cant_find_this.ogg", 0, 0),
  ("mount_and_blade_title_screen", "mount_and_blade_title_screen.ogg", mtf_module_track|mtf_sit_main_title|mtf_start_immediately, 0),
  ("captured", "capture.ogg", mtf_module_track, 0),

  ("empty_village", "empty_village.ogg", mtf_module_track|mtf_persist_until_finished, 0),
  ("escape", "escape.ogg", mtf_module_track|mtf_persist_until_finished, 0),
  ("retreat", "retreat.ogg", mtf_module_track|mtf_persist_until_finished|mtf_sit_killed, 0),
  
  # modded2x begin:
  # Central eu
  ("Central0", "Werkraum_Slâfest_du_friedel_ziere.mp3", mtf_module_track|mtf_culture_central_eu|mtf_sit_travel,  mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_central_eu),
  ("Central1", "Ductia.mp3", mtf_module_track|mtf_culture_central_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_central_eu),
  ("Central2", "David_GayPerret_Redemption.ogg", mtf_module_track|mtf_culture_central_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_central_eu),
  ("Central3", "Castle_Dance.ogg", mtf_module_track|mtf_culture_central_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_central_eu),
  ("Central4", "Dove_in_the_Sky.ogg", mtf_module_track|mtf_culture_central_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_central_eu),
  ("Central5", "Echo_in_Eternity.ogg", mtf_module_track|mtf_culture_central_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_central_eu),
  ("Central6", "Prana_WORLD_Here_we_come.ogg", mtf_module_track|mtf_culture_central_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_central_eu),
  ("Central7", "PicturesPlay_Danza.ogg", mtf_module_track|mtf_culture_central_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_central_eu),
  ("Central8", "Ignacio_Núñez_Wings_of_glory.ogg", mtf_module_track|mtf_culture_central_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_central_eu),
  ("Central9", "Ignacio_Núñez_Mnemósine.ogg", mtf_module_track|mtf_culture_central_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_central_eu),
  ("Central10", "Bard_Tale.ogg", mtf_module_track|mtf_culture_central_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_central_eu),
  ("Central11", "Lost_Battle_New_Begining.ogg", mtf_module_track|mtf_culture_central_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_central_eu),
  ("Central12", "Handful_of_Sorrow.ogg", mtf_module_track|mtf_culture_central_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_central_eu),
  ("Central13", "travel_central_1.ogg", mtf_module_track|mtf_culture_central_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_central_eu),
  ("Central14", "travel_central_2.ogg", mtf_module_track|mtf_culture_central_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_central_eu),
  ("Central15", "Knights_Fall.ogg", mtf_module_track|mtf_culture_central_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_central_eu),
  ("Central16", "Where_my_Heart_is.ogg", mtf_module_track|mtf_culture_central_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_central_eu),
  ("Central17", "euro19_Medieval_II_Total_War.ogg", mtf_module_track|mtf_culture_central_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_central_eu),
  ("Central18", "Iska_Oldtown.ogg", mtf_module_track|mtf_culture_central_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_central_eu),

  # West eu
  ("West0", "travel_france_1.mp3", mtf_module_track|mtf_culture_west_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_west_eu),
  ("West1", "Ductia.mp3", mtf_module_track|mtf_culture_west_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_west_eu),
  ("West2", "David_GayPerret_Redemption.ogg", mtf_module_track|mtf_culture_west_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_west_eu),
  ("West3", "Castle_Dance.ogg", mtf_module_track|mtf_culture_west_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_west_eu),
  ("West4", "Dove_in_the_Sky.ogg", mtf_module_track|mtf_culture_west_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_west_eu),
  ("West5", "Echo_in_Eternity.ogg", mtf_module_track|mtf_culture_west_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_west_eu),
  ("West6", "Prana_WORLD_Here_we_come.ogg", mtf_module_track|mtf_culture_west_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_west_eu),
  ("West7", "PicturesPlay_Danza.ogg", mtf_module_track|mtf_culture_west_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_west_eu),
  ("West8", "Ignacio_Núñez_Wings_of_glory.ogg", mtf_module_track|mtf_culture_west_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_west_eu),
  ("West9", "Ignacio_Núñez_Mnemósine.ogg", mtf_module_track|mtf_culture_west_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_west_eu),
  ("West10", "Bard_Tale.ogg", mtf_module_track|mtf_culture_west_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_west_eu),
  ("West11", "Lost_Battle_New_Begining.ogg", mtf_module_track|mtf_culture_west_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_west_eu),
  ("West12", "Handful_of_Sorrow.ogg", mtf_module_track|mtf_culture_west_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_west_eu),
  ("West13", "travel_france_2.mp3", mtf_module_track|mtf_culture_west_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_west_eu),
  ("West14", "A_chantar_m'er_de_so_qieu_no_voldria.mp3", mtf_module_track|mtf_culture_west_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_west_eu),
  ("West15", "armorer.mp3", mtf_module_track|mtf_culture_west_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_west_eu),

  # Eastern eu
  
  ("Eastern1", "David_GayPerret_Redemption.ogg", mtf_module_track|mtf_culture_eastern_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_eastern_eu),
  ("Eastern2", "travel_baltic_2.ogg", mtf_module_track|mtf_culture_eastern_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_eastern_eu),
  ("Eastern3", "Dove_in_the_Sky.ogg", mtf_module_track|mtf_culture_eastern_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_eastern_eu),
  ("Eastern4", "Echo_in_Eternity.ogg", mtf_module_track|mtf_culture_eastern_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_eastern_eu),
  ("Eastern5", "Ignacio_Núñez_Wings_of_glory.ogg", mtf_module_track|mtf_culture_eastern_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_eastern_eu),
  ("Eastern6", "Ignacio_Núñez_Mnemósine.ogg", mtf_module_track|mtf_culture_eastern_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_eastern_eu),
  ("Eastern7", "Bard_Tale.ogg", mtf_module_track|mtf_culture_eastern_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_eastern_eu),
  ("Eastern8", "Lost_Battle_New_Begining.ogg", mtf_module_track|mtf_culture_eastern_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_eastern_eu),
  ("Eastern9", "Handful_of_Sorrow.ogg", mtf_module_track|mtf_culture_eastern_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_eastern_eu),
  ("Eastern10", "Klaipėdos_krašto_lietuvininkų_daina.mp3", mtf_module_track|mtf_culture_eastern_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_eastern_eu),
  #("Eastern11", "baltic_3.mp3", mtf_module_track|mtf_culture_eastern_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),

  # Britain
  
  ("Britain1", "David_GayPerret_Redemption.ogg", mtf_module_track|mtf_culture_britain|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_britain),
  ("Britain2", "travel_baltic_2.ogg", mtf_module_track|mtf_culture_britain|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_britain),
  ("Britain3", "Dove_in_the_Sky.ogg", mtf_module_track|mtf_culture_britain|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_britain),
  ("Britain4", "Echo_in_Eternity.ogg", mtf_module_track|mtf_culture_britain|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_britain),
  ("Britain5", "Ignacio_Núñez_Wings_of_glory.ogg", mtf_module_track|mtf_culture_britain|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_britain),
  ("Britain6", "Ignacio_Núñez_Mnemósine.ogg", mtf_module_track|mtf_culture_britain|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_britain),
  ("Britain7", "SimonBowman_Knight_Time.ogg", mtf_module_track|mtf_culture_britain|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_britain),
  ("Britain8", "Handful_of_Sorrow.ogg", mtf_module_track|mtf_culture_britain|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_britain),
  ("Britain9", "Klaipėdos_krašto_lietuvininkų_daina.mp3", mtf_module_track|mtf_culture_britain|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_britain),
  ("Britain10", "Ignacio_Núñez_Celtas.mp3", mtf_module_track|mtf_culture_britain|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_britain),
  ("Britain11", "England_Anon_1225_Miri_it_is_while_sumer_ilast.mp3", mtf_module_track|mtf_culture_britain|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_britain),

  # Scandinavia
  ("Scandinavia1", "David_GayPerret_Redemption.ogg", mtf_module_track|mtf_culture_scandinavia|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_scandinavia),
  ("Scandinavia2", "travel_baltic_2.ogg", mtf_module_track|mtf_culture_scandinavia|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_scandinavia),
  ("Scandinavia3", "Dove_in_the_Sky.ogg", mtf_module_track|mtf_culture_scandinavia|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_scandinavia),
  ("Scandinavia4", "Echo_in_Eternity.ogg", mtf_module_track|mtf_culture_scandinavia|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_scandinavia),
  ("Scandinavia5", "Ignacio_Núñez_Wings_of_glory.ogg", mtf_module_track|mtf_culture_scandinavia|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_scandinavia),
  ("Scandinavia6", "Ignacio_Núñez_Mnemósine.ogg", mtf_module_track|mtf_culture_scandinavia|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_scandinavia),
  ("Scandinavia7", "SimonBowman_Knight_Time.ogg", mtf_module_track|mtf_culture_scandinavia|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_scandinavia),
  ("Scandinavia8", "Handful_of_Sorrow.ogg", mtf_module_track|mtf_culture_scandinavia|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_scandinavia),
  ("Scandinavia10", "Ignacio_Núñez_Celtas.mp3", mtf_module_track|mtf_culture_scandinavia|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_scandinavia),
  ("Scandinavia11", "travel_nordic_2.ogg", mtf_module_track|mtf_culture_scandinavia|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_scandinavia),
  ("Scandinavia12", "travel_nordic_3.ogg", mtf_module_track|mtf_culture_scandinavia|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_scandinavia),
  ("Scandinavia13", "travel_nordic_4.ogg", mtf_module_track|mtf_culture_scandinavia|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_scandinavia),
  ("Scandinavia14", "travel_nordic_5.ogg", mtf_module_track|mtf_culture_scandinavia|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_scandinavia),

  # Mediterannia
  ("Mediterannia2", "David_GayPerret_Redemption.ogg", mtf_module_track|mtf_culture_mediterrania|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_mediterrania),
  ("Mediterannia3", "Castle_Dance.ogg", mtf_module_track|mtf_culture_mediterrania|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_mediterrania),
  ("Mediterannia4", "Dove_in_the_Sky.ogg", mtf_module_track|mtf_culture_mediterrania|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_mediterrania),
  ("Mediterannia5", "Echo_in_Eternity.ogg", mtf_module_track|mtf_culture_mediterrania|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_mediterrania),
  ("Mediterannia7", "PicturesPlay_Danza.ogg", mtf_module_track|mtf_culture_mediterrania|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_mediterrania),
  ("Mediterannia8", "Ignacio_Núñez_Wings_of_glory.ogg", mtf_module_track|mtf_culture_mediterrania|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_mediterrania),
  ("Mediterannia9", "Ignacio_Núñez_Mnemósine.ogg", mtf_module_track|mtf_culture_mediterrania|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_mediterrania),
  ("Mediterannia10", "Bard_Tale.ogg", mtf_module_track|mtf_culture_mediterrania|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_mediterrania),
  ("Mediterannia11", "Lost_Battle_New_Begining.ogg", mtf_module_track|mtf_culture_mediterrania|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_mediterrania),
  ("Mediterannia12", "Handful_of_Sorrow.ogg", mtf_module_track|mtf_culture_mediterrania|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_mediterrania),

  # Arabians
  ("Arabians1", "Desert_Flavours.ogg", mtf_module_track|mtf_culture_eastern_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_eastern_eu),
  ("Arabians2", "Medieval_Arab_Music_with_Qanun-Kanun.ogg", mtf_module_track|mtf_culture_eastern_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_eastern_eu),
  ("Arabians3", "Ignacio_Núñez_Mnemósine.ogg", mtf_module_track|mtf_culture_eastern_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_eastern_eu),
  ("Arabians4", "Handful_of_Sorrow.ogg", mtf_module_track|mtf_culture_eastern_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_eastern_eu),
  ("Arabians5", "Echo_in_Eternity.ogg", mtf_module_track|mtf_culture_eastern_eu|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_eastern_eu),

  # Byzantine  
  ("Byzantine1", "David_GayPerret_Redemption.ogg", mtf_module_track|mtf_culture_byzantine|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_byzantine),
  ("Byzantine2", "Dove_in_the_Sky.ogg", mtf_module_track|mtf_culture_byzantine|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_byzantine),
  ("Byzantine3", "Echo_in_Eternity.ogg", mtf_module_track|mtf_culture_byzantine|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_byzantine),
  ("Byzantine4", "Ignacio_Núñez_Wings_of_glory.ogg", mtf_module_track|mtf_culture_byzantine|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_byzantine),
  ("Byzantine5", "Ignacio_Núñez_Mnemósine.ogg", mtf_module_track|mtf_culture_byzantine|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_byzantine),
  ("Byzantine6", "Lost_Battle_New_Begining.ogg", mtf_module_track|mtf_culture_byzantine|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_byzantine),
  ("Byzantine7", "Nightingale_Kratima.mp3", mtf_module_track|mtf_culture_byzantine|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_byzantine),
  ("Byzantine8", "Χριστόδουλος_Χάλαρης_Κάτω_στον_Αγ_Γιάννη.mp3", mtf_module_track|mtf_culture_byzantine|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_byzantine),
  ("Byzantine9", "byz_4.mp3", mtf_module_track|mtf_culture_byzantine|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_byzantine),
  ("Byzantine10", "byz_2.mp3", mtf_module_track|mtf_culture_byzantine|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_byzantine),
  ("Byzantine11", "Wild_bird_become_tame.mp3", mtf_module_track|mtf_culture_byzantine|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_byzantine),



  # Encounter Theme: Christian & Others
  ("EncounterChristian1", "Euro_Camp_Battle_1_Destiny.mp3", mtf_module_track|mtf_encounter_christian, 0),
 
  # Encounter Theme: Muslim & Mongols
  ("EncounterNonChristian1", "Arabic_Camp_Battle_1_Honour_Of_Sultan.mp3", mtf_module_track|mtf_encounter_nonchristian, 0),
 
  # Travel War Theme: Christian & Others  
  ("WarChristian1", "Iska_Blackfyre.ogg", mtf_module_track|mtf_hostile_teritory|mtf_hostile_teritory_christian|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_hostile_teritory_christian),
  ("WarChristian2", "First_Battle.ogg", mtf_module_track|mtf_hostile_teritory|mtf_hostile_teritory_christian|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_hostile_teritory_christian),
  ("WarChristian3", "09bis.ogg", mtf_module_track|mtf_hostile_teritory|mtf_hostile_teritory_christian|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_hostile_teritory_christian),
  ("WarChristian4", "March_of_Honor.ogg", mtf_module_track|mtf_hostile_teritory|mtf_hostile_teritory_christian|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_hostile_teritory_christian),
  ("WarChristian5", "The_Die_is_Cast.ogg", mtf_module_track|mtf_hostile_teritory|mtf_hostile_teritory_christian|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_hostile_teritory_christian),
  ("WarChristian6", "euro_1.ogg", mtf_module_track|mtf_hostile_teritory|mtf_hostile_teritory_christian|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_hostile_teritory_christian),
  ("WarChristian7", "euro_2.ogg", mtf_module_track|mtf_hostile_teritory|mtf_hostile_teritory_christian|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_hostile_teritory_christian),
  ("WarChristian8", "euro_3.ogg", mtf_module_track|mtf_hostile_teritory|mtf_hostile_teritory_christian|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_hostile_teritory_christian),
  ("WarChristian9", "euro_4.ogg", mtf_module_track|mtf_hostile_teritory|mtf_hostile_teritory_christian|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_hostile_teritory_christian),
  ("WarChristian10", "euro_5.ogg", mtf_module_track|mtf_hostile_teritory|mtf_hostile_teritory_christian|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_hostile_teritory_christian),
  ("WarChristian11", "euro_12.ogg", mtf_module_track|mtf_hostile_teritory|mtf_hostile_teritory_christian|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_hostile_teritory_christian),
  # Travel War Theme: Muslim & Mongols
  ("WarMuslim1", "Iska_Blackfyre.ogg", mtf_module_track|mtf_hostile_teritory|mtf_hostile_teritory_nonchristian|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_hostile_teritory_nonchristian),
  ("WarMuslim2", "saracen_1.ogg", mtf_module_track|mtf_hostile_teritory|mtf_hostile_teritory_nonchristian|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_hostile_teritory_nonchristian),
  ("WarMuslim3", "saracen_3.ogg", mtf_module_track|mtf_hostile_teritory|mtf_hostile_teritory_nonchristian|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_hostile_teritory_nonchristian),
  ("WarMuslim4", "saracen_4.ogg", mtf_module_track|mtf_hostile_teritory|mtf_hostile_teritory_nonchristian|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_hostile_teritory_nonchristian),

  # Battle Theme: Christian & Others
  # AMBUSH!
    ("BattleChristian0", "(Euro_Battle_1)_Duke_of_Death.mp3", mtf_module_track|mtf_sit_siege|mtf_sit_ambushed|mtf_battle_christian, 0),
  # AMBUSH!
    ("BattleChristian1", "(Euro_Battle_2)_Nothing_Left.mp3", mtf_module_track|mtf_sit_siege|mtf_sit_ambushed|mtf_battle_christian, 0),
  ("BattleChristian2", "(Euro_Battle_3)_Crusaders.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_ambushed|mtf_battle_christian, 0),
  ("BattleChristian3", "(Teutonic_Battle)_Darker_Skies_Ahead.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_ambushed|mtf_battle_christian, 0),
  ("BattleChristian4", "(Euro_Battle_4)_War_of_Kings.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_ambushed|mtf_battle_christian, 0),
  ("BattleChristian5", "(Crusades_Battle)_Valley_Of_Death.mp3", mtf_module_track|mtf_sit_fight|mtf_battle_christian, 0),
  ("BattleChristian6", "(Britannia_Camp_Battle)_Tally-ho.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_ambushed|mtf_battle_christian, 0),
  ("BattleChristian7", "(Euro_Mobilize_1)_Sister_Davul.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_ambushed|mtf_battle_christian, 0),
  ("BattleChristian8", "(Euro_Mobilize_2)_Solenka.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_ambushed|mtf_battle_christian, 0),
  ("BattleChristian9", "(Euro_Mobilize_3)_This_is_it.mp3", mtf_module_track|mtf_sit_fight|mtf_battle_christian, 0),
  ("BattleChristian10", "(Mediterranean_Mobilize_1)_Mare_Nostrum.mp3", mtf_module_track|mtf_sit_fight|mtf_battle_christian, 0),
  ("BattleChristian11", "(Mediterranean_Mobilize_2)_Death_Lullaby.mp3", mtf_module_track|mtf_sit_fight|mtf_battle_christian, 0),
  ("BattleChristian12", "(Mediterranean_Mobilize_2)_Song_For_Toomba.mp3", mtf_module_track|mtf_sit_fight|mtf_battle_christian, 0),
  ("BattleChristian13", "euro_10.ogg", mtf_module_track|mtf_sit_fight|mtf_battle_christian, 0),

  ("BattleChristian14", "(Britannia_Camp_Battle)_Tally-ho.mp3", mtf_module_track|mtf_sit_fight|mtf_battle_christian, 0),
  ("BattleChristian15", "(Euro_Mobilize_1)_Sister_Davul.mp3", mtf_module_track|mtf_sit_fight|mtf_battle_christian, 0),
  ("BattleChristian16", "(Euro_Mobilize_2)_Solenka.mp3", mtf_module_track|mtf_sit_fight|mtf_battle_christian, 0),
      # Siege & Ambush
      ("BattleChristian14", "(Euro_Battle_1)_Duke_of_Death.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_siege|mtf_battle_christian, 0),
      ("BattleChristian15", "(Euro_Battle_2)_Nothing_Left.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_siege|mtf_battle_christian, 0),
  
  # Battle Theme: Muslim
  ("BattleMuslim0", "(Arabic_Battle_1)_Crack_your_head_with_a_Tabla.mp3", mtf_module_track|mtf_sit_fight|mtf_battle_nonchristian, 0),
  ("BattleMuslim1", "(Arabic_Battle_2)_Wind_Cuts.mp3", mtf_module_track|mtf_sit_fight|mtf_battle_nonchristian, 0),
  ("BattleMuslim2", "(Mediterranean_Battle_1)_Lifted_To_The_Hotplate.mp3", mtf_module_track|mtf_sit_fight|mtf_battle_nonchristian, 0),
  # AMBUSH!
   ("BattleMuslim3", "Arabic_Camp_Battle_1_Honour_Of_Sultan.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_ambushed|mtf_battle_nonchristian, 0),
  ("BattleMuslim4", "(Arabic_Mobilize_1)_High_Winds.mp3", mtf_module_track|mtf_sit_fight|mtf_battle_nonchristian, 0),
  ("BattleMuslim5", "saracen_6.ogg", mtf_module_track|mtf_sit_fight|mtf_battle_nonchristian, 0),
  ("BattleMuslim6", "(Mediterranean_Mobilize_1)_Mare_Nostrum.mp3", mtf_module_track|mtf_sit_fight|mtf_battle_nonchristian, 0),
  ("BattleMuslim7", "(Mediterranean_Mobilize_2)_Death_Lullaby.mp3", mtf_module_track|mtf_sit_fight|mtf_battle_nonchristian, 0),
  ("BattleMuslim8", "(Mediterranean_Mobilize_2)_Song_For_Toomba.mp3", mtf_module_track|mtf_sit_fight|mtf_battle_nonchristian, 0),
      # Siege
      ("BattleMuslim9", "(Euro_Battle_1)_Duke_of_Death.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_siege|mtf_battle_nonchristian, 0),
      ("BattleMuslim10", "(Euro_Battle_2)_Nothing_Left.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_siege|mtf_battle_nonchristian, 0),
  
  # Victory Themes
  ("VictoryChristian", "Euro_Win_1_Going_Home.mp3", mtf_module_track|mtf_persist_until_finished, 0),
  ("VictoryMuslim", "Arabic_Win_1_Balalip.mp3", mtf_module_track|mtf_persist_until_finished, 0),
  ("VictoryOthers", "victorious_neutral_1.ogg", mtf_persist_until_finished, 0),

#tom end

  ("victorious_evil", "victorious_evil.ogg", mtf_module_track|mtf_persist_until_finished, 0),
  
  ("wedding", "wedding.ogg", mtf_persist_until_finished, 0),
  ("coronation", "coronation.ogg", mtf_persist_until_finished, 0),
  
  #("ambient_1", "ambient_1.ogg", mtf_persist_until_finished|mtf_module_track|mtf_sit_fight|mtf_culture_all, 0),
  #("ambient_2", "ambient_2.ogg", mtf_persist_until_finished|mtf_module_track|mtf_sit_fight|mtf_culture_all, 0),
  #("ambient_3", "ambient_3.ogg", mtf_persist_until_finished|mtf_module_track|mtf_sit_fight|mtf_culture_all, 0),
  #("ambient_4", "ambient_4.ogg", mtf_persist_until_finished|mtf_module_track|mtf_sit_fight|mtf_culture_all, 0),
  #("ambient_5", "ambient_5.ogg", mtf_persist_until_finished|mtf_module_track|mtf_sit_fight|mtf_culture_all, 0),
  #("ambient_6", "ambient_6.ogg", mtf_persist_until_finished|mtf_module_track|mtf_sit_fight|mtf_culture_all, 0),
  #("ambient_7", "ambient_7.ogg", mtf_persist_until_finished|mtf_module_track|mtf_sit_fight|mtf_culture_all, 0),
  #("ambient_8", "ambient_8.ogg", mtf_persist_until_finished|mtf_module_track|mtf_sit_fight|mtf_culture_all, 0),
  #("ambient_9", "ambient_9.ogg", mtf_persist_until_finished|mtf_module_track|mtf_sit_fight|mtf_culture_all, 0),
  #("ambient_10", "ambient_10.ogg", mtf_persist_until_finished|mtf_module_track, 0),
  #("ambient_end", "silence.ogg", mtf_persist_until_finished|mtf_module_track, 0),
]

  