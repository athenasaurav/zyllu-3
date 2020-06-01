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
* fetch_details_name_all{"details":"all details","PERSON":"kumar saurav"}
    - slot{"details":"all details"}
    - slot{"PERSON":"kumar saurav"}
    - action_fetch_all_details_name
    - utter_anyother_help

## New Story_fetch_details_name_id

* greet
    - utter_greet
* fetch_details_name_id{"id_details":"employee id","id":"32100"}
    - slot{"id_details":"employee code"}
    - slot{"id":"32100"}
    - action_fetch_all_details_id
    - utter_anyother_help
* fetch_details_name_id{"id_details":"employee code","PERSON":"aman raj"}
    - slot{"id_details":"employee code"}
    - slot{"PERSON":"aman raj"}
    - action_fetch_all_details_post
    - utter_anyother_help

## New Story_fetch_details_name_id

* greet
    - utter_greet
* fetch_details_name_id{"id_details":"employee id","PERSON":"kumar saurav"}
    - slot{"id_details":"employee id"}
    - slot{"PERSON":"kumar saurav"}
    - action_fetch_id_details_name
    - utter_anyother_help
* fetch_details_name_id{"id_details":"employee id","PERSON":"jasmine"}
    - slot{"id_details":"employee id"}
    - slot{"PERSON":"jasmine"}
    - action_fetch_id_details_name
    - utter_anyother_help
* fetch_details_name_id{"id_details":"employee id","PERSON":"aman raj"}
    - slot{"id_details":"employee id"}
    - slot{"PERSON":"jasmine"}
    - action_fetch_id_details_name
    - utter_anyother_help

## New Story_fetch_details_name_bday

* greet
    - utter_greet
* fetch_details_name_bday{"bday":"birthday","PERSON":"kumar saurav"}
    - slot{"bday":"birthday"}
    - slot{"PERSON":"kumar saurav"}
    - action_fetch_bday_details_name
    - utter_anyother_help
* fetch_details_name_bday{"bday":"bday","PERSON":"jasmine"}
    - slot{"bday":"bday"}
    - slot{"PERSON":"jasmine"}
    - action_fetch_bday_details_name
    - utter_anyother_help
* fetch_details_name_bday{"bday":"date of birth","PERSON":"aman raj"}
    - slot{"bday":"date of birth"}
    - slot{"PERSON":"jasmine"}
    - action_fetch_bday_details_name
    - utter_anyother_help

## New Story_fetch_details_name_designation

* greet
    - utter_greet
* fetch_details_name_bday{"desg_details":"designation","PERSON":"kumar saurav"}
    - slot{"desg_details":"designation"}
    - slot{"PERSON":"kumar saurav"}
    - action_fetch_desg_details_name
    - utter_anyother_help
* fetch_details_name_bday{"desg_details":"post","PERSON":"jasmine"}
    - slot{"desg_details":"post"}
    - slot{"PERSON":"jasmine"}
    - action_fetch_desg_details_name
    - utter_anyother_help
* fetch_details_name_bday{"desg_details":"work profile","PERSON":"aman raj"}
    - slot{"desg_details": "work profile"}
    - slot{"PERSON":"jasmine"}
    - action_fetch_desg_details_name
    - utter_anyother_help

## New Story_fetch_details_name_designation_bday

* greet
    - utter_greet
* fetch_details_name_bday{"desg_details":"designation","bday":"birthday","PERSON":"kumar saurav"}
    - slot{"desg_details":"designation"}
    - slot{"bday":"birthday"}
    - slot{"PERSON":"kumar saurav"}
    - action_fetch_desg_bday_details_name
    - utter_anyother_help
* fetch_details_name_bday{"desg_details":"post","bday":"bday","PERSON":"jasmine"}
    - slot{"desg_details":"post"}
    - slot{"bday":"bday"}
    - slot{"PERSON":"jasmine"}
    - action_fetch_desg_bday_details_name
    - utter_anyother_help
* fetch_details_name_bday{"desg_details":"work profile","bday":"date of birth","PERSON":"aman raj"}
    - slot{"desg_details": "work profile"}
    - slot{"bday":"date of birth"}
    - slot{"PERSON":"jasmine"}
    - action_fetch_desg_bday_details_name
    - utter_anyother_help

## New Story_fetch_details_name_id_bday

* greet
    - utter_greet
* fetch_details_name_bday{"id_details":"employee id","bday":"birthday","PERSON":"kumar saurav"}
    - slot{"id_details":"employee id"}
    - slot{"bday":"birthday"}
    - slot{"PERSON":"kumar saurav"}
    - action_fetch_id_bday_details_name
    - utter_anyother_help
* fetch_details_name_bday{"id_details":"employee id","bday":"bday","PERSON":"jasmine"}
    - slot{"id_details":"employee id"}
    - slot{"bday":"bday"}
    - slot{"PERSON":"jasmine"}
    - action_fetch_id_bday_details_name
    - utter_anyother_help
* fetch_details_name_bday{"id_details":"employee id","bday":"date of birth","PERSON":"aman raj"}
    - slot{"id_details":"employee id"}
    - slot{"bday":"date of birth"}
    - slot{"PERSON":"jasmine"}
    - action_fetch_id_bday_details_name
    - utter_anyother_help

## New Story_fetch_details_name_id_designation

* greet
    - utter_greet
* fetch_details_name_bday{"id_details":"employee id","desg_details":"designation","PERSON":"kumar saurav"}
    - slot{"id_details":"employee id"}
    - slot{"desg_details":"designation"}
    - slot{"PERSON":"kumar saurav"}
    - action_fetch_id_desg_details_name
    - utter_anyother_help
* fetch_details_name_bday{"id_details":"employee id","desg_details":"post","PERSON":"jasmine"}
    - slot{"id_details":"employee id"}
    - slot{"desg_details":"post"}
    - slot{"PERSON":"jasmine"}
    - action_fetch_id_desg_details_name
    - utter_anyother_help
* fetch_details_name_bday{"id_details":"employee id","desg_details":"work profile","PERSON":"aman raj"}
    - slot{"id_details":"employee id"}
    - slot{"desg_details":"work profile"}
    - slot{"PERSON":"jasmine"}
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
* fetch_details_id_name{"names":"PERSON","id":"214"}
    - slot{"names":"PERSON"}
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

## New Story_fetch_details_id_name

* greet
    - utter_greet
* fetch_details_id_name{"names":"PERSON","id":"214"}
    - slot{"names":"PERSON"}
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
* fetch_details_id_name_bday{"id_details":"employee id","bday":"born","names":"PERSON"}
    - slot{"id_details":"employee id"}
    - slot{"bday":"born"}
    - slot{"names":"PERSON"}
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
* fetch_details_id_designation_name{"id_details":"employee id","desg_details":"post","names":"PERSON"}
    - slot{"id_details":"employee id"}
    - slot{"desg_details":"post"}
    - slot{"names":"PERSON"}
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
* save_data{"save_data": "save his data", "PERSON": "Kumar Saurav"}
  - slot{"save_data": "save his data"}
  - slot{"PERSON": "Kumar Saurav"}
  - utter_Q2
* employee_id{"save_data": "save his data", "PERSON": "Kumar Saurav", "id": "222"}
  - slot{"save_data": "save his data"}
  - slot{"PERSON": "Kumar Saurav"}
  - slot{"id": "222"}
  - utter_Q3
* designation{"save_data": "save his data", "PERSON": "Kumar Saurav", "id": "222", "post": "Director"}
  - slot{"save_data": "save his data"}
  - slot{"PERSON": "Kumar Saurav"}
  - slot{"id": "222"}
  - slot{"post": "Director"}
  - utter_Q4
* dob{"save_data": "save his data", "PERSON": "Kumar Saurav", "id": "222", "post": "Director", "birth": "19-07-1992"}
  - slot{"save_data": "save his data"}
  - slot{"PERSON": "Kumar Saurav"}
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
* name{"save_data": "save his data", "id": "212", "PERSON": "Kumar Saurav"}
  - slot{"save_data": "save his data"}
  - slot{"id": "212"}
  - slot{"PERSON": "Kumar Saurav"}
  - utter_Q3
* designation{"save_data": "save his data", "id": "212","PERSON": "Kumar Saurav", "post": "Director"}
  - slot{"save_data": "save his data"}
  - slot{"id": "222"}
  - slot{"PERSON": "Kumar Saurav"}
  - slot{"post": "Director"}
  - utter_Q4
* dob{"save_data": "save his data", "id": "222","PERSON": "Kumar Saurav", "post": "Director", "birth": "19-07-1992"}
  - slot{"save_data": "save his data"}
  - slot{"PERSON": "Kumar Saurav"}
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
* name{"save_data": "save his data", "PERSON": "Kumar Saurav"}
  - slot{"save_data": "save his data"}
  - slot{"PERSON": "Kumar Saurav"}
  - utter_Q2
* employee_id{"save_data": "save his data", "PERSON": "Kumar Saurav", "id": "222"}
  - slot{"save_data": "save his data"}
  - slot{"PERSON": "Kumar Saurav"}
  - slot{"id": "222"}
  - utter_Q3
* designation{"save_data": "save his data", "PERSON":"Kumar Saurav", "id": "222", "post":"Director"}
  - slot{"save_data":"save his data"}
  - slot{"PERSON":"Kumar Saurav"}
  - slot{"id":"222"}
  - slot{"post":"Director"}
  - utter_Q4
* dob{"save_data": "save his data", "PERSON": "Kumar Saurav", "id": "222", "post": "Director", "birth":"19-07-1992"}
  - slot{"save_data": "save his data"}
  - slot{"PERSON": "Kumar Saurav"}
  - slot{"id": "222"}
  - slot{"post": "Director"}
  - slot{"birth": "19-07-1992"}
  - action_save_dob
  - utter_anyother_help

## interactive_story_save_details_all
* greet
    - utter_greet
* save_data{"save_data": "save data", "PERSON": "kiran"}
    - slot{"PERSON": "kiran"}
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
* name{"PERSON": "aman raj"}
    - slot{"PERSON": "aman raj"}
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
* update_data{"update": "promoted", "PERSON": "kiran", "post": "cto"}
    - slot{"PERSON": "kiran"}
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
* update_data{"update": "promoted", "PERSON": "kiran", "post": "cto"}
    - slot{"PERSON": "kiran"}
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
* update_data{"PERSON": "kiran", "update": "change", "post": "cto"}
    - slot{"PERSON": "kiran"}
    - slot{"post": "cto"}
    - slot{"update": "change"}
    - action_update_name_post
    - utter_anyother_help

## New Story_update_details_name_bday
* greet
    - utter_greet
* update_data{"update": "update", "PERSON": "kumar saurav", "bday": "birthday", "birth": "19-04-1988"}
    - slot{"update": "update"}
    - slot{"PERSON": "kumar saurav"}
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
* update_data{"update": "update", "PERSON": "kumar saurav", "bday": "birthday", "birth": "19-04-1988"}
    - slot{"update": "update"}
    - slot{"PERSON": "kumar saurav"}
    - slot{"bday": "birthday"}
    - slot{"birth": "19-04-1988"}
    - action_update_name_bday
    - utter_anyother_help

## New Story_update_details_name_id
* greet
    - utter_greet
* update_data{"update": "new", "PERSON": "kumar saurav", "id_details": "employee id", "id": "232"}
    - slot{"update": "new"}
    - slot{"PERSON": "kumar saurav"}
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
* update_data{"update": "new", "PERSON": "kumar saurav", "id_details": "employee id", "id": "232"}
    - slot{"update": "new"}
    - slot{"PERSON": "kumar saurav"}
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
* update_data{"update": "now belongs", "id": "230", "id_details": "employee id", "PERSON": "rakesh"}
    - slot{"update": "now belongs"}
    - slot{"PERSON": "rakesh"}
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
* update_data{"update": "now belongs", "id": "230", "id_details": "employee id", "PERSON": "rakesh"}
    - slot{"update": "now belongs"}
    - slot{"PERSON": "rakesh"}
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
* update_data{"PERSON": "kiran", "update": "change", "post": "cto"}
    - slot{"PERSON": "kiran"}
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
* update_data{"PERSON": "kiran", "delete": "fired"}
    - slot{"PERSON": "kiran"}
    - slot{"update": "fired"}
    - action_delete_name
    - utter_anyother_help

## New Story_delete_details_Q1_name_2
* greet
    - utter_greet
* update_data{"PERSON": "kiran", "delete": "fired"}
    - slot{"PERSON": "kiran"}
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

## New Story_fetch_details_all_names

* greet
    - utter_greet
* fetch_names{"all_names":"fetch all the names"}
    - slot{"all_names":"fetch all the names"}
    - action_fetch_all_name
    - utter_anyother_help

## New Story_fetch_details_all_names


* fetch_names{"all_names":"names of all the employee"}
    - slot{"all_names":"names of all the employee"}
    - action_fetch_all_name
    - utter_anyother_help

## New Story_fetch_details_all_names


* fetch_names{"all_names":"names of all the employee"}
    - slot{"all_names":"names of all the employee"}
    - action_fetch_all_name
    - utter_anyother_help


## New Story_fetch_details_all_id

* greet
    - utter_greet
* fetch_ids{"all_id":"all the id saved"}
    - slot{"all_id":"all the id saved"}
    - action_fetch_all_id
    - utter_anyother_help

## New Story_fetch_details_all_names


* fetch_ids{"all_id":"id details of all employees"}
    - slot{"all_id":"id details of all employees"}
    - action_fetch_all_id
    - utter_anyother_help

## New Story


* fetch_ids{"all_names":"all the id saved"}
    - slot{"all_names":"all the id saved"}
    - action_fetch_all_name
    - utter_anyother_help

## interactive_story_1
* fetch_details_name_all{"details": "details", "PERSON": "ARYA"}
    - slot{"PERSON": "ARYA"}
    - slot{"details": "details"}
    - action_fetch_all_details_name
    - reset_slots
    - utter_anyother_help
* fetch_details_name_all{"details": "details", "PERSON": "robin benedict Luba"}
    - slot{"PERSON": "robin benedict Luba"}
    - slot{"details": "details"}
    - action_fetch_all_details_name
    - reset_slots
    - utter_anyother_help
* fetch_details_name_all{"details": "details", "PERSON": "GANESH ANAND"}
    - slot{"PERSON": "GANESH ANAND"}
    - slot{"details": "details"}
    - action_fetch_all_details_name
    - reset_slots
    - utter_anyother_help
* fetch_details_name_id_bday{"id_details": "id", "bday": "bday", "PERSON": "RAGHAV"}
    - slot{"PERSON": "RAGHAV"}
    - slot{"bday": "bday"}
    - slot{"id_details": "id"}
    - action_fetch_id_bday_details_name
    - reset_slots
    - utter_anyother_help
* fetch_details_name_designation_bday{"desg_details": "designation", "bday": "bday", "PERSON": "RAGHAV"}
    - slot{"PERSON": "RAGHAV"}
    - slot{"bday": "bday"}
    - slot{"desg_details": "designation"}
    - action_fetch_desg_bday_details_name
    - reset_slots
    - utter_anyother_help
* fetch_details_id_all{"details": "details", "id": "223", "CARDINAL": "223"}
    - slot{"details": "details"}
    - slot{"id": "223"}
    - action_fetch_all_details_id
    - reset_slots
    - utter_anyother_help
* fetch_details_id_designation{"desg_details": "designation", "id": "221", "CARDINAL": "221"}
    - slot{"desg_details": "designation"}
    - slot{"id": "221"}
    - action_fetch_desg_details_id
    - reset_slots
    - utter_anyother_help
* fetch_details_name_id{"id_details": "employee id", "PERSON": "Jasmine"}
    - slot{"PERSON": "Jasmine"}
    - slot{"id_details": "employee id"}
    - action_fetch_id_details_name
    - reset_slots
    - utter_anyother_help
* fetch_details_id_all{"details": "all details", "id": "3210"}
    - slot{"details": "all details"}
    - slot{"id": "3210"}
    - action_fetch_all_details_id
    - reset_slots
    - utter_anyother_help
* fetch_details_name_designation_bday{"desg_details": "profile", "bday": "date of birth", "PERSON": "Jyoti"}
    - slot{"PERSON": "Jyoti"}
    - slot{"bday": "date of birth"}
    - slot{"desg_details": "profile"}
    - action_fetch_desg_bday_details_name
    - reset_slots
    - utter_anyother_help
* fetch_details_name_designation{"desg_details": "work profile", "PERSON": "bablu dablu yadav"}
    - slot{"PERSON": "bablu dablu yadav"}
    - slot{"desg_details": "work profile"}
    - action_fetch_desg_details_name
    - reset_slots
    - utter_anyother_help
* fetch_details_name_designation{"desg_details": "designation", "PERSON": "saloni bhutta"}
    - slot{"PERSON": "saloni bhutta"}
    - slot{"desg_details": "designation"}
    - action_fetch_desg_details_name
    - reset_slots
    - utter_anyother_help
* fetch_details_id_name{"names": "name", "id": "93"}
    - slot{"id": "93"}
    - slot{"names": "name"}
    - action_fetch_name_details_id
    - reset_slots
    - utter_anyother_help
* fetch_details_name_bday{"bday": "bday", "PERSON": "chung-ae"}
    - slot{"PERSON": "chung-ae"}
    - slot{"bday": "bday"}
    - action_fetch_bday_details_name
    - reset_slots
    - utter_anyother_help
* fetch_details_id_designation_bday{"desg_details": "designation", "bday": "birthday", "id": "32100"}
    - slot{"bday": "birthday"}
    - slot{"desg_details": "designation"}
    - slot{"id": "32100"}
    - action_fetch_desg_bday_details_id
    - reset_slots
    - utter_anyother_help
* save_data{"save_data": "save", "PERSON": "Prathmesh Karmarkar"}
    - slot{"PERSON": "Prathmesh Karmarkar"}
    - slot{"save_data": "save"}
    - utter_Q2
* employee_id{"id": "1712", "CARDINAL": "1712"}
    - slot{"id": "1712"}
    - utter_Q3
* designation{"post": "Interim CEO"}
    - slot{"post": "Interim CEO"}
    - utter_Q4
* dob{"birth": "19-01-1941", "DATE": "19-01-1941"}
    - slot{"birth": "19-01-1941"}
    - action_save_dob
    - utter_anyother_help
* save_data{"save_data": "save details", "PERSON": "Kissy Khisiyani"}
    - slot{"PERSON": "Kissy Khisiyani"}
    - slot{"save_data": "save details"}
    - utter_Q2
* employee_id{"id": "932", "CARDINAL": "932"}
    - slot{"id": "932"}
    - utter_Q3
* designation{"post": "Interim CEO"}
    - slot{"post": "Interim CEO"}
    - utter_Q4
* dob{"birth": "31-01-1956", "DATE": "31-01-1956"}
    - slot{"birth": "31-01-1956"}
    - action_save_dob
    - reset_slots
    - utter_anyother_help
* update_data{"PERSON": "kissy khisiyani", "update": "promoted", "post": "manager"}
    - slot{"PERSON": "kissy khisiyani"}
    - slot{"post": "manager"}
    - slot{"update": "promoted"}
    - action_update_name_post
    - reset_slots
    - utter_anyother_help
* update_data{"PERSON": "kissy khisiyani", "update": "promoted", "post": "manager"}
    - slot{"PERSON": "kissy khisiyani"}
    - slot{"post": "manager"}
    - slot{"update": "promoted"}
    - action_update_name_post
    - reset_slots
    - utter_anyother_help
* update_data{"update": "promoted", "post": "accountant", "PERSON": "kissy khisiyani"}
    - slot{"PERSON": "kissy khisiyani"}
    - slot{"post": "accountant"}
    - slot{"update": "promoted"}
    - action_update_name_post
    - reset_slots
    - utter_anyother_help
* update_data{"update": "update", "bday": "bday", "PERSON": "saloni bhutta"}
    - slot{"PERSON": "saloni bhutta"}
    - slot{"bday": "bday"}
    - slot{"update": "update"}
    - utter_update_Q1
* update_data{"update": "change", "bday": "bday", "birth": "17-11-1992", "CARDINAL": "17-11-1992"}
    - slot{"bday": "bday"}
    - slot{"birth": "17-11-1992"}
    - slot{"update": "change"}
    - action_update_name_bday
    - reset_slots
    - utter_anyother_help
* update_data{"update": "update", "id_details": "employee code", "PERSON": "Chung-ae", "id": "232", "CARDINAL": "232"}
    - slot{"PERSON": "Chung-ae"}
    - slot{"id": "232"}
    - slot{"id_details": "employee code"}
    - slot{"update": "update"}
    - action_update_name_id
    - utter_anyother_help
* update_data{"update": "update", "id_details": "employee code", "PERSON": "chung-ae", "id": "254", "CARDINAL": "254"}
    - slot{"PERSON": "chung-ae"}
    - slot{"id": "254"}
    - slot{"id_details": "employee code"}
    - slot{"update": "update"}
    - action_update_name_id
    - utter_anyother_help
* update_data{"update": "update", "id_details": "employee id", "id": "350", "PERSON": "ganesh anand", "CARDINAL": "350"}
    - slot{"PERSON": "ganesh anand"}
    - slot{"id": "350"}
    - slot{"id_details": "employee id"}
    - slot{"update": "update"}
    - action_update_name_id
    - utter_anyother_help
* update_data{"update": "update", "desg_details": "designation", "PERSON": "ganesh anand", "post": "ceo"}
    - slot{"PERSON": "ganesh anand"}
    - slot{"desg_details": "designation"}
    - slot{"post": "ceo"}
    - slot{"update": "update"}
    - action_update_name_post
    - reset_slots
    - utter_anyother_help
* update_data{"update": "update", "id_details": "employee id", "id": "350", "PERSON": "ganesh anand", "CARDINAL": "350"}
    - slot{"PERSON": "ganesh anand"}
    - slot{"id": "350"}
    - slot{"id_details": "employee id"}
    - slot{"update": "update"}
    - action_update_name_id
    - utter_anyother_help
* update_data{"update": "update", "id_details": "employee id", "PERSON": "shakeela"}
    - slot{"PERSON": "shakeela"}
    - slot{"id_details": "employee id"}
    - slot{"update": "update"}
    - action_update_name_id
    - reset_slots
    - utter_anyother_help
* delete_data{"delete": "remove information", "id": "211", "CARDINAL": "about 211"}
    - slot{"delete": "remove information"}
    - slot{"id": "211"}
    - action_delete_id
    - reset_slots
    - utter_anyother_help
* fetch_details_name_all{"details": "details", "PERSON": "Bablu dablu yadav"}
    - slot{"PERSON": "Bablu dablu yadav"}
    - slot{"details": "details"}
    - action_fetch_all_details_name
    - reset_slots
    - utter_anyother_help
* fetch_details_name_all{"details": "details", "PERSON": "saloni bhutta"}
    - slot{"PERSON": "saloni bhutta"}
    - slot{"details": "details"}
    - action_fetch_all_details_name
    - reset_slots
    - utter_anyother_help
* fetch_details_id_all{"details": "details", "id": "32100"}
    - slot{"details": "details"}
    - slot{"id": "32100"}
    - action_fetch_all_details_id
    - reset_slots
    - utter_anyother_help
* fetch_details_name_all{"details": "details", "PERSON": "bablu dablu yadav"}
    - slot{"PERSON": "bablu dablu yadav"}
    - slot{"details": "details"}
    - action_fetch_all_details_name
    - reset_slots
    - utter_anyother_help
* fetch_details_id_bday{"bday": "bday", "id": "350", "CARDINAL": "350"}
    - slot{"bday": "bday"}
    - slot{"id": "350"}
    - action_fetch_bday_details_id
    - reset_slots
    - utter_anyother_help
* fetch_details_id_bday{"bday": "bday", "details": "details", "id": "221", "CARDINAL": "221"}
    - slot{"bday": "bday"}
    - slot{"details": "details"}
    - slot{"id": "221"}
    - action_fetch_bday_details_id
    - reset_slots
    - utter_anyother_help
