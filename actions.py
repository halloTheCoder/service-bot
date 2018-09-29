from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.forms import FormAction, FormField 

import pandas as pd


# EntityFormField(entity_name, slot_name), which will look for an entity called entity_name to fill a slot slot_name.
# BooleanFormField(slot_name, affirm_intent, deny_intent), which looks for the intents affirm_intent and deny_intent to fill a boolean slot called slot_name.
# FreeTextFormField(slot_name) : which will use the next user utterance to fill the text slot slot_name
class CustomFormField(FormField):
    def __init__(self):
        self.df = pd.read_excel('SampleModelSerialGEA.xlsx')
        super(self, FormField).__init__()
        
    # noinspection PyMethodMayBeStatic
    def validate(self, value):
        """Check if extracted value for a requested slot is valid.
        Users should override this to implement custom validation logic,
        returning None indicates a negative validation result, and the slot
        will not be set.
        """
        print(value)
        if value == 'appliance':      ###IMP :: can reduce appliance value to one allowed here
            if not any(self.df.loc[:, 'Product Line'] == value):
                value = None
        
        if value == 'modelnumber':
            if not any(self.df.loc[:, 'Model Number'] == value):
                value = None

        if value == 'serialnumber':
            if not any(self.df.loc[:, 'Serial Number'] == value):
                value = None

        return value


class EntityFormField(CustomFormField):

    def __init__(self, entity_name, slot_name):
        self.entity_name = entity_name
        self.slot_name = slot_name

    def extract(self, tracker):
        # type: (Tracker) -> List[EventType]

        value = next(tracker.get_latest_entity_values(self.entity_name), None)
        validated = self.validate(value)
        if validated is not None:
            return [SlotSet(self.slot_name, validated)]
        else:
            return []


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
            if entity["entity"] == self.slot_name: 
                validated = self.validate(entity["value"])
                if validated is not None:
                    events_custom.extend([SlotSet(self.slot_name, validated)])
                # return [SlotSet(self.slot_name, validated)]
        return events_custom


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
        dispatcher.utter_message("Your complaint has been logged successfully !!!!. Thank you for using our service.")
#         dispatcher // padho
        return []

# class GenerateTrackID

