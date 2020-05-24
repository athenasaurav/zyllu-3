## New Story
* greet
    - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## New Story_details_name_all

* greet
    - utter_greet
* fetch_details_name_all{"details":"all details","name":"kumar saurav"}
    - slot{"details":"all details"}
    - slot{"name":"kumar saurav"}
    - action_fetch_all_details_name
    - utter_anyother_help

## New Story_fetch_details_name_id

* greet
    - utter_greet
* fetch_details_name_id{"id_details":"employee id","name":"kumar saurav"}
    - slot{"id_details":"employee code"}
    - slot{"name":"Kumar Saurav"}
    - action_fetch_all_details_id
    - utter_anyother_help
* fetch_details_name_id{"id_details":"employee code","name":"aman raj"}
    - slot{"id_details":"employee code"}
    - slot{"name":"aman raj"}
    - action_fetch_all_details_post
    - utter_anyother_help

## New Story_fetch_details_name_id

* greet
    - utter_greet
* fetch_details_name_id{"id_details":"employee id","name":"kumar saurav"}
    - slot{"id_details":"employee id"}
    - slot{"name":"kumar saurav"}
    - action_fetch_id_details_name
    - utter_anyother_help
* fetch_details_name_id{"id_details":"employee id","name":"jasmine"}
    - slot{"id_details":"employee id"}
    - slot{"name":"jasmine"}
    - action_fetch_id_details_name
    - utter_anyother_help
* fetch_details_name_id{"id_details":"employee id","name":"aman raj"}
    - slot{"id_details":"employee id"}
    - slot{"name":"jasmine"}
    - action_fetch_id_details_name
    - utter_anyother_help

## New Story_fetch_details_name_bday

* greet
    - utter_greet
* fetch_details_name_bday{"bday":"birthday","name":"kumar saurav"}
    - slot{"bday":"birthday"}
    - slot{"name":"kumar saurav"}
    - action_fetch_bday_details_name
    - utter_anyother_help
* fetch_details_name_bday{"bday":"bday","name":"jasmine"}
    - slot{"bday":"bday"}
    - slot{"name":"jasmine"}
    - action_fetch_bday_details_name
    - utter_anyother_help
* fetch_details_name_bday{"bday":"date of birth","name":"aman raj"}
    - slot{"bday":"date of birth"}
    - slot{"name":"jasmine"}
    - action_fetch_bday_details_name
    - utter_anyother_help

## New Story_fetch_details_name_designation

* greet
    - utter_greet
* fetch_details_name_bday{"desg_details":"designation","name":"kumar saurav"}
    - slot{"desg_details":"designation"}
    - slot{"name":"kumar saurav"}
    - action_fetch_desg_details_name
    - utter_anyother_help
* fetch_details_name_bday{"desg_details":"post","name":"jasmine"}
    - slot{"desg_details":"post"}
    - slot{"name":"jasmine"}
    - action_fetch_desg_details_name
    - utter_anyother_help
* fetch_details_name_bday{"desg_details":"work profile","name":"aman raj"}
    - slot{"desg_details": "work profile"}
    - slot{"name":"jasmine"}
    - action_fetch_desg_details_name
    - utter_anyother_help

## New Story_fetch_details_name_designation_bday

* greet
    - utter_greet
* fetch_details_name_bday{"desg_details":"designation","bday":"birthday","name":"kumar saurav"}
    - slot{"desg_details":"designation"}
    - slot{"bday":"birthday"}
    - slot{"name":"kumar saurav"}
    - action_fetch_desg_bday_details_name
    - utter_anyother_help
* fetch_details_name_bday{"desg_details":"post","bday":"bday","name":"jasmine"}
    - slot{"desg_details":"post"}
    - slot{"bday":"bday"}
    - slot{"name":"jasmine"}
    - action_fetch_desg_bday_details_name
    - utter_anyother_help
* fetch_details_name_bday{"desg_details":"work profile","bday":"date of birth","name":"aman raj"}
    - slot{"desg_details": "work profile"}
    - slot{"bday":"date of birth"}
    - slot{"name":"jasmine"}
    - action_fetch_desg_bday_details_name
    - utter_anyother_help

## New Story_fetch_details_name_id_bday

* greet
    - utter_greet
* fetch_details_name_bday{"id_details":"employee id","bday":"birthday","name":"kumar saurav"}
    - slot{"id_details":"employee id"}
    - slot{"bday":"birthday"}
    - slot{"name":"kumar saurav"}
    - action_fetch_id_bday_details_name
    - utter_anyother_help
* fetch_details_name_bday{"id_details":"employee id","bday":"bday","name":"jasmine"}
    - slot{"id_details":"employee id"}
    - slot{"bday":"bday"}
    - slot{"name":"jasmine"}
    - action_fetch_id_bday_details_name
    - utter_anyother_help
* fetch_details_name_bday{"id_details":"employee id","bday":"date of birth","name":"aman raj"}
    - slot{"id_details":"employee id"}
    - slot{"bday":"date of birth"}
    - slot{"name":"jasmine"}
    - action_fetch_id_bday_details_name
    - utter_anyother_help

## New Story_fetch_details_name_id_designation

* greet
    - utter_greet
* fetch_details_name_bday{"id_details":"employee id","desg_details":"designation","name":"kumar saurav"}
    - slot{"id_details":"employee id"}
    - slot{"desg_details":"designation"}
    - slot{"name":"kumar saurav"}
    - action_fetch_id_desg_details_name
    - utter_anyother_help
* fetch_details_name_bday{"id_details":"employee id","desg_details":"post","name":"jasmine"}
    - slot{"id_details":"employee id"}
    - slot{"desg_details":"post"}
    - slot{"name":"jasmine"}
    - action_fetch_id_desg_details_name
    - utter_anyother_help
* fetch_details_name_bday{"id_details":"employee id","desg_details":"work profile","name":"aman raj"}
    - slot{"id_details":"employee id"}
    - slot{"desg_details":"work profile"}
    - slot{"name":"jasmine"}
    - action_fetch_id_desg_details_name
    - utter_anyother_help

## New Story_fetch_details_id_all

* greet
    - utter_greet
* fetch_details_id_all{"details":"details","id":"214"}
    - slot{"details":"details"}
    - slot{"id":"214"}
    - action_fetch_all_details_id
    - utter_anyother_help
* fetch_details_post_all{"details":"details","post":"founder"}
    - slot{"details":"details"}
    - slot{"post":"founder"}
    - action_fetch_all_details_post
    - utter_anyother_help
* fetch_details_post_all{"details":"details","post":"co-founder"}
    - slot{"details":"details"}
    - slot{"post":"co-founder"}
    - action_fetch_all_details_post
    - utter_anyother_help

## New Story_fetch_details_id_name

* greet
    - utter_greet
* fetch_details_id_name{"names":"name","id":"214"}
    - slot{"names":"name"}
    - slot{"id":"214"}
    - action_fetch_name_details_id
    - utter_anyother_help
* fetch_details_id_name{"names":"full name","id":"215"}
    - slot{"names":"full name"}
    - slot{"id":"215"}
    - action_fetch_name_details_id
    - utter_anyother_help
* fetch_details_id_name{"names":"first name","id":"216"}
    - slot{"names":"first name"}
    - slot{"id":"216"}
    - action_fetch_name_details_id
    - utter_anyother_help

## New Story_fetch_details_id_bday

* greet
    - utter_greet
* fetch_details_id_bday{"bday":"born","id":"214"}
    - slot{"bday":"born"}
    - slot{"id":"214"}
    - action_fetch_bday_details_id
    - utter_anyother_help
* fetch_details_id_bday{"bday":"birthday","id":"215"}
    - slot{"bday":"birthday"}
    - slot{"id":"215"}
    - action_fetch_bday_details_id
    - utter_anyother_help
* fetch_details_id_bday{"bday":"date of birth","id":"216"}
    - slot{"bday":"date of birth"}
    - slot{"id":"216"}
    - action_fetch_bday_details_id
    - utter_anyother_help

## New Story_fetch_details_id_desgnination

* greet
    - utter_greet
* fetch_details_id_designation{"desg_details":"post","id":"214"}
    - slot{"desg_details":"post"}
    - slot{"id":"214"}
    - action_fetch_desg_details_id
    - utter_anyother_help
* fetch_details_id_designation{"desg_details":"designation","id":"215"}
    - slot{"desg_details":"designation"}
    - slot{"id":"215"}
    - action_fetch_desg_details_id
    - utter_anyother_help
* fetch_details_id_designation{"desg_details":"profile","id":"216"}
    - slot{"desg_details":"profile"}
    - slot{"id":"216"}
    - action_fetch_desg_details_id
    - utter_anyother_help

## New Story_fetch_details_id_name_bday

* greet
    - utter_greet
* fetch_details_id_name_bday{"id_details":"employee id","bday":"born","names":"name"}
    - slot{"id_details":"employee id"}
    - slot{"bday":"born"}
    - slot{"names":"name"}
    - action_fetch_name_bday_details_id
    - utter_anyother_help
* fetch_details_id_name_bday{"id_details":"employee id","bday":"birthday","names":"lastname"}
    - slot{"id_details":"employee id"}
    - slot{"bday":"birthday"}
    - slot{"names":"lastname"}
    - action_fetch_name_bday_details_id
    - utter_anyother_help
* fetch_details_id_name_bday{"id_details":"employee id","bday":"date of birth","names":"firstname"}
    - slot{"id_details":"employee id"}
    - slot{"bday":"date of birth"}
    - slot{"names":"firstname"}
    - action_fetch_name_bday_details_id
    - utter_anyother_help

## New Story_fetch_details_id_designation_bday

* greet
    - utter_greet
* fetch_details_id_designation_bday{"id_details":"employee id","bday":"born","desg_details":"post"}
    - slot{"id_details":"employee id"}
    - slot{"bday":"born"}
    - slot{"desg_details":"post"}
    - action_fetch_desg_bday_details_id
    - utter_anyother_help
* fetch_details_id_designation_bday{"id_details":"employee id","bday":"birthday","desg_details":"profile"}
    - slot{"id_details":"employee id"}
    - slot{"bday":"birthday"}
    - slot{"desg_details":"profile"}
    - action_fetch_desg_bday_details_id
    - utter_anyother_help
* fetch_details_id_designation_bday{"id_details":"employee id","bday":"date of birth","desg_details":"designation"}
    - slot{"id_details":"employee id"}
    - slot{"bday":"date of birth"}
    - slot{"desg_details":"designation"}
    - action_fetch_desg_bday_details_id
    - utter_anyother_help

## New Story_fetch_details_id_designation_name

* greet
    - utter_greet
* fetch_details_id_designation_name{"id_details":"employee id","desg_details":"post","names":"name"}
    - slot{"id_details":"employee id"}
    - slot{"desg_details":"post"}
    - slot{"names":"name"}
    - action_fetch_name_desg_details_id
    - utter_anyother_help
* fetch_details_id_designation_name{"id_details":"employee id","desg_details":"profile","names":"lastname"}
    - slot{"id_details":"employee id"}
    - slot{"desg_details":"profile"}
    - slot{"names":"lastname"}
    - action_fetch_name_desg_details_id
    - utter_anyother_help
* fetch_details_id_designation_name{"id_details":"employee id","desg_details":"designation","names":"firstname"}
    - slot{"id_details":"employee id"}
    - slot{"desg_details":"designation"}
    - slot{"names":"firstname"}
    - action_fetch_name_desg_details_id
    - utter_anyother_help

## New Story_fetch_details_post_all

* greet
    - utter_greet
* fetch_details_post_all{"details":"details","post":"founder"}
    - slot{"details":"details"}
    - slot{"post":"founder"}
    - action_fetch_all_details_post
    - utter_anyother_help
* fetch_details_post_all{"details":"details","post":"co-founder"}
    - slot{"details":"details"}
    - slot{"post":"co-founder"}
    - action_fetch_all_details_post
    - utter_anyother_help

## New Story_save_details_name_all
* greet
    - utter_greet
* save_data{"save_data": "save his data", "name": "Kumar Saurav"}
  - slot{"save_data": "save his data"}
  - slot{"name": "Kumar Saurav"}
  - utter_Q2
* employee_id{"save_data": "save his data", "name": "Kumar Saurav", "id": "222"}
  - slot{"save_data": "save his data"}
  - slot{"name": "Kumar Saurav"}
  - slot{"id": "222"}
  - utter_Q3
* designation{"save_data": "save his data", "name": "Kumar Saurav", "id": "222", "post": "Director"}
  - slot{"save_data": "save his data"}
  - slot{"name": "Kumar Saurav"}
  - slot{"id": "222"}
  - slot{"post": "Director"}
  - utter_Q4
* dob{"save_data": "save his data", "name": "Kumar Saurav", "id": "222", "post": "Director", "birth": "19-07-1992"}
  - slot{"save_data": "save his data"}
  - slot{"name": "Kumar Saurav"}
  - slot{"id": "222"}
  - slot{"post": "Director"}
  - slot{"birth": "19-07-1992"}
  - action_save_dob
  - utter_anyother_help

## New Story_save_details_id_all
* greet
    - utter_greet
* save_data{"save_data": "save his data", "id": "212"}
  - slot{"save_data": "save his data"}
  - slot{"id": "212"}
  - utter_Q1
* name{"save_data": "save his data", "id": "212", "name": "Kumar Saurav"}
  - slot{"save_data": "save his data"}
  - slot{"id": "212"}
  - slot{"name": "Kumar Saurav"}
  - utter_Q3
* designation{"save_data": "save his data", "id": "212","name": "Kumar Saurav", "post": "Director"}
  - slot{"save_data": "save his data"}
  - slot{"id": "222"}
  - slot{"name": "Kumar Saurav"}
  - slot{"post": "Director"}
  - utter_Q4
* dob{"save_data": "save his data", "id": "222","name": "Kumar Saurav", "post": "Director", "birth": "19-07-1992"}
  - slot{"save_data": "save his data"}
  - slot{"name": "Kumar Saurav"}
  - slot{"id": "222"}
  - slot{"post": "Director"}
  - slot{"birth": "19-07-1992"}
  - action_save_dob
  - utter_anyother_help

## New Story_save_details_all
* greet
    - utter_greet
* save_data{"save_data": "save his data"}
  - slot{"save_data": "save his data"}
  - utter_Q1
* name{"save_data": "save his data", "name": "Kumar Saurav"}
  - slot{"save_data": "save his data"}
  - slot{"name": "Kumar Saurav"}
  - utter_Q2
* employee_id{"save_data": "save his data", "name": "Kumar Saurav", "id": "222"}
  - slot{"save_data": "save his data"}
  - slot{"name": "Kumar Saurav"}
  - slot{"id": "222"}
  - utter_Q3
* designation{"save_data": "save his data", "name":"Kumar Saurav", "id": "222", "post":"Director"}
  - slot{"save_data":"save his data"}
  - slot{"name":"Kumar Saurav"}
  - slot{"id":"222"}
  - slot{"post":"Director"}
  - utter_Q4
* dob{"save_data": "save his data", "name": "Kumar Saurav", "id": "222", "post": "Director", "birth":"19-07-1992"}
  - slot{"save_data": "save his data"}
  - slot{"name": "Kumar Saurav"}
  - slot{"id": "222"}
  - slot{"post": "Director"}
  - slot{"birth": "19-07-1992"}
  - action_save_dob
  - utter_anyother_help

## interactive_story_save_details_all
* greet
    - utter_greet
* save_data{"save_data": "save data", "name": "kiran"}
    - slot{"name": "kiran"}
    - slot{"save_data": "save data"}
    - utter_Q2
* employee_id{"id": "232"}
    - slot{"id": "232"}
    - utter_Q3
* designation{"post": "cto"}
    - slot{"post": "cto"}
    - utter_Q4
* dob{"birth": "19-04-1988"}
    - slot{"birth": "19-04-1988"}
    - action_save_dob
    - reset_slots
    - utter_anyother_help
* save_data{"save_data": "save data", "id": "235"}
    - slot{"id": "235"}
    - slot{"save_data": "save data"}
    - utter_Q1
* name{"name": "aman raj"}
    - slot{"name": "aman raj"}
    - utter_Q3
* designation{"post": "founder"}
    - slot{"post": "founder"}
    - utter_Q4
* dob{"birth": "19-02-1990"}
    - slot{"birth": "19-02-1990"}
    - action_save_dob
    - reset_slots
    - utter_anyother_help

## New Story_update_details_name_post
* greet
    - utter_greet
* update_data{"update": "promoted", "name": "kiran", "post": "cto"}
    - slot{"name": "kiran"}
    - slot{"update": "change data"}
    - slot{"post": "cto"}
    - action_update_name_post
    - utter_anyother_help

## New Story_update_details_Q1_name_post
* greet
    - utter_greet
* update_data{"update": "update"}
    - slot{"update": "update"}
    - utter_update_Q1
* update_data{"update": "promoted", "name": "kiran", "post": "cto"}
    - slot{"name": "kiran"}
    - slot{"update": "change data"}
    - slot{"post": "cto"}
    - action_update_name_post
    - utter_anyother_help

## interactive_story_update_details_Q1_name_post
* greet
    - utter_greet
* update_data{"update": "change data"}
    - slot{"update": "change data"}
    - utter_update_Q1
* update_data{"name": "kiran", "update": "change", "post": "cto"}
    - slot{"name": "kiran"}
    - slot{"post": "cto"}
    - slot{"update": "change"}
    - action_update_name_post
    - utter_anyother_help

## New Story_update_details_name_bday
* greet
    - utter_greet
* update_data{"update": "update", "name": "kumar saurav", "bday": "birthday", "birth": "19-04-1988"}
    - slot{"update": "update"}
    - slot{"name": "kumar saurav"}
    - slot{"bday": "birthday"}
    - slot{"birth": "19-04-1988"}
    - action_update_name_bday
    - utter_anyother_help

## New Story_update_details_Q1_name_bday
* greet
    - utter_greet
* update_data{"update": "update"}
    - slot{"update": "update"}
    - utter_update_Q1
* update_data{"update": "update", "name": "kumar saurav", "bday": "birthday", "birth": "19-04-1988"}
    - slot{"update": "update"}
    - slot{"name": "kumar saurav"}
    - slot{"bday": "birthday"}
    - slot{"birth": "19-04-1988"}
    - action_update_name_bday
    - utter_anyother_help

## New Story_update_details_name_id
* greet
    - utter_greet
* update_data{"update": "new", "name": "kumar saurav", "id_details": "employee id", "id": "232"}
    - slot{"update": "new"}
    - slot{"name": "kumar saurav"}
    - slot{"id_details": "employee id"}
    - slot{"id": "232"}
    - action_update_name_id
    - utter_anyother_help

## New Story_update_details_Q1_name_id
* greet
    - utter_greet
* update_data{"update": "update"}
    - slot{"update": "update"}
    - utter_update_Q1
* update_data{"update": "new", "name": "kumar saurav", "id_details": "employee id", "id": "232"}
    - slot{"update": "new"}
    - slot{"name": "kumar saurav"}
    - slot{"id_details": "employee id"}
    - slot{"id": "232"}
    - action_update_name_id
    - utter_anyother_help

## New Story_update_details_id_post
* greet
    - utter_greet
* update_data{"update": "promoted", "id": "222", "post": "cto"}
    - slot{"id": "222"}
    - slot{"update": "change data"}
    - slot{"post": "cto"}
    - action_update_id_post
    - utter_anyother_help

## New Story_update_details_Q1_id_post
* greet
    - utter_greet
* update_data{"update": "update"}
    - slot{"update": "update"}
    - utter_update_Q1
* update_data{"update": "promoted", "id": "222", "post": "cto"}
    - slot{"id": "222"}
    - slot{"update": "change data"}
    - slot{"post": "cto"}
    - action_update_id_post
    - utter_anyother_help

## New Story_update_details_id_bday
* greet
    - utter_greet
* update_data{"update": "update", "id": "222", "bday": "birthday", "birth": "07-02-1993"}
    - slot{"update": "update"}
    - slot{"id": "222"}
    - slot{"bday": "birthday"}
    - slot{"birth": "07-02-1993"}
    - action_update_id_bday
    - utter_anyother_help

## New Story_update_details_Q1_id_bday
* greet
    - utter_greet
* update_data{"update": "update"}
    - slot{"update": "update"}
    - utter_update_Q1
* update_data{"update": "update", "id": "222", "bday": "birthday", "birth": "07-02-1993"}
    - slot{"update": "update"}
    - slot{"id": "222"}
    - slot{"bday": "birthday"}
    - slot{"birth": "07-02-1993"}
    - action_update_id_bday
    - utter_anyother_help

## New Story_update_details_id_name
* greet
    - utter_greet
* update_data{"update": "now belongs", "id": "230", "id_details": "employee id", "name": "rakesh"}
    - slot{"update": "now belongs"}
    - slot{"name": "rakesh"}
    - slot{"id_details": "employee id"}
    - slot{"id": "232"}
    - action_update_id_name
    - utter_anyother_help

## New Story_update_details_Q1_id_name
* greet
    - utter_greet
* update_data{"update": "update"}
    - slot{"update": "update"}
    - utter_update_Q1
* update_data{"update": "now belongs", "id": "230", "id_details": "employee id", "name": "rakesh"}
    - slot{"update": "now belongs"}
    - slot{"name": "rakesh"}
    - slot{"id_details": "employee id"}
    - slot{"id": "232"}
    - action_update_id_name
    - utter_anyother_help

## interactive_story_1
* greet
    - utter_greet
* update_data{"update": "change data"}
    - slot{"update": "change data"}
    - utter_update_Q1
* update_data{"name": "kiran", "update": "change", "post": "cto"}
    - slot{"name": "kiran"}
    - slot{"post": "cto"}
    - slot{"update": "change"}
    - action_update_name_post
    - utter_anyother_help

## New Story_delete_details_Q1_name
* greet
    - utter_greet
* delete_data{"delete": "delete"}
    - slot{"delete": "delete"}
    - utter_delete
* update_data{"name": "kiran", "delete": "fired"}
    - slot{"name": "kiran"}
    - slot{"update": "fired"}
    - action_delete_name
    - utter_anyother_help

## New Story_delete_details_Q1_name_2
* greet
    - utter_greet
* update_data{"name": "kiran", "delete": "fired"}
    - slot{"name": "kiran"}
    - slot{"update": "fired"}
    - action_delete_name
    - utter_anyother_help

## New Story_delete_details_Q1_id
* greet
    - utter_greet
* delete_data{"delete": "delete"}
    - slot{"delete": "delete"}
    - utter_delete
* update_data{"id": "212", "delete": "left"}
    - slot{"id": "212"}
    - slot{"delete": "left"}
    - action_delete_id
    - utter_anyother_help

## New Story_delete_details_Q1_id_2
* greet
    - utter_greet
* update_data{"id": "212", "delete": "left"}
    - slot{"id": "212"}
    - slot{"delete": "left"}
    - action_delete_id
    - utter_anyother_help

## New Story

* greet
    - utter_greet
* delete_data{"delete":"delete"}
    - slot{"delete":"delete"}
    - utter_delete
* delete_data{"id":"213","delete":"fired"}
    - slot{"delete":"delete"}
    - slot{"delete":"fired"}
    - slot{"id":"213"}
    - action_delete_id
    - utter_anyother_help

## New Story

* greet
    - utter_greet
* delete_data{"id":"213","delete":"fired"}
    - slot{"delete":"fired"}
    - slot{"id":"213"}
    - action_delete_id
    - utter_anyother_help
