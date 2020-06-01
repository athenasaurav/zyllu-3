# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import AllSlotsReset
#
#
class ActionFetchDetailsName(Action):
#
    def name(self) -> Text:
        return "action_fetch_all_details_name"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())

        if tracker.get_slot("PERSON"):
            text = str(tracker.get_slot("PERSON"))
            text = text.lower()
            print(type(tracker.get_slot("PERSON")))
            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. The employee id is {} & is working as {}. Date of Birth registered with us is {}.".format(get[0], get[1], get[2], get[3]))
        elif tracker.get_slot("ORG"):
            text = str(tracker.get_slot("ORG"))
            text = text.lower()
            print(type(tracker.get_slot("ORG")))
            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. The employee id is {} & is working as {}. Date of Birth registered with us is {}.".format(get[0], get[1], get[2], get[3]))
        elif tracker.get_slot("NORP"):
            text = str(tracker.get_slot("NORP"))
            text = text.lower()
            print(type(tracker.get_slot("NORP")))
            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. The employee id is {} & is working as {}. Date of Birth registered with us is {}.".format(get[0], get[1], get[2], get[3]))
        
        return [AllSlotsReset()]


class ActionFetchIdDetailsName(Action):
#
    def name(self) -> Text:
        return "action_fetch_id_details_name"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        if tracker.get_slot("PERSON"):
            text = str(tracker.get_slot("PERSON"))
            text = text.lower()

            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. The employee id is {}.".format(get[0], get[1]))
        elif tracker.get_slot("ORG"):
            text = str(tracker.get_slot("ORG"))
            text = text.lower()

            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. The employee id is {}.".format(get[0], get[1]))
        elif tracker.get_slot("NORP"):
            text = str(tracker.get_slot("NORP"))
            text = text.lower()

            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. The employee id is {}.".format(get[0], get[1]))

        return [AllSlotsReset()]

class ActionFetchBdayDetailsName(Action):
#
    def name(self) -> Text:
        return "action_fetch_bday_details_name"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        if tracker.get_slot("PERSON"):
            text = str(tracker.get_slot("PERSON"))
            text = text.lower()

            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. Date of Birth registered with us is {}.".format(get[0], get[3]))
        elif tracker.get_slot("ORG"):
            text = str(tracker.get_slot("ORG"))
            text = text.lower()

            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. Date of Birth registered with us is {}.".format(get[0], get[3]))
        elif tracker.get_slot("NORP"):
            text = str(tracker.get_slot("NORP"))
            text = text.lower()

            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. Date of Birth registered with us is {}.".format(get[0], get[3]))


        return [AllSlotsReset()]

class ActionFetchDesgDetailsName(Action):
#
    def name(self) -> Text:
        return "action_fetch_desg_details_name"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        if tracker.get_slot("PERSON"):
            text = str(tracker.get_slot("PERSON"))
            text = text.lower()

            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. {} works with us as {}.".format(get[0], get[0], get[2]))
        elif tracker.get_slot("ORG"):
            text = str(tracker.get_slot("ORG"))
            text = text.lower()

            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. {} works with us as {}.".format(get[0], get[0], get[2]))
        elif tracker.get_slot("NORP"):
            text = str(tracker.get_slot("NORP"))
            text = text.lower()

            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. {} works with us as {}.".format(get[0], get[0], get[2]))
        return [AllSlotsReset()]

class ActionFetchDesgBdayDetailsName(Action):
#
    def name(self) -> Text:
        return "action_fetch_desg_bday_details_name"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
   
        if tracker.get_slot("PERSON"):
            text = str(tracker.get_slot("PERSON"))
            text = text.lower()

            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. {} works with us as {}. Date of Birth registered with us is {}".format(get[0], get[0], get[2], get[3]))
        elif tracker.get_slot("ORG"):
            text = str(tracker.get_slot("ORG"))
            text = text.lower()

            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. {} works with us as {}. Date of Birth registered with us is {}".format(get[0], get[0], get[2], get[3]))
        elif tracker.get_slot("NORP"):
            text = str(tracker.get_slot("NORP"))
            text = text.lower()

            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. {} works with us as {}. Date of Birth registered with us is {}".format(get[0], get[0], get[2], get[3]))
    
        return [AllSlotsReset()]

class ActionFetchIdBdayDetailsName(Action):
#
    def name(self) -> Text:
        return "action_fetch_id_bday_details_name"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
   
        if tracker.get_slot("PERSON"):
            text = str(tracker.get_slot("PERSON"))
            text = text.lower()

            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. {} employee code is {}. Date of Birth registered with us is {}".format(get[0], get[0], get[1], get[3]))
        elif tracker.get_slot("ORG"):
            text = str(tracker.get_slot("ORG"))
            text = text.lower()

            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. {} employee code is {}. Date of Birth registered with us is {}".format(get[0], get[0], get[1], get[3]))
        elif tracker.get_slot("NORP"):
            text = str(tracker.get_slot("NORP"))
            text = text.lower()

            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. {} employee code is {}. Date of Birth registered with us is {}".format(get[0], get[0], get[1], get[3]))
        
        return [AllSlotsReset()]

class ActionFetchIdDesgDetailsName(Action):
#
    def name(self) -> Text:
        return "action_fetch_id_desg_details_name"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        if tracker.get_slot("PERSON"):
            text = str(tracker.get_slot("PERSON"))
            text = text.lower()

            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. {} employee code is {} & designation is {}".format(get[0], get[0], get[1], get[2]))
        elif tracker.get_slot("ORG"):
            text = str(tracker.get_slot("ORG"))
            text = text.lower()

            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. {} employee code is {} & designation is {}".format(get[0], get[0], get[1], get[2]))
        elif tracker.get_slot("NORP"):
            text = str(tracker.get_slot("NORP"))
            text = text.lower()

            local_row = (data.loc[data['Name'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. {} employee code is {} & designation is {}".format(get[0], get[0], get[1], get[2]))
    
        return [AllSlotsReset()]

class ActionFetchDetailsId(Action):
#
    def name(self) -> Text:
        return "action_fetch_all_details_id"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        if str(tracker.get_slot("id")):
            text = int(tracker.get_slot("id"))
            text = text
            local_row = (data.loc[data['Employee_Code'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. The name of employee is {} & is working as {}. Date of Birth registered with us is {}.".format(get[1], get[0], get[2], get[3]))
        elif tracker.get_slot("CARDINAL"):
            text = str(tracker.get_slot("CARDINAL"))
            text = text.lower()
            local_row = (data.loc[data['Employee_Code'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. The name of employee is {} & is working as {}. Date of Birth registered with us is {}.".format(get[1], get[0], get[2], get[3]))

        return [AllSlotsReset()]

class ActionFetchNameDetailsId(Action):
#
    def name(self) -> Text:
        return "action_fetch_name_details_id"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        if str(tracker.get_slot("id")):
            text = int(tracker.get_slot("id"))
            text = text
            local_row = (data.loc[data['Employee_Code'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. The name of employee is {}.".format(get[1], get[0]))
        elif tracker.get_slot("CARDINAL"):
            text = str(tracker.get_slot("CARDINAL"))
            text = text.lower()
            local_row = (data.loc[data['Employee_Code'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. The name of employee is {}.".format(get[1], get[0]))
        return [AllSlotsReset()]

class ActionFetchBdayDetailsId(Action):
#
    def name(self) -> Text:
        return "action_fetch_bday_details_id"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet

        if str(tracker.get_slot("id")):
            text = int(tracker.get_slot("id"))
            text = text
            local_row = (data.loc[data['Employee_Code'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. The date of birth is {}.".format(get[1], get[3]))
        elif tracker.get_slot("CARDINAL"):
            text = str(tracker.get_slot("CARDINAL"))
            text = text.lower()
            local_row = (data.loc[data['Employee_Code'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. The date of birth is {}.".format(get[1], get[3]))
        return [AllSlotsReset()]


class ActionFetchDesgDetailsId(Action):
#
    def name(self) -> Text:
        return "action_fetch_desg_details_id"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        if str(tracker.get_slot("id")):
            text = int(tracker.get_slot("id"))
            text = text
            local_row = (data.loc[data['Employee_Code'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. {} works with us as {}.".format(get[0], get[0], get[2]))
        elif tracker.get_slot("CARDINAL"):
            text = str(tracker.get_slot("CARDINAL"))
            text = text.lower()
            local_row = (data.loc[data['Employee_Code'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. {} works with us as {}.".format(get[0], get[0], get[2]))
        return [AllSlotsReset()]

class ActionFetchNameBdayDetailsId(Action):
#
    def name(self) -> Text:
        return "action_fetch_name_bday_details_id"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        if str(tracker.get_slot("id")):
            text = int(tracker.get_slot("id"))
            text = text
            local_row = (data.loc[data['Employee_Code'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. The name of employee us {} & Date of Birth registered with us is {}.".format(get[0], get[1], get[3]))
        elif tracker.get_slot("CARDINAL"):
            text = str(tracker.get_slot("CARDINAL"))
            text = text.lower()
            local_row = (data.loc[data['Employee_Code'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. The name of employee us {} & Date of Birth registered with us is {}.".format(get[0], get[1], get[3]))
        return [AllSlotsReset()]

class ActionFetchDesgBdayDetailsId(Action):
#
    def name(self) -> Text:
        return "action_fetch_desg_bday_details_id"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        
        if str(tracker.get_slot("id")):
            text = int(tracker.get_slot("id"))
            text = text
            local_row = (data.loc[data['Employee_Code'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. {} is working with us as {} & Date of Birth registered with us is {}.".format(get[1], get[1], get[2], get[3]))
        elif tracker.get_slot("CARDINAL"):
            text = str(tracker.get_slot("CARDINAL"))
            text = text.lower()
            local_row = (data.loc[data['Employee_Code'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {}. {} is working with us as {} & Date of Birth registered with us is {}.".format(get[1], get[1], get[2], get[3]))
        return [AllSlotsReset()]

class ActionFetchDesgBdayDetailsId(Action):
#
    def name(self) -> Text:
        return "action_fetch_name_desg_details_id"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        if str(tracker.get_slot("id")):
            text = int(tracker.get_slot("id"))
            text = text
            local_row = (data.loc[data['Employee_Code'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {} & Date of Birth registered with us is {}.".format(get[1], get[3]))
        elif tracker.get_slot("CARDINAL"):
            text = str(tracker.get_slot("CARDINAL"))
            text = text.lower()
            local_row = (data.loc[data['Employee_Code'] == text].index[0])
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay you are looking for {} & Date of Birth registered with us is {}.".format(get[1], get[3]))

        return [AllSlotsReset()]


class ActionFetchDetailsPost(Action):
#
    def name(self) -> Text:
        return "action_fetch_all_details_post"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        text = str(tracker.get_slot("post"))
        text = text.lower()
        local_row = (data.loc[data['Designation'] == text].index[0])
        get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
        dispatcher.utter_message("okay you are looking for {}. The employee id is {} & is working as {}. Date of Birth registered with us is {}.".format(get[0], get[1], get[2], get[3]))
        return [AllSlotsReset()]

        
class ActionSaveDobDetails(Action):
#

    def name(self) -> Text:
        return "action_save_dob"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        if tracker.get_slot("PERSON"):
            if tracker.get_slot("id"):
                if tracker.get_slot("birth"):
                    name = str(tracker.get_slot("PERSON"))
                    name = name.lower()
                    employee_code = tracker.get_slot("id")
                    designation = str(tracker.get_slot("post"))
                    designation = designation.lower()
                    Date_of_Birth = tracker.get_slot("birth")
                    insertCell = [name, employee_code, designation, Date_of_Birth]
                    sheet.insert_row(insertCell, 2)
                    dispatcher.utter_message("All Saved! ☺")     
        elif tracker.get_slot("ORG"):
            if tracker.get_slot("id"):
                if tracker.get_slot("birth"):
                    name = str(tracker.get_slot("ORG"))
                    name = name.lower()
                    employee_code = tracker.get_slot("id")
                    designation = str(tracker.get_slot("post"))
                    designation = designation.lower()
                    Date_of_Birth = tracker.get_slot("birth")
                    insertCell = [name, employee_code, designation, Date_of_Birth]
                    sheet.insert_row(insertCell, 2)
                    dispatcher.utter_message("All Saved! ☺")  
        elif tracker.get_slot("NORP"):
            if tracker.get_slot("id"):
                if tracker.get_slot("birth"):
                    name = str(tracker.get_slot("NORP"))
                    name = name.lower()
                    employee_code = tracker.get_slot("id")
                    designation = str(tracker.get_slot("post"))
                    designation = designation.lower()
                    Date_of_Birth = tracker.get_slot("birth")
                    insertCell = [name, employee_code, designation, Date_of_Birth]
                    sheet.insert_row(insertCell, 2)
                    dispatcher.utter_message("All Saved! ☺")         
        elif tracker.get_slot("PERSON"):
            if tracker.get_slot("CARDINAL"):
                if tracker.get_slot("birth"):
                    name = str(tracker.get_slot("PERSON"))
                    name = name.lower()
                    employee_code = tracker.get_slot("CARDINAL")
                    designation = str(tracker.get_slot("post"))
                    designation = designation.lower()
                    Date_of_Birth = tracker.get_slot("birth")
                    insertCell = [name, employee_code, designation, Date_of_Birth]
                    sheet.insert_row(insertCell, 2)
                    dispatcher.utter_message("All Saved! ☺")  
        elif tracker.get_slot("ORG"):
            if tracker.get_slot("CARDINAL"):
                if tracker.get_slot("birth"):
                    name = str(tracker.get_slot("ORG"))
                    name = name.lower()
                    employee_code = tracker.get_slot("CARDINAL")
                    designation = str(tracker.get_slot("post"))
                    designation = designation.lower()
                    Date_of_Birth = tracker.get_slot("birth")
                    insertCell = [name, employee_code, designation, Date_of_Birth]
                    sheet.insert_row(insertCell, 2)
                    dispatcher.utter_message("All Saved! ☺")   
        elif tracker.get_slot("NORP"):
            if tracker.get_slot("CARDINAL"):
                if tracker.get_slot("birth"):
                    name = str(tracker.get_slot("NORP"))
                    name = name.lower()
                    employee_code = tracker.get_slot("CARDINAL")
                    designation = str(tracker.get_slot("post"))
                    designation = designation.lower()
                    Date_of_Birth = tracker.get_slot("birth")
                    insertCell = [name, employee_code, designation, Date_of_Birth]
                    sheet.insert_row(insertCell, 2)
                    dispatcher.utter_message("All Saved! ☺")  
        elif tracker.get_slot("PERSON"):
            if tracker.get_slot("id"):
                if tracker.get_slot("DATE"):
                    name = str(tracker.get_slot("PERSON"))
                    name = name.lower()
                    employee_code = tracker.get_slot("id")
                    designation = str(tracker.get_slot("post"))
                    designation = designation.lower()
                    Date_of_Birth = tracker.get_slot("DATE")
                    insertCell = [name, employee_code, designation, Date_of_Birth]
                    sheet.insert_row(insertCell, 2)
                    dispatcher.utter_message("All Saved! ☺") 
        elif tracker.get_slot("ORG"):
            if tracker.get_slot("id"):
                if tracker.get_slot("DATE"):
                    name = str(tracker.get_slot("ORG"))
                    name = name.lower()
                    employee_code = tracker.get_slot("idL")
                    designation = str(tracker.get_slot("post"))
                    designation = designation.lower()
                    Date_of_Birth = tracker.get_slot("DATE")
                    insertCell = [name, employee_code, designation, Date_of_Birth]
                    sheet.insert_row(insertCell, 2)
                    dispatcher.utter_message("All Saved! ☺") 
        elif tracker.get_slot("NORP"):
            if tracker.get_slot("id"):
                if tracker.get_slot("DATE"):
                    name = str(tracker.get_slot("NORP"))
                    name = name.lower()
                    employee_code = tracker.get_slot("id")
                    designation = str(tracker.get_slot("post"))
                    designation = designation.lower()
                    Date_of_Birth = tracker.get_slot("DATE")
                    insertCell = [name, employee_code, designation, Date_of_Birth]
                    sheet.insert_row(insertCell, 2)
                    dispatcher.utter_message("All Saved! ☺") 
        elif tracker.get_slot("PERSON"):
            if tracker.get_slot("CARDINAL"):
                if tracker.get_slot("DATE"):
                    name = str(tracker.get_slot("PERSON"))
                    name = name.lower()
                    employee_code = tracker.get_slot("CARDINAL")
                    designation = str(tracker.get_slot("post"))
                    designation = designation.lower()
                    Date_of_Birth = tracker.get_slot("DATE")
                    insertCell = [name, employee_code, designation, Date_of_Birth]
                    sheet.insert_row(insertCell, 2)
                    dispatcher.utter_message("All Saved! ☺")    
        elif tracker.get_slot("ORG"):
            if tracker.get_slot("CARDINAL"):
                if tracker.get_slot("DATE"):
                    name = str(tracker.get_slot("ORG"))
                    name = name.lower()
                    employee_code = tracker.get_slot("CARDINAL")
                    designation = str(tracker.get_slot("post"))
                    designation = designation.lower()
                    Date_of_Birth = tracker.get_slot("DATE")
                    insertCell = [name, employee_code, designation, Date_of_Birth]
                    sheet.insert_row(insertCell, 2)
                    dispatcher.utter_message("All Saved! ☺") 
        elif tracker.get_slot("NORP"):
            if tracker.get_slot("CARDINAL"):
                if tracker.get_slot("DATE"):
                    name = str(tracker.get_slot("NORP"))
                    name = name.lower()
                    employee_code = tracker.get_slot("CARDINAL")
                    designation = str(tracker.get_slot("post"))
                    designation = designation.lower()
                    Date_of_Birth = tracker.get_slot("DATE")
                    insertCell = [name, employee_code, designation, Date_of_Birth]
                    sheet.insert_row(insertCell, 2)
                    dispatcher.utter_message("All Saved! ☺") 

        return [AllSlotsReset()]

class ActionUpdateNamePostDetails(Action):
#

    def name(self) -> Text:
        return "action_update_name_post"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        if tracker.get_slot("PERSON"):
            name = str(tracker.get_slot("PERSON"))
            name = name.lower()
            designation = str(tracker.get_slot("post"))
            designation = designation.lower()
            local_row = (data.loc[data['Name'] == name].index[0])
            sheet.update_cell(local_row+2, 3, designation)
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay updated details for {} is as follows: The employee id is {} & is working now as {}. Date of Birth registered with us is {}.".format(get[0], get[1], get[2], get[3]))
        elif tracker.get_slot("ORG"):
            name = str(tracker.get_slot("ORG"))
            name = name.lower()
            designation = str(tracker.get_slot("post"))
            designation = designation.lower()
            local_row = (data.loc[data['Name'] == name].index[0])
            sheet.update_cell(local_row+2, 3, designation)
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay updated details for {} is as follows: The employee id is {} & is working now as {}. Date of Birth registered with us is {}.".format(get[0], get[1], get[2], get[3]))
        elif tracker.get_slot("NORP"):
            name = str(tracker.get_slot("NORP"))
            name = name.lower()
            designation = str(tracker.get_slot("post"))
            designation = designation.lower()
            local_row = (data.loc[data['Name'] == name].index[0])
            sheet.update_cell(local_row+2, 3, designation)
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay updated details for {} is as follows: The employee id is {} & is working now as {}. Date of Birth registered with us is {}.".format(get[0], get[1], get[2], get[3]))
                

        return [AllSlotsReset()]

class ActionUpdateNameBdayDetails(Action):
#

    def name(self) -> Text:
        return "action_update_name_bday"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())


        if tracker.get_slot("PERSON"):
            if tracker.get_slot("birth"):
                name = str(tracker.get_slot("PERSON"))
                name = name.lower()
                Date_of_Birth = tracker.get_slot("birth")
                local_row = (data.loc[data['Name'] == name].index[0])
                sheet.update_cell(local_row+2, 4, Date_of_Birth)
                get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
                dispatcher.utter_message("okay updated details for {} is as follows: The employee id is {} & is working as {}. Corrected Date of Birth registered with us is {}.".format(get[0], get[1], get[2], get[3]))
        elif tracker.get_slot("ORG"):
            if tracker.get_slot("birth"):
                name = str(tracker.get_slot("ORG"))
                name = name.lower()
                Date_of_Birth = tracker.get_slot("birth")
                local_row = (data.loc[data['Name'] == name].index[0])
                sheet.update_cell(local_row+2, 4, Date_of_Birth)
                get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
                dispatcher.utter_message("okay updated details for {} is as follows: The employee id is {} & is working as {}. Corrected Date of Birth registered with us is {}.".format(get[0], get[1], get[2], get[3]))
        elif tracker.get_slot("NORP"):
            if tracker.get_slot("birth"):
                name = str(tracker.get_slot("NORP"))
                name = name.lower()
                Date_of_Birth = tracker.get_slot("birth")
                local_row = (data.loc[data['Name'] == name].index[0])
                sheet.update_cell(local_row+2, 4, Date_of_Birth)
                get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
                dispatcher.utter_message("okay updated details for {} is as follows: The employee id is {} & is working as {}. Corrected Date of Birth registered with us is {}.".format(get[0], get[1], get[2], get[3]))
        elif tracker.get_slot("PERSON"):
            if tracker.get_slot("DATE"):
                name = str(tracker.get_slot("PERSON"))
                name = name.lower()
                Date_of_Birth = tracker.get_slot("DATE")
                local_row = (data.loc[data['Name'] == name].index[0])
                sheet.update_cell(local_row+2, 4, Date_of_Birth)
                get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
                dispatcher.utter_message("okay updated details for {} is as follows: The employee id is {} & is working as {}. Corrected Date of Birth registered with us is {}.".format(get[0], get[1], get[2], get[3]))
        elif tracker.get_slot("ORG"):
            if tracker.get_slot("DATE"):
                name = str(tracker.get_slot("ORG"))
                name = name.lower()
                Date_of_Birth = tracker.get_slot("DATE")
                local_row = (data.loc[data['Name'] == name].index[0])
                sheet.update_cell(local_row+2, 4, Date_of_Birth)
                get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
                dispatcher.utter_message("okay updated details for {} is as follows: The employee id is {} & is working as {}. Corrected Date of Birth registered with us is {}.".format(get[0], get[1], get[2], get[3]))
        elif tracker.get_slot("NORP"):
            if tracker.get_slot("DATE"):
                name = str(tracker.get_slot("NORP"))
                name = name.lower()
                Date_of_Birth = tracker.get_slot("DATE")
                local_row = (data.loc[data['Name'] == name].index[0])
                sheet.update_cell(local_row+2, 4, Date_of_Birth)
                get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
                dispatcher.utter_message("okay updated details for {} is as follows: The employee id is {} & is working as {}. Corrected Date of Birth registered with us is {}.".format(get[0], get[1], get[2], get[3]))
                

        return [AllSlotsReset()]

class ActionUpdateNameIdDetails(Action):
#

    def name(self) -> Text:
        return "action_update_name_id"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        if tracker.get_slot("PERSON"):
            name = str(tracker.get_slot("PERSON"))
            name = name.lower()
            employee_code = int(tracker.get_slot("id"))
            local_row = (data.loc[data['Name'] == name].index[0])
            sheet.update_cell(local_row+2, 2, employee_code)
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay updated details for {} is as follows: The employee id is now {} & is working as {}. Date of Birth registered with us is {}.".format(get[0], get[1], get[2], get[3]))
        elif tracker.get_slot("ORG"):
            name = str(tracker.get_slot("ORG"))
            name = name.lower()
            employee_code = int(tracker.get_slot("id"))
            local_row = (data.loc[data['Name'] == name].index[0])
            sheet.update_cell(local_row+2, 2, employee_code)
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay updated details for {} is as follows: The employee id is now {} & is working as {}. Date of Birth registered with us is {}.".format(get[0], get[1], get[2], get[3]))
        elif tracker.get_slot("NORP"):
            name = str(tracker.get_slot("NORP"))
            name = name.lower()
            employee_code = int(tracker.get_slot("id"))
            local_row = (data.loc[data['Name'] == name].index[0])
            sheet.update_cell(local_row+2, 2, employee_code)
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay updated details for {} is as follows: The employee id is now {} & is working as {}. Date of Birth registered with us is {}.".format(get[0], get[1], get[2], get[3]))
   
        return [AllSlotsReset()]

class ActionUpdateIdNameDetails(Action):
#

    def name(self) -> Text:
        return "action_update_id_name"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        if tracker.get_slot("PERSON"):
            name = str(tracker.get_slot("PERSON"))
            name = name.lower()
            employee_code = int(tracker.get_slot("id"))
            local_row = (data.loc[data['Employee_Code'] == employee_code].index[0])
            sheet.update_cell(local_row+2, 1, name)
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay updated details for {} is as follows: The name is now {} & is working as {}. Date of Birth registered with us is {}.".format(get[1], get[0], get[2], get[3]))
        elif tracker.get_slot("ORG"):
            name = str(tracker.get_slot("ORG"))
            name = name.lower()
            employee_code = int(tracker.get_slot("id"))
            local_row = (data.loc[data['Employee_Code'] == employee_code].index[0])
            sheet.update_cell(local_row+2, 1, name)
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay updated details for {} is as follows: The name is now {} & is working as {}. Date of Birth registered with us is {}.".format(get[1], get[0], get[2], get[3]))
        elif tracker.get_slot("NORP"):
            name = str(tracker.get_slot("NORP"))
            name = name.lower()
            employee_code = int(tracker.get_slot("id"))
            local_row = (data.loc[data['Employee_Code'] == employee_code].index[0])
            sheet.update_cell(local_row+2, 1, name)
            get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
            dispatcher.utter_message("okay updated details for {} is as follows: The name is now {} & is working as {}. Date of Birth registered with us is {}.".format(get[1], get[0], get[2], get[3]))

        return [AllSlotsReset()]

class ActionUpdateIdPostDetails(Action):
#

    def name(self) -> Text:
        return "action_update_id_post"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        employee_code = int(tracker.get_slot("id"))
        designation = str(tracker.get_slot("post"))
        designation = designation.lower()
        local_row = (data.loc[data['Employee_Code'] == employee_code].index[0])
        sheet.update_cell(local_row+2, 3, designation)
        get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
        dispatcher.utter_message("okay updated details for {} is as follows: {}  is now working as {}. Date of Birth registered with us is {}.".format(get[1], get[0], get[2], get[3]))
 

        return [AllSlotsReset()]

class ActionUpdateIdBdayDetails(Action):
#

    def name(self) -> Text:
        return "action_update_id_bday"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        employee_code = int(tracker.get_slot("id"))
        Date_of_Birth = tracker.get_slot("birth")
        local_row = (data.loc[data['Employee_Code'] == employee_code].index[0])
        sheet.update_cell(local_row+2, 4, Date_of_birth)
        get = sheet.row_values(local_row+2, value_render_option='FORMATTED_VALUE')
        dispatcher.utter_message("okay updated details for {} is as follows: {}  is working as {}. Corrected Date of Birth registered with us is {}.".format(get[1], get[0], get[2], get[3]))
 

        return [AllSlotsReset()]

class ActionDeleteNameDetails(Action):
#

    def name(self) -> Text:
        return "action_delete_name"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        if tracker.get_slot("PERSON"):
            name = str(tracker.get_slot("PERSON"))
            name = name.lower()
            local_row = (data.loc[data['Name'] == name].index[0])
            local_row = int(local_row)
            local_row = local_row+2
            sheet.delete_rows(local_row)
            dispatcher.utter_message("Done!! Removed from my Database")
        elif tracker.get_slot("ORG"):
            name = str(tracker.get_slot("ORG"))
            name = name.lower()
            local_row = (data.loc[data['Name'] == name].index[0])
            local_row = int(local_row)
            local_row = local_row+2
            sheet.delete_rows(local_row)
            dispatcher.utter_message("Done!! Removed from my Database")
        elif tracker.get_slot("NORP"):
            name = str(tracker.get_slot("NORP"))
            name = name.lower()
            local_row = (data.loc[data['Name'] == name].index[0])
            local_row = int(local_row)
            local_row = local_row+2
            sheet.delete_rows(local_row)
            dispatcher.utter_message("Done!! Removed from my Database")
 

        return [AllSlotsReset()]


class ActionDeleteIdDetails(Action):
#

    def name(self) -> Text:
        return "action_delete_id"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        employee_code = int(tracker.get_slot("id"))
        id = int(tracker.get_slot("id"))
        local_row = (data.loc[data['Employee_Code'] == id].index[0])
        local_row = int(local_row)
        local_row = local_row+2
        sheet.delete_rows(local_row)
        dispatcher.utter_message("Done!! Removed from my Database")
 

        return [AllSlotsReset()]


class ActionFetchAllName(Action):
#

    def name(self) -> Text:
        return "action_fetch_all_name"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        all_names = tracker.get_slot("all_names")
        dispatcher.utter_message("Okay! i have following people in my Database, Serial wise : ")
        a = str(data.iloc[:,0])
        print(a)
        dispatcher.utter_message(a)
 
        return [AllSlotsReset()]

class ActionFetchAllId(Action):
#

    def name(self) -> Text:
        return "action_fetch_all_id"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        import json
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Challenge").sheet1 # Open the spreadhseet
        data = pd.DataFrame(sheet.get_all_records())
        all_id = tracker.get_slot("all_id")
        dispatcher.utter_message("Okay! i have following ids in my Database, Serial wise : ")
        b = str(data.iloc[:,1])
        print(b)
        dispatcher.utter_message(b)
 

        return [AllSlotsReset()]