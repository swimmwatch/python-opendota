# MatchResponsePlayers

player

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_id** | **int** | Match ID | [optional] 
**player_slot** | **int** | Which slot the player is in. 0-127 are Radiant, 128-255 are Dire | [optional] 
**ability_upgrades_arr** | **[int]** | An array describing how abilities were upgraded | [optional] 
**ability_uses** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object containing information on how many times the played used their abilities | [optional] 
**ability_targets** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object containing information on who the player used their abilities on | [optional] 
**damage_targets** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object containing information on how and how much damage the player dealt to other heroes | [optional] 
**account_id** | **int** | account_id | [optional] 
**actions** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object containing information on how many and what type of actions the player issued to their hero | [optional] 
**additional_units** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object containing information on additional units the player had under their control | [optional] 
**assists** | **int** | Number of assists the player had | [optional] 
**backpack_0** | **int** | Item in backpack slot 0 | [optional] 
**backpack_1** | **int** | Item in backpack slot 1 | [optional] 
**backpack_2** | **int** | Item in backpack slot 2 | [optional] 
**buyback_log** | [**[MatchResponseBuybackLog]**](MatchResponseBuybackLog.md) | Array containing information about buybacks | [optional] 
**camps_stacked** | **int** | Number of camps stacked | [optional] 
**connection_log** | [**[MatchResponseConnectionLog]**](MatchResponseConnectionLog.md) | Array containing information about the player&#39;s disconnections and reconnections | [optional] 
**creeps_stacked** | **int** | Number of creeps stacked | [optional] 
**damage** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object containing information about damage dealt by the player to different units | [optional] 
**damage_inflictor** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object containing information about about the sources of this player&#39;s damage to heroes | [optional] 
**damage_inflictor_received** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object containing information about the sources of damage received by this player from heroes | [optional] 
**damage_taken** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object containing information about from whom the player took damage | [optional] 
**deaths** | **int** | Number of deaths | [optional] 
**denies** | **int** | Number of denies | [optional] 
**dn_t** | **[int]** | Array containing number of denies at different times of the match | [optional] 
**gold** | **int** | Gold at the end of the game | [optional] 
**gold_per_min** | **int** | Gold Per Minute obtained by this player | [optional] 
**gold_reasons** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object containing information on how the player gainined gold over the course of the match | [optional] 
**gold_spent** | **int** | How much gold the player spent | [optional] 
**gold_t** | **[int]** | Array containing total gold at different times of the match | [optional] 
**hero_damage** | **int** | Hero Damage Dealt | [optional] 
**hero_healing** | **int** | Hero Healing Done | [optional] 
**hero_hits** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object containing information on how many ticks of damages the hero inflicted with different spells and damage inflictors | [optional] 
**hero_id** | **int** | The ID value of the hero played | [optional] 
**item_0** | **int** | Item in the player&#39;s first slot | [optional] 
**item_1** | **int** | Item in the player&#39;s second slot | [optional] 
**item_2** | **int** | Item in the player&#39;s third slot | [optional] 
**item_3** | **int** | Item in the player&#39;s fourth slot | [optional] 
**item_4** | **int** | Item in the player&#39;s fifth slot | [optional] 
**item_5** | **int** | Item in the player&#39;s sixth slot | [optional] 
**item_uses** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object containing information about how many times a player used items | [optional] 
**kill_streaks** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object containing information about the player&#39;s killstreaks | [optional] 
**killed** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object containing information about what units the player killed | [optional] 
**killed_by** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object containing information about who killed the player | [optional] 
**kills** | **int** | Number of kills | [optional] 
**kills_log** | [**[MatchResponseKillsLog]**](MatchResponseKillsLog.md) | Array containing information on which hero the player killed at what time | [optional] 
**lane_pos** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object containing information on lane position | [optional] 
**last_hits** | **int** | Number of last hits | [optional] 
**leaver_status** | **int** | Integer describing whether or not the player left the game. 0: didn&#39;t leave. 1: left safely. 2+: Abandoned | [optional] 
**level** | **int** | Level at the end of the game | [optional] 
**lh_t** | **[int]** | Array describing last hits at each minute in the game | [optional] 
**life_state** | **bool, date, datetime, dict, float, int, list, str, none_type** | life_state | [optional] 
**max_hero_hit** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object with information on the highest damage instance the player inflicted | [optional] 
**multi_kills** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object with information on the number of the number of multikills the player had | [optional] 
**obs** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object with information on where the player placed observer wards. The location takes the form (outer number, inner number) and are from ~64-192. | [optional] 
**obs_left_log** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | obs_left_log | [optional] 
**obs_log** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | Object containing information on when and where the player placed observer wards | [optional] 
**obs_placed** | **int** | Total number of observer wards placed | [optional] 
**party_id** | **int** | party_id | [optional] 
**permanent_buffs** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | Array describing permanent buffs the player had at the end of the game. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/permanent_buffs.json | [optional] 
**pings** | **int** | Total number of pings | [optional] 
**purchase** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object containing information on the items the player purchased | [optional] 
**purchase_log** | [**[MatchResponsePurchaseLog]**](MatchResponsePurchaseLog.md) | Object containing information on when items were purchased | [optional] 
**rune_pickups** | **int** | Number of runes picked up | [optional] 
**runes** | **{str: (int,)}** | Object with information about which runes the player picked up | [optional] 
**runes_log** | [**[MatchResponseRunesLog]**](MatchResponseRunesLog.md) | Array with information on when runes were picked up | [optional] 
**sen** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object with information on where sentries were placed. The location takes the form (outer number, inner number) and are from ~64-192. | [optional] 
**sen_left_log** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | Array containing information on when and where the player placed sentries | [optional] 
**sen_log** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | Array with information on when and where sentries were placed by the player | [optional] 
**sen_placed** | **int** | How many sentries were placed by the player | [optional] 
**stuns** | **float** | Total stun duration of all stuns by the player | [optional] 
**times** | **[int]** | Time in seconds corresponding to the time of entries of other arrays in the match. | [optional] 
**tower_damage** | **int** | Total tower damage done by the player | [optional] 
**xp_per_min** | **int** | Experience Per Minute obtained by the player | [optional] 
**xp_reasons** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object containing information on the sources of this player&#39;s experience | [optional] 
**xp_t** | **[int]** | Experience at each minute of the game | [optional] 
**personaname** | **str** | personaname | [optional] 
**name** | **str** | name | [optional] 
**last_login** | **datetime** | Time of player&#39;s last login | [optional] 
**radiant_win** | **bool** | Boolean indicating whether Radiant won the match | [optional] 
**start_time** | **int** | Start time of the match in seconds since 1970 | [optional] 
**duration** | **int** | Duration of the game in seconds | [optional] 
**cluster** | **int** | cluster | [optional] 
**lobby_type** | **int** | Integer corresponding to lobby type of match. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/lobby_type.json | [optional] 
**game_mode** | **int** | Integer corresponding to game mode played. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/game_mode.json | [optional] 
**patch** | **int** | Integer representing the patch the game was played on | [optional] 
**region** | **int** | Integer corresponding to the region the game was played on | [optional] 
**is_radiant** | **bool** | Boolean for whether or not the player is on Radiant | [optional] 
**win** | **int** | Binary integer representing whether or not the player won | [optional] 
**lose** | **int** | Binary integer representing whether or not the player lost | [optional] 
**total_gold** | **int** | Total gold at the end of the game | [optional] 
**total_xp** | **int** | Total experience at the end of the game | [optional] 
**kills_per_min** | **float** | Number of kills per minute | [optional] 
**kda** | **float** | kda | [optional] 
**abandons** | **int** | abandons | [optional] 
**neutral_kills** | **int** | Total number of neutral creeps killed | [optional] 
**tower_kills** | **int** | Total number of tower kills the player had | [optional] 
**courier_kills** | **int** | Total number of courier kills the player had | [optional] 
**lane_kills** | **int** | Total number of lane creeps killed by the player | [optional] 
**hero_kills** | **int** | Total number of heroes killed by the player | [optional] 
**observer_kills** | **int** | Total number of observer wards killed by the player | [optional] 
**sentry_kills** | **int** | Total number of sentry wards killed by the player | [optional] 
**roshan_kills** | **int** | Total number of roshan kills (last hit on roshan) the player had | [optional] 
**necronomicon_kills** | **int** | Total number of Necronomicon creeps killed by the player | [optional] 
**ancient_kills** | **int** | Total number of Ancient creeps killed by the player | [optional] 
**buyback_count** | **int** | Total number of buyback the player used | [optional] 
**observer_uses** | **int** | Number of observer wards used | [optional] 
**sentry_uses** | **int** | Number of sentry wards used | [optional] 
**lane_efficiency** | **float** | lane_efficiency | [optional] 
**lane_efficiency_pct** | **float** | lane_efficiency_pct | [optional] 
**lane** | **int** | Integer referring to which lane the hero laned in | [optional] 
**lane_role** | **int** | lane_role | [optional] 
**is_roaming** | **bool** | Boolean referring to whether or not the player roamed | [optional] 
**purchase_time** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object with information on when the player last purchased an item | [optional] 
**first_purchase_time** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object with information on when the player first puchased an item | [optional] 
**item_win** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object with information on whether or not the item won | [optional] 
**item_usage** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object containing binary integers the tell whether the item was purchased by the player (note: this is always 1) | [optional] 
**purchase_tpscroll** | **bool, date, datetime, dict, float, int, list, str, none_type** | Total number of TP scrolls purchased by the player | [optional] 
**actions_per_min** | **int** | Actions per minute | [optional] 
**life_state_dead** | **int** | life_state_dead | [optional] 
**rank_tier** | **int** | The rank tier of the player. Tens place indicates rank, ones place indicates stars. | [optional] 
**cosmetics** | **[int]** | cosmetics | [optional] 
**benchmarks** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object containing information on certain benchmarks like GPM, XPM, KDA, tower damage, etc | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


