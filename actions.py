from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.forms import FormAction # , FreeTextFormField

import pandas as pd


# EntityFormField(entity_name, slot_name), which will look for an entity called entity_name to fill a slot slot_name.
# BooleanFormField(slot_name, affirm_intent, deny_intent), which looks for the intents affirm_intent and deny_intent to fill a boolean slot called slot_name.
# FreeTextFormField(slot_name) : which will use the next user utterance to fill the text slot slot_name

class FormField(object):
    def __init__(self):
        df = pd.read_excel('SampleModelSerialGEA.xlsx')
        
    # noinspection PyMethodMayBeStatic
    def validate(self, value):
        """Check if extracted value for a requested slot is valid.
        Users should override this to implement custom validation logic,
        returning None indicates a negative validation result, and the slot
        will not be set.
        """
        if value == 'appliance':      ###IMP :: can reduce appliance value to one allowed here
            if not any(df.loc[:, 'Product Line'] == value):
                value = None
        
        if value == 'model_number':
            if not any(df.loc[:, 'Model Number'] == value):
                value = None

        if value == 'serial_number':
            if not any(df.loc[:, 'Serial Number'] == value):
                value = None

        return value

class FreeTextFormField(FormField):
    def __init__(self, slot_name):
        self.slot_name = slot_name

    def extract(self, tracker):
        # type: (Tracker) -> List[EventType]

        validated = self.validate(tracker.latest_message.get("text"))
        if validated is not None:
            return [SlotSet(self.slot_name, validated)]
        return []


class ActionSearchRestaurants(FormAction):
    RANDOMIZE = False

    @staticmethod
    def required_fields():
        return [
            FreeTextFormField("appliance"),
            FreeTextFormField("issue"),
#             BooleanFormField("vegetarian", "affirm", "deny")
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
        dispatcher.utter_message("Your complaint has been logged successfully !!!!. Thank you for using our service.")
#         dispatcher // padho
        return []

# class GenerateTrackID
