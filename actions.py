from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.forms import FormAction, FormField 

import pandas as pd
import string

# EntityFormField(entity_name, slot_name), which will look for an entity called entity_name to fill a slot slot_name.
# BooleanFormField(slot_name, affirm_intent, deny_intent), which looks for the intents affirm_intent and deny_intent to fill a boolean slot called slot_name.
# FreeTextFormField(slot_name) : which will use the next user utterance to fill the text slot slot_name
class CustomFormField(FormField):
    # noinspection PyMethodMayBeStatic
    def validate(self, entity, value):
        """Check if extracted value for a requested slot is valid.
        Users should override this to implement custom validation logic,
        returning None indicates a negative validation result, and the slot
        will not be set.
        """
        df = pd.read_excel('SampleModelSerialGEA.xlsx')
        print(entity, value)
        if entity == 'appliance':      ###IMP :: can reduce appliance value to one allowed here
            print('Checking')
            if value not in ['refrigerator', 'fridge', 'freezer', 'dishwasher', 'wall oven', 'microwave',
                             'washer', 'dryer', 'air conditioner', 'ac']:
                print('error')
                value = None
        
        if entity == 'modelnumber':
            print('Checking')
            if not any(df.loc[:, 'Model Number'] == value.upper()):
                print('error')
                value = None

        if entity == 'serialnumber':
            print('Checking')
            if not any(df.loc[:, 'Serial Number'] == value.upper()):
                print('error')
                value = None

        return value


class BooleanFormField(CustomFormField):
    """A form field that prompts the user for a yes or no answer.
    The interpreter should map positive and negative answers to
    the intents ``affirm_intent`` and ``deny_intent``.
    """

    def __init__(self, slot_name, affirm_intent, deny_intent):
        self.slot_name = slot_name
        self.affirm_intent = affirm_intent
        self.deny_intent = deny_intent

    def extract(self, tracker):
        # type: (Tracker) -> List[EventType]

        intent = tracker.latest_message.get("intent", {}).get("name")
        if intent == self.affirm_intent:
            value = True
        elif intent == self.deny_intent:
            value = False
        else:
            return []

        return [SlotSet(self.slot_name, value)]


class FreeTextFormField(CustomFormField):

    def __init__(self, slot_name):
        self.slot_name = slot_name

    def extract(self, tracker):
        # type: (Tracker) -> List[EventType]

        print(tracker.latest_message)

        events_custom = []
        
        for entity in tracker.latest_message.get("entities"):
            # if entity["entity"] == self.slot_name: 
            validated = self.validate(entity["entity"], entity["value"])
                # if validated is not None:
            events_custom.extend([SlotSet(entity, validated)])
                # return [SlotSet(self.slot_name, validated)]
        return events_custom

def trackid_generator(size = 5, chars = string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_trackid(size = 5):
    trackidnum = trackid_generator(size = size)
    df = pd.read_csv('complaints.csv')
    if any(df.loc[:, 'Track ID'] == trackidnum):
        return create_trackid(size = size)
    return trackid

class ActionSearchRestaurants(FormAction):
    RANDOMIZE = False

    @staticmethod
    def required_fields():
        return [
            FreeTextFormField("appliance"),
            FreeTextFormField("issue"),
            FreeTextFormField("modelnumber"),
            FreeTextFormField("serialnumber"),
            FreeTextFormField("name"),
            FreeTextFormField("email"),
            FreeTextFormField("address"),
            FreeTextFormField("pincode"),
            FreeTextFormField("date"),
            FreeTextFormField("timeslots"),
            BooleanFormField("confirmcomplain", "affirm", "deny")
        ]

    def name(self):
        return 'action_get_complaint_detail'

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Your complaint has been logged successfully !!!!.")
#         dispatcher // padho
        return []

# class GenerateTimeSlots(Action):
#     def name(self):
#         return 'action_generate_time_slots'
        
#     def run(self, dispatcher, tracker, domain):
#         import random
#         [random.randint()] 
        # dispatcher.utter_message("looking for restaurants")
#         restaurant_api = RestaurantAPI()
#         restaurants = restaurant_api.search(tracker.get_slot("cuisine"))
#         return [SlotSet("matches", restaurants)]


# class ActionSuggest(Action):
#     def name(self):
#         return 'action_suggest'

#     def run(self, dispatcher, tracker, domain):
#         dispatcher.utter_message("here's what I found:")
#         dispatcher.utter_message(tracker.get_slot("matches"))
#         dispatcher.utter_message("is it ok for you? "
#                                  "hint: I'm not going to "
#                                  "find anything else :)")
#         return []
