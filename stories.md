## Generated Story 4126920875962733299
* greet
    - utter_greet
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "appliance"}
* log_complain{"appliance": "fridge", "issue": "broken"}
    - slot{"appliance": "fridge"}
    - slot{"issue": "broken"}
    - action_get_complaint_detail
    - slot{"appliance": "fridge"}
    - slot{"appliance": "broken"}
    - slot{"requested_slot": "modelnumber"}
* deny{"modelnumber": "cfe28ushss"}
    - slot{"modelnumber": "cfe28ushss"}
    - action_get_complaint_detail
    - slot{"modelnumber": "cfe28ushss"}
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "rf2az3345"}
    - slot{"serialnumber": "rf2az3345"}
    - action_get_complaint_detail
    - slot{"serialnumber": null}
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "rfaz3345"}
    - slot{"serialnumber": "rfaz3345"}
    - action_get_complaint_detail
    - slot{"serialnumber": "rfaz3345"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "abc@xyz"}
    - slot{"email": "abc@xyz"}
    - action_get_complaint_detail
    - slot{"email": "abc@xyz"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "8002331136"}
    - slot{"phonenumber": "8002331136"}
    - action_get_complaint_detail
    - slot{"phonenumber": "8002331136"}
    - action_get_geo_location
    - slot{"address": "Kharagpur Paschim Medinipur West Bengal 721301 "}
    - slot{"pincode": "721301"}
    - utter_ask_confirm_address
* affirm
    - action_set_geo_location
    - slot{"address": null}
    - slot{"pincode": null}
    - action_get_complaint_detail
    - slot{"requested_slot": "address"}
* log_complain{"address": "132 , my street , kingston , new york   united states", "pincode": "12401"}
    - slot{"address": "132 , my street , kingston , new york   united states"}
    - slot{"pincode": "12401"}
    - action_get_complaint_detail
    - slot{"address": "132 , my street , kingston , new york   united states"}
    - slot{"address": "12401"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "monday\t1-4 am"}
    - slot{"time2": "tuseday\t7-10 am"}
    - slot{"time3": "tuseday\t8-11 am"}
    - utter_ask_time
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "11 - 12"}
    - slot{"timeslots": "11 - 12"}
    - action_get_complaint_detail
    - slot{"timeslots": "11 - 12"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR96517"}
    - action_store_details
    - utter_youarewelcome
    - action_restart
* goodbye
    - utter_goodbye
    - action_restart

## Generated Story 462259937121795223
* greet
    - utter_greet
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "appliance"}
* log_complain{"appliance": "fridge", "issue": "broken"}
    - slot{"appliance": "fridge"}
    - slot{"issue": "broken"}
    - action_get_complaint_detail
    - slot{"appliance": "fridge"}
    - slot{"issue": "broken"}
    - slot{"requested_slot": "modelnumber"}
* log_complain{"modelnumber": "pyd22kblts"}
    - slot{"modelnumber": "pyd22kblts"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "rfa22z3347"}
    - slot{"serialnumber": "rfa22z3347"}
    - action_get_complaint_detail
    - slot{"serialnumber": null}
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "rfaz3347"}
    - slot{"serialnumber": "rfaz3347"}
    - action_get_complaint_detail
    - slot{"serialnumber": "rfaz3347"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev", "email": "abc@xyz"}
    - slot{"email": "abc@xyz"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"email": "abc@xyz"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "8002331136"}
    - slot{"phonenumber": "8002331136"}
    - action_get_complaint_detail
    - slot{"phonenumber": "8002331136"}
    - action_get_geo_location
    - slot{"address": "Kharagpur Paschim Medinipur West Bengal 721301 "}
    - slot{"pincode": "721301"}
    - utter_ask_confirm_address
* affirm
    - action_set_geo_location
    - slot{"address": null}
    - slot{"pincode": null}
    - action_get_complaint_detail
    - slot{"requested_slot": "address"}
* log_complain{"address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - action_get_complaint_detail
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "monday\t1-4 am"}
    - slot{"time2": "tuseday\t7-10 am"}
    - slot{"time3": "tuseday\t8-11 am"}
    - utter_ask_time
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "11-12"}
    - slot{"timeslots": "11-12"}
    - action_get_complaint_detail
    - slot{"timeslots": "11-12"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR96517"}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## Generated Story -6935492597364981232
* greet
    - utter_greet
* log_complain{"appliance": "fridge", "issue": "broken", "name": "dev", "email": "abc@gmail.com", "modelnumber": "pyd22kblts", "serialnumber": "rfaz3347", "address": "2025 m street , northwest , washington , dc", "pincode": "20036", "date": "tuseday", "timeslots": "11-12"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"appliance": "fridge"}
    - slot{"date": "tuseday"}
    - slot{"email": "abc@gmail.com"}
    - slot{"issue": "broken"}
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"name": "dev"}
    - slot{"pincode": "20036"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"timeslots": "11-12"}
    - action_get_complaint_detail
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR96517"}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## story2
* greet
    - utter_greet
* service_modify_cancel
    - utter_ask_trackid
* service_detail{"trackid": "TR96517"}
    - utter_ask_cancel_complain_confirm
* affirm
    - action_cancel_complain
    - utter_youarewelcome
    - action_restart
    - utter_greet

## story3
* greet
    - utter_greet
* service_modify_cancel
    - utter_ask_trackid
* service_detail{"trackid": "TR96517"}
    - utter_ask_cancel_complain_confirm
* deny
    - utter_youarewelcome
    - action_restart
    - utter_greet

## Generated Story -5149329953314977538
* greet
    - utter_greet
* service_modify_cancel{"trackid": "tr96517"}
    - slot{"trackid": "tr96517"}
    - utter_ask_cancel_complain_confirm
* affirm
    - action_cancel_complain
    - slot{"trackid": null}
    - utter_youarewelcome
    - action_restart
    - utter_greet

## Generated Story 2873271378787429177
* service_modify_cancel
    - utter_ask_trackid
* service_detail{"trackid": "tr96517"}
    - slot{"trackid": "tr96517"}
    - utter_ask_cancel_complain_confirm
* deny
    - utter_youarewelcome
    - action_restart
    - utter_greet

## Generated Story -1078642771550695945
* goodbye
    - utter_goodbye
    - utter_youarewelcome
    - action_restart
    - utter_greet

## Generated Story 8531147378216048446
* greet
    - utter_greet
* service_query
    - utter_ask_trackid
* service_detail{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_query_detail
    - slot{"trackid": null}
    - utter_youarewelcome
    - action_restart
    - utter_greet

## Story4
* greet
    - utter_greet
* service_query{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_query_detail
    - slot{"trackid": null}
    - utter_youarewelcome
    - action_restart
    - utter_greet


## Generated Story 7138389429977952463
* service_query_time
    - utter_ask_trackid
* service_detail{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_query_time_detail
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart




## Generated Story 5312243617061914185
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "appliance"}
* log_complain{"appliance": "ac", "issue": "not cooling"}
    - slot{"appliance": "ac"}
    - slot{"issue": "not cooling"}
    - action_get_complaint_detail
    - slot{"appliance": "ac"}
    - slot{"issue": "not cooling"}
    - slot{"requested_slot": "modelnumber"}
* log_complain{"modelnumber": "AJEQ10DCF"}
    - slot{"modelnumber": "AJEQ10DCF"}
    - action_get_complaint_detail
    - slot{"modelnumber": "AJEQ10DCF"}
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "aczn9053"}
    - slot{"serialnumber": "aczn9053"}
    - action_get_complaint_detail
    - slot{"serialnumber": "aczn9053"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "Warner"}
    - slot{"name": "Warner"}
    - action_get_complaint_detail
    - slot{"name": "Warner"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "letme@gmail.com"}
    - slot{"email": "letme@gmail.com"}
    - action_get_complaint_detail
    - slot{"email": "letme@gmail.com"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "8002331136"}
    - slot{"phonenumber": "8002331136"}
    - action_get_complaint_detail
    - slot{"phonenumber": "8002331136"}
    - action_get_geo_location
    - slot{"address": "Kharagpur Paschim Medinipur West Bengal 721301 "}
    - slot{"pincode": "721301"}
    - utter_ask_confirm_address
* affirm
    - action_set_geo_location
    - slot{"address": null}
    - slot{"pincode": null}
    - action_get_complaint_detail
    - slot{"requested_slot": "address"}
* log_complain{"address": "50 water street mystic ct", "pincode": "06355"}
    - slot{"address": "50 water street mystic ct"}
    - slot{"pincode": "06355"}
    - action_get_complaint_detail
    - slot{"address": "50 water street mystic ct"}
    - slot{"pincode": "06355"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "monday\t1-4 am"}
    - slot{"time2": "tuseday\t7-10 am"}
    - slot{"time3": "tuseday\t8-11 am"}
    - utter_ask_time
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_set_timeslots
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "2 - 6 pm"}
    - slot{"timeslots": "2 - 6 pm"}
    - action_get_complaint_detail
    - slot{"timeslots": "2 - 6 pm"}
    - slot{"requested_slot": "confirmcomplain"}
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story 3579041470812976832
* goodbye
    - utter_goodbye
    - utter_youarewelcome
    - action_restart


## Generated Story -5586181752857983642
* greet
    - utter_greet
* log_complain{"appliance": "fridge", "issue": "broken"}
    - slot{"appliance": "fridge"}
    - slot{"issue": "broken"}
    - action_get_complaint_detail
    - slot{"requested_slot": "modelnumber"}
* log_complain{"name": "dev", "email": "abc@gmail.com", "modelnumber": "pyd22kblts", "serialnumber": "rfaz3347", "address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"email": "abc@gmail.com"}
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"name": "dev"}
    - slot{"pincode": "20036"}
    - slot{"serialnumber": "rfaz3347"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"email": "abc@gmail.com"}
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "monday\t1-4 am"}
    - slot{"time2": "tuseday\t7-10 am"}
    - slot{"time3": "tuseday\t8-11 am"}
    - utter_ask_time
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "11 - 12 am"}
    - slot{"timeslots": "11 - 12 am"}
    - action_get_complaint_detail
    - slot{"timeslots": "11 - 12 am"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR74418"}
    - action_store_details
    - utter_youarewelcome
    - action_restart
    - utter_greet


## Story10
* service_modify_cancel{"trackid": "tr96517"}
    - slot{"trackid": "tr96517"}
    - utter_ask_cancel_complain_confirm
* deny
    - utter_youarewelcome
    - action_restart
    - utter_greet

## Generated Story 5141647181317035153
* greet
    - utter_greet
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "appliance"}
* log_complain{"appliance": "dryer"}
    - slot{"appliance": "dryer"}
    - action_get_complaint_detail
    - slot{"appliance": "dryer"}
    - slot{"requested_slot": "issue"}
* log_complain{"issue": "not heating"}
    - slot{"issue": "not heating"}
    - action_get_complaint_detail
    - slot{"issue": "not heating"}
    - slot{"requested_slot": "modelnumber"}
* log_complain{"modelnumber": "gfd43essmww"}
    - slot{"modelnumber": "gfd43essmww"}
    - action_get_complaint_detail
    - slot{"modelnumber": "gfd43essmww"}
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "drbg0112"}
    - slot{"serialnumber": "drbg0112"}
    - action_get_complaint_detail
    - slot{"serialnumber": "drbg0112"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "max"}
    - slot{"name": "max"}
    - action_get_complaint_detail
    - slot{"name": "max"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "max@yahoo.com"}
    - slot{"email": "max@yahoo.com"}
    - action_get_complaint_detail
    - slot{"email": "max@yahoo.com"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "8002331136"}
    - slot{"phonenumber": "8002331136"}
    - action_get_complaint_detail
    - slot{"phonenumber": "8002331136"}
    - action_get_geo_location
    - slot{"address": "Kharagpur Paschim Medinipur West Bengal 721301 "}
    - slot{"pincode": "721301"}
    - utter_ask_confirm_address
* affirm
    - action_set_geo_location
    - slot{"address": null}
    - slot{"pincode": null}
    - action_get_complaint_detail
    - slot{"requested_slot": "address"}
* log_complain{"address": "574 new london turnpike norwich ct", "pincode": "06360"}
    - slot{"address": "574 new london turnpike norwich ct"}
    - slot{"pincode": "06360"}
    - action_get_complaint_detail
    - slot{"address": "574 new london turnpike norwich ct"}
    - slot{"pincode": "06360"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "monday\t1-4 am"}
    - slot{"time2": "tuseday\t7-10 am"}
    - slot{"time3": "tuseday\t8-11 am"}
    - utter_ask_time
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "5 - 6 pm"}
    - slot{"timeslots": "5 - 6 pm"}
    - action_get_complaint_detail
    - slot{"timeslots": "5 - 6 pm"}
    - slot{"requested_slot": "confirmcomplain"}
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story -4368655346389352461
* None
    - utter_default
* goodbye
    - utter_goodbye
    - action_restart

## Generated Story 385304095398033263
* greet
    - utter_greet
* log_complain{"appliance": "fridge", "issue": "broken"}
    - slot{"appliance": "fridge"}
    - slot{"issue": "broken"}
    - action_get_complaint_detail
    - slot{"requested_slot": "modelnumber"}
* log_complain{"modelnumber": "pyd22kblts", "serialnumber": "rfaz3347", "address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"pincode": "20036"}
    - slot{"serialnumber": "rfaz3347"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "abc@xyz"}
    - slot{"email": "abc@xyz"}
    - action_get_complaint_detail
    - slot{"email": "abc@xyz"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "8002331136"}
    - slot{"phonenumber": "8002331136"}
    - action_get_complaint_detail
    - slot{"phonenumber": "8002331136"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "tuseday\t3-6 pm"}
    - slot{"time2": "tuseday\t6-9 pm"}
    - slot{"time3": "monday\t2-5 am"}
    - utter_ask_time
* log_complain{"date": "tuseday", "timeslots": "11 - 12"}
    - slot{"date": "tuseday"}
    - slot{"timeslots": "11 - 12"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_get_complaint_detail
    - slot{"date": "tuseday"}
    - slot{"timeslots": "11 - 12"}
    - slot{"requested_slot": "confirmcomplain"}
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story -5662216199692479777
* greet
    - utter_greet
* log_complain{"appliance": "ac", "issue": "not working"}
    - slot{"appliance": "ac"}
    - slot{"issue": "not working"}
    - action_get_complaint_detail
    - slot{"requested_slot": "modelnumber"}
* log_complain{"modelnumber": "pyd22kblts", "serialnumber": "rfaz3347"}
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"serialnumber": "rfaz3347"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "Ralph White", "email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - slot{"name": "Ralph White"}
    - action_get_complaint_detail
    - slot{"name": "Ralph White"}
    - slot{"email": "abc@gmail.com"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "8002331136"}
    - slot{"phonenumber": "8002331136"}
    - action_get_complaint_detail
    - slot{"phonenumber": "8002331136"}
    - action_get_geo_location
    - slot{"address": "Kharagpur Paschim Medinipur West Bengal 721301 "}
    - slot{"pincode": "721301"}
    - utter_ask_confirm_address
* affirm
    - action_set_geo_location
    - slot{"address": null}
    - slot{"pincode": null}
    - action_get_complaint_detail
    - slot{"requested_slot": "address"}
* log_complain{"address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - action_get_complaint_detail
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "tuseday\t7-10 pm"}
    - slot{"time2": "tuseday\t2-5 am"}
    - slot{"time3": "monday\t5-8 pm"}
    - utter_ask_time
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "11 - 12 am"}
    - slot{"timeslots": "11 - 12 am"}
    - action_get_complaint_detail
    - slot{"timeslots": "11 - 12 am"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR91045"}
    - action_store_details
    - utter_youarewelcome
    - action_restart


## Generated Story 5250014129854198553
* greet
    - utter_greet
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "appliance"}
* log_complain{"appliance": "microwave"}
    - slot{"appliance": "microwave"}
    - action_get_complaint_detail
    - slot{"appliance": "microwave"}
    - slot{"requested_slot": "issue"}
* log_complain{"issue": "not working"}
    - slot{"issue": "not working"}
    - action_get_complaint_detail
    - slot{"issue": "not working"}
    - slot{"requested_slot": "modelnumber"}
* log_complain{"modelnumber": "pt9051slsh"}
    - slot{"modelnumber": "pt9051slsh"}
    - action_get_complaint_detail
    - slot{"modelnumber": null}
    - slot{"requested_slot": "modelnumber"}
* log_complain{"modelnumber": "pt9051slss"}
    - slot{"modelnumber": "pt9051slss"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pt9051slss"}
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "wopk2283"}
    - slot{"serialnumber": "wopk2283"}
    - action_get_complaint_detail
    - slot{"serialnumber": "wopk2283"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "dev@gmail.com"}
    - slot{"email": "dev@gmail.com"}
    - action_get_complaint_detail
    - slot{"email": "dev@gmail.com"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "8002331136"}
    - slot{"phonenumber": "8002331136"}
    - action_get_complaint_detail
    - slot{"phonenumber": "8002331136"}
    - action_get_geo_location
    - slot{"address": "Kharagpur Paschim Medinipur West Bengal 721301 "}
    - slot{"pincode": "721301"}
    - utter_ask_confirm_address
* affirm
    - action_set_geo_location
    - slot{"address": null}
    - slot{"pincode": null}
    - action_get_complaint_detail
    - slot{"requested_slot": "address"}
* log_complain{"address": "675 greenview ave . thibodaux , la", "pincode": "70301"}
    - slot{"address": "675 greenview ave . thibodaux , la"}
    - slot{"pincode": "70301"}
    - action_get_complaint_detail
    - slot{"address": "675 greenview ave . thibodaux , la"}
    - slot{"pincode": "70301"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "tuseday\t7-10 pm"}
    - slot{"time2": "tuseday\t2-5 am"}
    - slot{"time3": "monday\t5-8 pm"}
    - utter_ask_time
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "1 - 5 pm"}
    - slot{"timeslots": "1 - 5 pm"}
    - action_get_complaint_detail
    - slot{"timeslots": "1 - 5 pm"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR66873"}
    - action_store_details
    - utter_youarewelcome
    - action_restart


## Generated Story -5049449237464951625
* service_modify_cancel
    - utter_ask_trackid
* service_detail{"trackid": "tr66873"}
    - slot{"trackid": "tr66873"}
    - utter_ask_cancel_complain_confirm
* affirm
    - action_cancel_complain
    - slot{"trackid": null}
    - utter_youarewelcome
    - action_restart

## Generated Story 4881292647007510230
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "appliance"}
* log_complain{"appliance": "ac", "issue": "not cooling"}
    - slot{"appliance": "ac"}
    - slot{"issue": "not cooling"}
    - action_get_complaint_detail
    - slot{"appliance": "ac"}
    - slot{"issue": "not cooling"}
    - slot{"requested_slot": "modelnumber"}
* log_complain{"modelnumber": "ajcq10acg", "serialnumber": "aczn9072"}
    - slot{"modelnumber": "ajcq10acg"}
    - slot{"serialnumber": "aczn9072"}
    - action_get_complaint_detail
    - slot{"modelnumber": "ajcq10acg"}
    - slot{"serialnumber": "aczn9072"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "dev@gmail.com"}
    - slot{"email": "dev@gmail.com"}
    - action_get_complaint_detail
    - slot{"email": "dev@gmail.com"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "8002331136"}
    - slot{"phonenumber": "8002331136"}
    - action_get_complaint_detail
    - slot{"phonenumber": "8002331136"}
    - action_get_geo_location
    - slot{"address": "Kharagpur Paschim Medinipur West Bengal 721301 "}
    - slot{"pincode": "721301"}
    - utter_ask_confirm_address
* affirm
    - action_set_geo_location
    - slot{"address": null}
    - slot{"pincode": null}
    - action_get_complaint_detail
    - slot{"requested_slot": "address"}
* log_complain{"address": "49 anderson street greensboro , nc", "pincode": "27405"}
    - slot{"address": "49 anderson street greensboro , nc"}
    - slot{"pincode": "27405"}
    - action_get_complaint_detail
    - slot{"address": "49 anderson street greensboro , nc"}
    - slot{"pincode": "27405"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "tuseday\t7-10 pm"}
    - slot{"time2": "tuseday\t2-5 am"}
    - slot{"time3": "monday\t5-8 pm"}
    - utter_ask_time
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "4 - 7 pm"}
    - slot{"timeslots": "4 - 7 pm"}
    - action_get_complaint_detail
    - slot{"timeslots": "4 - 7 pm"}
    - slot{"requested_slot": "confirmcomplain"}
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story 8073371264184960528
* goodbye
    - utter_goodbye

## Story30
* restart
    - utter_youarewelcome
    - action_restart


## Generated Story 7347670153600515006
* greet
    - utter_greet
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "appliance"}
* log_complain{"serialnumber": "rfaz3351"}
    - slot{"serialnumber": "rfaz3351"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"appliance": "refrigerator"}
    - slot{"serialnumber": "rfaz3351"}
    - slot{"requested_slot": "issue"}
* log_complain{"issue": "broken"}
    - slot{"issue": "broken"}
    - action_get_complaint_detail
    - slot{"issue": "broken"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "akash.chandra8d@gmail.com"}
    - slot{"email": "akash.chandra8d@gmail.com"}
    - action_get_complaint_detail
    - slot{"email": "akash.chandra8d@gmail.com"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "8002331136"}
    - slot{"phonenumber": "8002331136"}
    - action_get_complaint_detail
    - slot{"phonenumber": "8002331136"}
    - action_get_geo_location
    - slot{"address": "Kharagpur Paschim Medinipur West Bengal 721301 "}
    - slot{"pincode": "721301"}
    - utter_ask_confirm_address
* affirm
    - action_set_geo_location
    - slot{"address": null}
    - slot{"pincode": null}
    - action_get_complaint_detail
    - slot{"requested_slot": "address"}
* log_complain{"address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - action_get_complaint_detail
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "saturday\t4-7 pm"}
    - slot{"time2": "saturday\t5-8 am"}
    - slot{"time3": "friday\t5-8 am"}
    - utter_ask_time
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "10 - 12 am"}
    - slot{"timeslots": "10 - 12 am"}
    - action_get_complaint_detail
    - slot{"timeslots": "10 - 12 am"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR16353"}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## Generated Story -6150529693599065443
* greet
    - utter_greet
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "appliance"}
* deny{"serialnumber": "rfaz3347"}
    - slot{"serialnumber": "rfaz3347"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"appliance": "refrigerator"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"requested_slot": "issue"}
* deny{"modelnumber": "cfe28ushss"}
    - slot{"modelnumber": "cfe28ushss"}
    - action_get_complaint_detail
    - slot{"modelnumber": null}
    - slot{"requested_slot": "issue"}
* log_complain{"issue": "not working"}
    - slot{"issue": "not working"}
    - action_get_complaint_detail
    - slot{"issue": "not working"}
    - slot{"requested_slot": "modelnumber"}
* deny{"serialnumber": "rfaz3345"}
    - slot{"serialnumber": "rfaz3345"}
    - action_get_complaint_detail
    - slot{"modelnumber": "cfe28ushss"}
    - slot{"serialnumber": "rfaz3345"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "akash.chandra8d@gmail.com"}
    - slot{"email": "akash.chandra8d@gmail.com"}
    - action_get_complaint_detail
    - slot{"email": "akash.chandra8d@gmail.com"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "8002331136"}
    - slot{"phonenumber": "8002331136"}
    - action_get_complaint_detail
    - slot{"phonenumber": "8002331136"}
    - action_get_geo_location
    - slot{"address": "Kharagpur Paschim Medinipur West Bengal 721301 "}
    - slot{"pincode": "721301"}
    - utter_ask_confirm_address
* affirm
    - action_set_geo_location
    - slot{"address": null}
    - slot{"pincode": null}
    - action_get_complaint_detail
    - slot{"requested_slot": "address"}
* log_complain{"address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - action_get_complaint_detail
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "saturday\t7-10 pm"}
    - slot{"time2": "saturday\t4-7 pm"}
    - slot{"time3": "saturday\t5-8 am"}
    - utter_ask_time
* log_complain{"date": "tuesday", "timeslots": "4 - 5 pm"}
    - slot{"date": "tuesday"}
    - slot{"timeslots": "4 - 5 pm"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"timeslots": "4 - 5 pm"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR71946"}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## Generated Story -6445700626960324807
* greet
    - utter_greet
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "rfaz3347"}
    - slot{"serialnumber": "rfaz3347"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"appliance": "refrigerator"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"requested_slot": "issue"}
* log_complain{"appliance": "refrigerator", "issue": "broken"}
    - slot{"appliance": "refrigerator"}
    - slot{"issue": "broken"}
    - action_get_complaint_detail
    - slot{"appliance": "refrigerator"}
    - slot{"issue": "broken"}
    - slot{"requested_slot": "name"}
* log_complain{"modelnumber": "cye22ushss"}
    - slot{"modelnumber": "cye22ushss"}
    - action_get_complaint_detail
    - slot{"modelnumber": null}
    - slot{"requested_slot": "modelnumber"}
* log_complain{"modelnumber": "pyd22kblts"}
    - slot{"modelnumber": "pyd22kblts"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev", "email": "akash.chandra8d@gmail.com"}
    - slot{"email": "akash.chandra8d@gmail.com"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"email": "akash.chandra8d@gmail.com"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "8002331136"}
    - slot{"phonenumber": "8002331136"}
    - action_get_complaint_detail
    - slot{"phonenumber": "8002331136"}
    - action_get_geo_location
    - action_get_geo_location
    - slot{"address": "Kharagpur Paschim Medinipur West Bengal 721301 "}
    - slot{"pincode": "721301"}
    - utter_ask_confirm_address
* affirm
    - action_set_geo_location
    - slot{"address": null}
    - slot{"pincode": null}
    - action_get_complaint_detail
    - slot{"requested_slot": "address"}
* log_complain{"address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - action_get_complaint_detail
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "friday\t1-4 pm"}
    - slot{"time2": "saturday\t5-8 pm"}
    - slot{"time3": "friday\t6-9 am"}
    - utter_ask_time
* log_complain{"date": "sunday"}
    - slot{"date": "sunday"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_get_complaint_detail
    - slot{"date": "sunday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "8 - 10 am"}
    - slot{"timeslots": "8 - 10 am"}
    - action_get_complaint_detail
    - slot{"timeslots": "8 - 10 am"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR70320"}
    - action_store_details
    - utter_youarewelcome
    - action_restart


## Generated Story -1908691441644278433
* greet
    - utter_greet
* log_complain{"appliance": "refrigerator", "issue": "not working"}
    - slot{"appliance": "refrigerator"}
    - slot{"issue": "not working"}
    - action_get_complaint_detail
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "rfaz3347"}
    - slot{"serialnumber": "rfaz3347"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"requested_slot": "name"}
* log_complain{"email": "akash.chandra8d@gmail.com", "phonenumber": "8002331136"}
    - slot{"email": "akash.chandra8d@gmail.com"}
    - slot{"phonenumber": "8002331136"}
    - action_get_complaint_detail
    - slot{"email": "akash.chandra8d@gmail.com"}
    - slot{"phonenumber": "8002331136"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "address"}
    - action_get_geo_location
    - slot{"address": "Kharagpur Paschim Medinipur West Bengal 721301 "}
    - slot{"pincode": "721301"}
    - utter_ask_confirm_address
* affirm
    - action_set_geo_location
    - slot{"address": null}
    - slot{"pincode": null}
    - action_get_complaint_detail
    - slot{"requested_slot": "address"}
* log_complain{"address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - action_get_complaint_detail
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "scott\tsunday\t2-5 pm"}
    - slot{"time2": "scott\tmonday\t6-9 pm"}
    - slot{"time3": "scott\ttuseday\t3-6 am"}
    - utter_ask_time
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - slot{"time": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "10 - 12 pm"}
    - slot{"timeslots": "10 - 12 pm"}
    - action_get_complaint_detail
    - slot{"timeslots": "10 - 12 pm"}
    - slot{"requested_slot": "confirmcomplain"}
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates{"name": "ralph white"}
    - slot{"name": "ralph white"}
    - utter_ask_confirmcomplain
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR42032"}
    - slot{"time": null}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## Generated Story -5794393172560610186
* greet
    - utter_greet
* log_complain{"appliance": "refrigerator", "issue": "not working"}
    - slot{"appliance": "refrigerator"}
    - slot{"issue": "not working"}
    - action_get_complaint_detail
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "rfaz3347"}
    - slot{"serialnumber": "rfaz3347"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"requested_slot": "name"}
* log_complain{"email": "akash.chandra8d@gmail.com", "phonenumber": "8002331136"}
    - slot{"email": "akash.chandra8d@gmail.com"}
    - slot{"phonenumber": "8002331136"}
    - action_get_complaint_detail
    - slot{"email": "akash.chandra8d@gmail.com"}
    - slot{"phonenumber": "8002331136"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "address"}
    - action_get_geo_location
    - slot{"address": "Kharagpur Paschim Medinipur West Bengal 721301 "}
    - slot{"pincode": "721301"}
    - utter_ask_confirm_address
* affirm
    - action_set_geo_location
    - slot{"address": null}
    - slot{"pincode": null}
    - action_get_complaint_detail
    - slot{"requested_slot": "address"}
* log_complain{"address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - action_get_complaint_detail
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "scott\tsunday\t8-11 am"}
    - slot{"time2": "scott\tmonday\t2-5 am"}
    - slot{"time3": "scott\ttuseday\t9-12 am"}
    - utter_ask_time
* log_complain{"date": "tuesday", "timeslots": "11 - 12 am"}
    - slot{"date": "tuesday"}
    - slot{"timeslots": "11 - 12 am"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - slot{"time": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"timeslots": "11 - 12 am"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR41264"}
    - slot{"time": null}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## Generated Story 4481529603718627494
* greet
    - utter_greet
* log_complain{"appliance": "refrigerator", "issue": "not cooling"}
    - slot{"appliance": "refrigerator"}
    - slot{"issue": "not cooling"}
    - action_get_complaint_detail
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "rfaz3347"}
    - slot{"serialnumber": "rfaz3347"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "emma", "email": "akash.chandra8d@gmail.com", "phonenumber": "8250599363"}
    - slot{"email": "akash.chandra8d@gmail.com"}
    - slot{"name": "emma"}
    - slot{"phonenumber": "8250599363"}
    - action_get_complaint_detail
    - slot{"name": "emma"}
    - slot{"email": "akash.chandra8d@gmail.com"}
    - slot{"phonenumber": "8250599363"}
    - slot{"requested_slot": "address"}
    - action_get_geo_location
    - slot{"address": "Kharagpur Paschim Medinipur West Bengal 721301 "}
    - slot{"pincode": "721301"}
    - utter_ask_confirm_address
* deny
    - action_set_geo_location
    - slot{"address": null}
    - slot{"pincode": null}
    - action_get_complaint_detail
    - slot{"requested_slot": "address"}
* log_complain{"address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - action_get_complaint_detail
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "tim\tsunday\t5 - 8 pm"}
    - slot{"time2": "scott\tmonday\t2 - 5 am"}
    - slot{"time3": "scott\ttuesday\t5 - 8 pm"}
    - utter_ask_time
* log_complain{"date": "tuesday", "timeslots": "5 - 8 pm"}
    - slot{"date": "tuesday"}
    - slot{"timeslots": "5 - 8 pm"}
    - action_set_timeslots
    - slot{"time": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"timeslots": "5 - 8 pm"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR59159"}
    - slot{"technician": "scott"}
    - slot{"time": null}
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_store_details
    - utter_youarewelcome
    - action_restart


## Generated Story 2280239829877492001
* greet
    - utter_greet
* service_modify
    - utter_ask_trackid
* service_detail{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "5 - 8 pm"}
    - slot{"time2": "6 - 9 pm"}
    - slot{"time3": "7 - 10 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "5 - 8 pm"}
    - slot{"timeslots": "5 - 8 pm"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* deny
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "8 - 11 am"}
    - slot{"time2": "7 - 10 am"}
    - slot{"time3": "8 - 11 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "7 - 10 am"}
    - slot{"timeslots": "7 - 10 am"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Story 100
* service_modify
    - utter_ask_trackid
* service_detail{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "5 - 8 pm"}
    - slot{"time2": "6 - 9 pm"}
    - slot{"time3": "7 - 10 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "5 - 8 pm"}
    - slot{"timeslots": "5 - 8 pm"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* deny
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "8 - 11 am"}
    - slot{"time2": "7 - 10 am"}
    - slot{"time3": "8 - 11 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "7 - 10 am"}
    - slot{"timeslots": "7 - 10 am"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Story 101
* service_modify{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "5 - 8 pm"}
    - slot{"time2": "6 - 9 pm"}
    - slot{"time3": "7 - 10 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "5 - 8 pm"}
    - slot{"timeslots": "5 - 8 pm"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* deny
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "8 - 11 am"}
    - slot{"time2": "7 - 10 am"}
    - slot{"time3": "8 - 11 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "7 - 10 am"}
    - slot{"timeslots": "7 - 10 am"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Story 102
* service_modify_timeslots{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "5 - 8 pm"}
    - slot{"time2": "6 - 9 pm"}
    - slot{"time3": "7 - 10 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "5 - 8 pm"}
    - slot{"timeslots": "5 - 8 pm"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* deny
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "8 - 11 am"}
    - slot{"time2": "7 - 10 am"}
    - slot{"time3": "8 - 11 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "7 - 10 am"}
    - slot{"timeslots": "7 - 10 am"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Story 103
* greet
    - utter_greet
* service_modify_timeslots{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "5 - 8 pm"}
    - slot{"time2": "6 - 9 pm"}
    - slot{"time3": "7 - 10 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "5 - 8 pm"}
    - slot{"timeslots": "5 - 8 pm"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* deny
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "8 - 11 am"}
    - slot{"time2": "7 - 10 am"}
    - slot{"time3": "8 - 11 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "7 - 10 am"}
    - slot{"timeslots": "7 - 10 am"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Story 104
* service_modify_timeslots{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "5 - 8 pm"}
    - slot{"time2": "6 - 9 pm"}
    - slot{"time3": "7 - 10 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "5 - 8 pm"}
    - slot{"timeslots": "5 - 8 pm"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* deny
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "8 - 11 am"}
    - slot{"time2": "7 - 10 am"}
    - slot{"time3": "8 - 11 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "7 - 10 am"}
    - slot{"timeslots": "7 - 10 am"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Story 105
* greet
    - utter_greet
* service_modify{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "5 - 8 pm"}
    - slot{"time2": "6 - 9 pm"}
    - slot{"time3": "7 - 10 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "5 - 8 pm"}
    - slot{"timeslots": "5 - 8 pm"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* deny
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "8 - 11 am"}
    - slot{"time2": "7 - 10 am"}
    - slot{"time3": "8 - 11 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "7 - 10 am"}
    - slot{"timeslots": "7 - 10 am"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story 8109298730726901941
* greet
    - utter_greet
* service_modify_timeslots{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_what_to_modify
* service_modify_timeslots
    - action_complain_modify_get_timeslots
    - slot{"time1": "3 - 6 pm"}
    - slot{"time2": "8 - 11 am"}
    - slot{"time3": "5 - 8 pm"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "3 - 6 pm"}
    - slot{"timeslots": "3 - 6 pm"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* deny
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story 1757201971027004411
* service_modify_timeslots{"trackid": "tr431252"}
    - slot{"trackid": "tr431252"}
    - action_complain_modify_check_track_id
    - slot{"trackid": null}
    - utter_wrong_track_id
* service_detail{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "5 - 8 pm"}
    - slot{"time2": "9 - 12 am"}
    - slot{"time3": "7 - 10 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "5 - 8 pm"}
    - slot{"timeslots": "5 - 8 pm"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* deny
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* deny
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Story 200
* service_modify
    - utter_ask_trackid
* service_detail{"trackid": "tr32312"}
    - slot{"trackid": "tr32312"}
    - action_complain_modify_check_track_id
    - slot{"trackid": null}
    - utter_wrong_track_id
* service_detail{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "5 - 8 pm"}
    - slot{"time2": "6 - 9 pm"}
    - slot{"time3": "7 - 10 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "5 - 8 pm"}
    - slot{"timeslots": "5 - 8 pm"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* deny
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "8 - 11 am"}
    - slot{"time2": "7 - 10 am"}
    - slot{"time3": "8 - 11 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "7 - 10 am"}
    - slot{"timeslots": "7 - 10 am"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Story 201
* service_modify{"trackid": "tr431252"}
    - slot{"trackid": "tr431252"}
    - action_complain_modify_check_track_id
    - slot{"trackid": null}
    - utter_wrong_track_id
* service_detail{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "5 - 8 pm"}
    - slot{"time2": "6 - 9 pm"}
    - slot{"time3": "7 - 10 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "5 - 8 pm"}
    - slot{"timeslots": "5 - 8 pm"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* deny
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "8 - 11 am"}
    - slot{"time2": "7 - 10 am"}
    - slot{"time3": "8 - 11 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "7 - 10 am"}
    - slot{"timeslots": "7 - 10 am"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Story 202
* service_modify_timeslots{"trackid": "tr431252"}
    - slot{"trackid": "tr431252"}
    - action_complain_modify_check_track_id
    - slot{"trackid": null}
    - utter_wrong_track_id
* service_detail{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "5 - 8 pm"}
    - slot{"time2": "6 - 9 pm"}
    - slot{"time3": "7 - 10 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "5 - 8 pm"}
    - slot{"timeslots": "5 - 8 pm"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* deny
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "8 - 11 am"}
    - slot{"time2": "7 - 10 am"}
    - slot{"time3": "8 - 11 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "7 - 10 am"}
    - slot{"timeslots": "7 - 10 am"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Story 203
* greet
    - utter_greet
* service_modify_timeslots{"trackid": "tr431252"}
    - slot{"trackid": "tr431252"}
    - action_complain_modify_check_track_id
    - slot{"trackid": null}
    - utter_wrong_track_id
* service_detail{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "5 - 8 pm"}
    - slot{"time2": "6 - 9 pm"}
    - slot{"time3": "7 - 10 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "5 - 8 pm"}
    - slot{"timeslots": "5 - 8 pm"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* deny
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "8 - 11 am"}
    - slot{"time2": "7 - 10 am"}
    - slot{"time3": "8 - 11 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "7 - 10 am"}
    - slot{"timeslots": "7 - 10 am"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Story 204
* service_modify_timeslots{"trackid": "tr431252"}
    - slot{"trackid": "tr431252"}
    - action_complain_modify_check_track_id
    - slot{"trackid": null}
    - utter_wrong_track_id
* service_detail{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "5 - 8 pm"}
    - slot{"time2": "6 - 9 pm"}
    - slot{"time3": "7 - 10 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "5 - 8 pm"}
    - slot{"timeslots": "5 - 8 pm"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* deny
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "8 - 11 am"}
    - slot{"time2": "7 - 10 am"}
    - slot{"time3": "8 - 11 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "7 - 10 am"}
    - slot{"timeslots": "7 - 10 am"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Story 205
* greet
    - utter_greet
* service_modify{"trackid": "tr431252"}
    - slot{"trackid": "tr431252"}
    - action_complain_modify_check_track_id
    - slot{"trackid": null}
    - utter_wrong_track_id
* service_detail{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "5 - 8 pm"}
    - slot{"time2": "6 - 9 pm"}
    - slot{"time3": "7 - 10 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "5 - 8 pm"}
    - slot{"timeslots": "5 - 8 pm"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* deny
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "8 - 11 am"}
    - slot{"time2": "7 - 10 am"}
    - slot{"time3": "8 - 11 am"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "7 - 10 am"}
    - slot{"timeslots": "7 - 10 am"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story -7043900514261493988
* service_modify_time{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_modify_time_confirm
* affirm
    - action_complain_modify_get_time
    - slot{"time1": "larry\ttuesday\t6 - 14 pm"}
    - slot{"time2": "scott\twednesday\t9 - 20 am"}
    - slot{"time3": "scott\tthursday\t8 - 18 am"}
    - utter_ask_time
* log_complain{"date": "wednesday", "timeslots": "9 - 20 am"}
    - slot{"date": "wednesday"}
    - slot{"timeslots": "9 - 20 am"}
    - action_complain_modify_set_time
    - slot{"time": null}
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story -5097314098511902396
* service_modify_time{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_modify_time_confirm
* affirm
    - action_complain_modify_get_time
    - slot{"time1": "larry\ttuesday\t4 - 7 pm"}
    - slot{"time2": "scott\twednesday\t7 - 10 am"}
    - slot{"time3": "scott\tthursday\t2 - 5 pm"}
    - utter_ask_time
* log_complain{"date": "wednesday", "timeslots": "7 - 10 am"}
    - slot{"date": "wednesday"}
    - slot{"timeslots": "7 - 10 am"}
    - action_complain_modify_set_time
    - slot{"time": null}
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story -6333162254070712700
* service_query
    - utter_ask_trackid
* service_detail{"trackid": "tr53622"}
    - slot{"trackid": "tr53622"}
    - action_query_detail
    - slot{"trackid": null}
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story 3175385900308852294
* service_query_time
    - utter_ask_trackid
* service_detail{"trackid": "tr53622"}
    - slot{"trackid": "tr53622"}
    - action_query_time_detail
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## story 70000000
* service_query_timeslots
    - utter_ask_trackid
* service_detail{"trackid": "tr53622"}
    - slot{"trackid": "tr53622"}
    - action_query_timeslots_detail
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story -5900065176236993828
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "dhrt5660"}
    - slot{"serialnumber": "dhrt5660"}
    - action_get_complaint_detail
    - slot{"modelnumber": "gdf650smjes"}
    - slot{"appliance": "dishwasher"}
    - slot{"serialnumber": "dhrt5660"}
    - slot{"requested_slot": "issue"}
* log_complain{"appliance": "dishwasher", "issue": "noisy"}
    - slot{"appliance": "dishwasher"}
    - slot{"issue": "noisy"}
    - action_get_complaint_detail
    - slot{"appliance": "dishwasher"}
    - slot{"issue": "noisy"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "robert"}
    - slot{"name": "robert"}
    - action_get_complaint_detail
    - slot{"name": "robert"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "robert@robertgmail.com"}
    - slot{"email": "robert@robertgmail.com"}
    - action_get_complaint_detail
    - slot{"email": "robert@robertgmail.com"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "1234567890"}
    - slot{"phonenumber": "1234567890"}
    - action_get_complaint_detail
    - slot{"phonenumber": "1234567890"}
    - slot{"requested_slot": "address"}
    - action_get_geo_location
    - action_get_complaint_detail
    - slot{"phonenumber": "1234567890"}
    - slot{"requested_slot": "address"}
* log_complain{"address": "8294 surrey street bonita springs , fl", "pincode": "34135"}
    - slot{"address": "8294 surrey street bonita springs , fl"}
    - slot{"pincode": "34135"}
    - action_get_complaint_detail
    - slot{"address": "8294 surrey street bonita springs , fl"}
    - slot{"pincode": "34135"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "scott\ttuesday\t5 - 7 pm"}
    - slot{"time2": "scott\twednesday\t1 - 3 pm"}
    - slot{"time3": "scott\tthursday\t7 - 9 am"}
    - utter_ask_time
* log_complain{"date": "tuesday", "timeslots": "5 - 7pm"}
    - slot{"date": "tuesday"}
    - slot{"timeslots": "5 - 7pm"}
    - action_set_timeslots
    - slot{"time": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"timeslots": "5 - 7pm"}
    - slot{"requested_slot": "confirmcomplain"}
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates{"address": "9312 shub farm st . arvada , co"}
    - slot{"address": "9312 shub farm st . arvada , co"}
    - utter_ask_confirmcomplain
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates{"email": "pop@pop.com"}
    - slot{"email": "pop@pop.com"}
    - utter_ask_confirmcomplain
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_notupdates{"pincode": "785496"}
    - slot{"pincode": "785496"}
    - utter_cannot_change_pincode
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story -59000651762369938299
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "dhrt5660"}
    - slot{"serialnumber": "dhrt5660"}
    - action_get_complaint_detail
    - slot{"modelnumber": "gdf650smjes"}
    - slot{"appliance": "dishwasher"}
    - slot{"serialnumber": "dhrt5660"}
    - slot{"requested_slot": "issue"}
* log_complain{"appliance": "dishwasher", "issue": "noisy"}
    - slot{"appliance": "dishwasher"}
    - slot{"issue": "noisy"}
    - action_get_complaint_detail
    - slot{"appliance": "dishwasher"}
    - slot{"issue": "noisy"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "robert"}
    - slot{"name": "robert"}
    - action_get_complaint_detail
    - slot{"name": "robert"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "robert@robertgmail.com"}
    - slot{"email": "robert@robertgmail.com"}
    - action_get_complaint_detail
    - slot{"email": "robert@robertgmail.com"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "1234567890"}
    - slot{"phonenumber": "1234567890"}
    - action_get_complaint_detail
    - slot{"phonenumber": "1234567890"}
    - slot{"requested_slot": "address"}
    - action_get_geo_location
    - action_get_complaint_detail
    - slot{"phonenumber": "1234567890"}
    - slot{"requested_slot": "address"}
* log_complain{"address": "8294 surrey street bonita springs , fl", "pincode": "34135"}
    - slot{"address": "8294 surrey street bonita springs , fl"}
    - slot{"pincode": "34135"}
    - action_get_complaint_detail
    - slot{"address": "8294 surrey street bonita springs , fl"}
    - slot{"pincode": "34135"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "scott\ttuesday\t5 - 7 pm"}
    - slot{"time2": "scott\twednesday\t1 - 3 pm"}
    - slot{"time3": "scott\tthursday\t7 - 9 am"}
    - utter_ask_time
* log_complain{"date": "tuesday", "timeslots": "5 - 7pm"}
    - slot{"date": "tuesday"}
    - slot{"timeslots": "5 - 7pm"}
    - action_set_timeslots
    - slot{"time": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"timeslots": "5 - 7pm"}
    - slot{"requested_slot": "confirmcomplain"}
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates{"name": "robert"}
    - slot{"name": "robert"}
    - utter_ask_confirmcomplain
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* service_modify_timeslots{"timeslots": "5 - 7pm"}
    - slot{"timeslots": "5 - 7pm"}
    - utter_cannot_change_timeslots
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_notupdates{"pincode": "785496"}
    - slot{"pincode": "785496"}
    - utter_cannot_change_pincode
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story 8504010697238780867
* service_query_timeslots
    - utter_ask_trackid
* service_detail{"trackid": "tr70320"}
    - slot{"trackid": "tr70320"}
    - action_query_timeslots_detail
    - utter_ask_take_to_homepage
* deny
    - utter_ask_more_query
* service_query_time
    - action_query_time_detail
    - utter_ask_take_to_homepage
* deny
    - utter_ask_more_query
* service_query
    - action_query_detail
    - slot{"trackid": null}
    - utter_youarewelcome
    - action_restart

## Generated Story 8739192303390817741
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "aczn9002"}
    - slot{"serialnumber": "aczn9002"}
    - action_get_complaint_detail
    - slot{"modelnumber": "aee24dt"}
    - slot{"appliance": "air conditioner"}
    - slot{"serialnumber": "aczn9002"}
    - slot{"requested_slot": "issue"}
* log_complain{"appliance": "air conditioner", "issue": "not cooling"}
    - slot{"appliance": "air conditioner"}
    - slot{"issue": "not cooling"}
    - action_get_complaint_detail
    - slot{"appliance": "air conditioner"}
    - slot{"issue": "not cooling"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "dev@dev.com"}
    - slot{"email": "dev@dev.com"}
    - action_get_complaint_detail
    - slot{"email": "dev@dev.com"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "8754963278"}
    - slot{"phonenumber": "8754963278"}
    - action_get_complaint_detail
    - slot{"phonenumber": "8754963278"}
    - slot{"requested_slot": "address"}
    - action_get_geo_location
    - action_get_complaint_detail
    - slot{"phonenumber": "8754963278"}
    - slot{"requested_slot": "address"}
* log_complain{"address": "574 new london turnpike norwich ct", "pincode": "06360"}
    - slot{"address": "574 new london turnpike norwich ct"}
    - slot{"pincode": "06360"}
    - action_get_complaint_detail
    - slot{"address": "574 new london turnpike norwich ct"}
    - slot{"pincode": "06360"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "scott\ttuesday\t7 - 10 am"}
    - slot{"time2": "scott\twednesday\t9 - 12 am"}
    - slot{"time3": "scott\tthursday\t7 - 10 pm"}
    - utter_ask_time
* log_complain{"date": "wednesday", "timeslots": "9 - 12am"}
    - slot{"date": "wednesday"}
    - slot{"timeslots": "9 - 12am"}
    - action_set_timeslots
    - slot{"time": null}
    - action_get_complaint_detail
    - slot{"date": "wednesday"}
    - slot{"timeslots": "9 - 12am"}
    - slot{"requested_slot": "confirmcomplain"}
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates{"phonenumber": "7845968596"}
    - slot{"phonenumber": "7845968596"}
    - utter_ask_confirmcomplain
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* service_modify_timeslots{"timeslots": "7 - 10 pm"}
    - slot{"timeslots": "7 - 10 pm"}
    - utter_cannot_change_timeslots
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates
    - utter_ask_change_entity
* log_complain{"email": "warner@gma.com"}
    - slot{"email": "warner@gma.com"}
    - utter_ask_confirmcomplain
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* service_modify_time
    - utter_cannot_change_time
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates{"address": "104 thomaston road preston ct"}
    - slot{"address": "104 thomaston road preston ct"}
    - utter_ask_confirmcomplain
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR14082"}
    - slot{"technician": null}
    - slot{"time": null}
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## Generated Story 87391923033965717741
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "aczn9002"}
    - slot{"serialnumber": "aczn9002"}
    - action_get_complaint_detail
    - slot{"modelnumber": "aee24dt"}
    - slot{"appliance": "air conditioner"}
    - slot{"serialnumber": "aczn9002"}
    - slot{"requested_slot": "issue"}
* log_complain{"appliance": "air conditioner", "issue": "not cooling"}
    - slot{"appliance": "air conditioner"}
    - slot{"issue": "not cooling"}
    - action_get_complaint_detail
    - slot{"appliance": "air conditioner"}
    - slot{"issue": "not cooling"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "dev@dev.com"}
    - slot{"email": "dev@dev.com"}
    - action_get_complaint_detail
    - slot{"email": "dev@dev.com"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "8754963278"}
    - slot{"phonenumber": "8754963278"}
    - action_get_complaint_detail
    - slot{"phonenumber": "8754963278"}
    - slot{"requested_slot": "address"}
    - action_get_geo_location
    - action_get_complaint_detail
    - slot{"phonenumber": "8754963278"}
    - slot{"requested_slot": "address"}
* log_complain{"address": "574 new london turnpike norwich ct", "pincode": "06360"}
    - slot{"address": "574 new london turnpike norwich ct"}
    - slot{"pincode": "06360"}
    - action_get_complaint_detail
    - slot{"address": "574 new london turnpike norwich ct"}
    - slot{"pincode": "06360"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "scott\ttuesday\t7 - 10 am"}
    - slot{"time2": "scott\twednesday\t9 - 12 am"}
    - slot{"time3": "scott\tthursday\t7 - 10 pm"}
    - utter_ask_time
* log_complain{"date": "wednesday", "timeslots": "9 - 12am"}
    - slot{"date": "wednesday"}
    - slot{"timeslots": "9 - 12am"}
    - action_set_timeslots
    - slot{"time": null}
    - action_get_complaint_detail
    - slot{"date": "wednesday"}
    - slot{"timeslots": "9 - 12am"}
    - slot{"requested_slot": "confirmcomplain"}
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates
  - utter_ask_change_entity
* log_complain{"phonenumber": "7845968596"}
    - slot{"phonenumber": "7845968596"}
    - utter_ask_confirmcomplain
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* service_modify_timeslots
    - utter_cannot_change_timeslots
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates{"email": "warner@gma.com"}
    - slot{"email": "warner@gma.com"}
    - utter_ask_confirmcomplain
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* service_modify_time
    - utter_cannot_change_time
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates{"address": "104 thomaston road preston ct"}
    - slot{"address": "104 thomaston road preston ct"}
    - utter_ask_confirmcomplain
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR14082"}
    - slot{"technician": null}
    - slot{"time": null}
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## Generated Story -2071334921477652906
* service_query
    - utter_ask_trackid
* service_detail{"trackid": "tr14082"}
    - slot{"trackid": "tr14082"}
    - action_query_detail
    - slot{"trackid": null}
    - utter_youarewelcome
    - action_restart

## Generated Story 7322435454655094750
* service_query_timeslots{"trackid": "tr14082"}
    - slot{"trackid": "tr14082"}
    - action_query_timeslots_detail
    - utter_ask_take_to_homepage
* deny
    - utter_ask_more_query
* service_query_time
    - action_query_time_detail
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story -5680008432225279254
* service_query_time
    - utter_ask_trackid
* service_detail{"trackid": "tr59159"}
    - slot{"trackid": "tr59159"}
    - action_query_time_detail
    - utter_ask_take_to_homepage
* deny
    - utter_ask_more_query
* service_query_timeslots
    - action_query_timeslots_detail
    - utter_ask_take_to_homepage
* deny
    - utter_ask_more_query
* service_query
    - action_query_time_detail
    - utter_youarewelcome
    - action_restart

## Generated Story 5062373256352525271
* service_query_timeslots
    - utter_ask_trackid
* service_detail{"trackid": "tr59159"}
    - slot{"trackid": "tr59159"}
    - action_query_timeslots_detail
    - utter_ask_take_to_homepage
* deny
    - utter_ask_more_query
* service_query_time
    - action_query_time_detail
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story -8368993236577954735
* service_query{"trackid": "tr59159"}
    - slot{"trackid": "tr59159"}
    - action_query_detail
    - slot{"trackid": null}
    - utter_youarewelcome
    - action_restart

## Generated Story -3724086228549891504
* service_query_timeslots{"trackid": "tr59159"}
    - slot{"trackid": "tr59159"}
    - action_query_timeslots_detail
    - utter_ask_take_to_homepage
* deny
    - utter_ask_more_query
* service_query_time
    - action_query_time_detail
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Story 300
* greet
    - utter_greet
* service_query
    - utter_ask_trackid
* service_detail{"trackid": "tr14082"}
    - slot{"trackid": "tr14082"}
    - action_query_detail
    - slot{"trackid": null}
    - utter_youarewelcome
    - action_restart

## Story 301
* greet
    - utter_greet
* service_query_timeslots{"trackid": "tr14082"}
    - slot{"trackid": "tr14082"}
    - action_query_timeslots_detail
    - utter_ask_take_to_homepage
* deny
    - utter_ask_more_query
* service_query_time
    - action_query_time_detail
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Story 302
* greet
    - utter_greet
* service_query_time
    - utter_ask_trackid
* service_detail{"trackid": "tr59159"}
    - slot{"trackid": "tr59159"}
    - action_query_time_detail
    - utter_ask_take_to_homepage
* deny
    - utter_ask_more_query
* service_query_timeslots
    - action_query_timeslots_detail
    - utter_ask_take_to_homepage
* deny
    - utter_ask_more_query
* service_query
    - action_query_time_detail
    - utter_youarewelcome
    - action_restart

## Story 303
* greet
    - utter_greet
* service_query_timeslots
    - utter_ask_trackid
* service_detail{"trackid": "tr59159"}
    - slot{"trackid": "tr59159"}
    - action_query_timeslots_detail
    - utter_ask_take_to_homepage
* deny
    - utter_ask_more_query
* service_query_time
    - action_query_time_detail
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Story 304
* greet
    - utter_greet
* service_query{"trackid": "tr59159"}
    - slot{"trackid": "tr59159"}
    - action_query_detail
    - slot{"trackid": null}
    - utter_youarewelcome
    - action_restart

## Story 305
* greet
    - utter_greet
* service_query_timeslots{"trackid": "tr59159"}
    - slot{"trackid": "tr59159"}
    - action_query_timeslots_detail
    - utter_ask_take_to_homepage
* deny
    - utter_ask_more_query
* service_query_time
    - action_query_time_detail
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Story 306
* greet
    - utter_greet
* service_query_time
    - utter_ask_trackid
* service_detail{"trackid": "tr59159"}
    - slot{"trackid": "tr59159"}
    - action_query_time_detail
    - utter_ask_take_to_homepage
* deny
    - utter_ask_more_query
* service_query_timeslots
    - action_query_timeslots_detail
    - utter_ask_take_to_homepage
* deny
    - utter_ask_more_query
* service_query
    - action_query_detail
    - slot{"trackid": null}
    - utter_youarewelcome
    - action_restart

## Generated Story 1026384420919559016
* greet
    - utter_greet
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "DRBG0110"}
    - slot{"serialnumber": "DRBG0110"}
    - action_get_complaint_detail
    - slot{"modelnumber": "gfd48esskww"}
    - slot{"appliance": "dryer"}
    - slot{"serialnumber": "DRBG0110"}
    - slot{"requested_slot": "issue"}
* log_complain{"appliance": "dryer", "issue": "not working"}
    - slot{"appliance": "dryer"}
    - slot{"issue": "not working"}
    - action_get_complaint_detail
    - slot{"appliance": "dryer"}
    - slot{"issue": "not working"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "emma"}
    - slot{"name": "emma"}
    - action_get_complaint_detail
    - slot{"name": "emma"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "emma@gma.com"}
    - slot{"email": "emma@gma.com"}
    - action_get_complaint_detail
    - slot{"email": "emma@gma.com"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "9708518476"}
    - slot{"phonenumber": "9708518476"}
    - action_get_complaint_detail
    - slot{"phonenumber": "9708518476"}
    - slot{"requested_slot": "address"}
    - action_get_geo_location
    - action_get_complaint_detail
    - slot{"phonenumber": "9708518476"}
    - slot{"requested_slot": "address"}
* log_complain{"address": "33 paula lane uncasville ct", "pincode": "06385"}
    - slot{"address": "33 paula lane uncasville ct"}
    - slot{"pincode": "06385"}
    - action_get_complaint_detail
    - slot{"address": "33 paula lane uncasville ct"}
    - slot{"pincode": "06385"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "scott\ttuesday\t5 - 6 pm"}
    - slot{"time2": "scott\twednesday\t9 - 10 am"}
    - slot{"time3": "scott\tthursday\t6 - 7 pm"}
    - utter_ask_time
* log_complain{"date": "tuesday", "timeslots": "6 - 7 pm"}
    - slot{"date": "tuesday"}
    - slot{"timeslots": "6 - 7 pm"}
    - action_set_timeslots
    - slot{"time": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"timeslots": "6 - 7 pm"}
    - slot{"requested_slot": "confirmcomplain"}
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates
    - utter_ask_change_entity
* log_complain{"name": "linda"}
    - slot{"name": "linda"}
    - utter_ask_confirmcomplain
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates
    - utter_ask_change_entity
* log_complain{"phonenumber": "8759645125"}
    - slot{"phonenumber": "8759645125"}
    - utter_ask_confirmcomplain
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates
    - utter_ask_change_entity
* log_complain{"email": "let@lemgmail.com"}
    - slot{"email": "let@lemgmail.com"}
    - utter_ask_confirmcomplain
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* service_modify_time
    - utter_cannot_change_time
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates
    - utter_ask_change_entity
* log_complain{"name": "emma"}
    - slot{"name": "emma"}
    - utter_ask_confirmcomplain
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR56886"}
    - slot{"technician": null}
    - slot{"time": null}
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## Generated Story 411451341000705178
* service_query_time{"trackid": "tr56886"}
    - slot{"trackid": "tr56886"}
    - action_query_time_detail
    - utter_ask_take_to_homepage
* deny
    - utter_ask_more_query
* service_query_timeslots
    - action_query_timeslots_detail
    - utter_ask_take_to_homepage
* deny
    - utter_ask_more_query
* service_query
    - action_query_detail
    - slot{"trackid": null}
    - utter_youarewelcome
    - action_restart
## Generated Story -4423545020723850
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "DRBG0119"}
    - slot{"serialnumber": "DRBG0119"}
    - action_get_complaint_detail
    - slot{"modelnumber": "gtd75ecslws"}
    - slot{"appliance": "dryer"}
    - slot{"serialnumber": "DRBG0119"}
    - slot{"requested_slot": "issue"}
* log_complain{"issue": "buttons do not work"}
    - slot{"issue": "buttons do not work"}
    - action_get_complaint_detail
    - slot{"issue": "buttons do not work"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "emma"}
    - slot{"name": "emma"}
    - action_get_complaint_detail
    - slot{"name": "emma"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "em@gma.com"}
    - slot{"email": "em@gma.com"}
    - action_get_complaint_detail
    - slot{"email": "em@gma.com"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "8294295135"}
    - slot{"phonenumber": "8294295135"}
    - action_get_complaint_detail
    - slot{"phonenumber": "8294295135"}
    - slot{"requested_slot": "address"}
    - action_get_geo_location
    - action_get_complaint_detail
    - slot{"phonenumber": "8294295135"}
    - slot{"requested_slot": "address"}
* log_complain{"address": "132 , my street , kingston , new york   united states", "pincode": "12401"}
    - slot{"address": "132 , my street , kingston , new york   united states"}
    - slot{"pincode": "12401"}
    - action_get_complaint_detail
    - slot{"address": "132 , my street , kingston , new york   united states"}
    - slot{"pincode": "12401"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "scott\ttuesday\t9 - 10 am"}
    - slot{"time2": "scott\twednesday\t8 - 9 am"}
    - slot{"time3": "scott\tthursday\t9 - 10 am"}
    - utter_ask_time
* log_complain{"date": "wednesday", "timeslots": "9 - 10 am"}
    - slot{"date": "wednesday"}
    - slot{"timeslots": "9 - 10 am"}
    - action_set_timeslots
    - slot{"time": null}
    - action_get_complaint_detail
    - slot{"date": "wednesday"}
    - slot{"timeslots": "9 - 10 am"}
    - slot{"requested_slot": "confirmcomplain"}
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_notupdates
    - utter_cannot_change_pincode
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* service_modify_timeslots
    - utter_cannot_change_timeslots
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates
    - utter_ask_change_entity
* log_complain{"email": "letmebe.asmita@gmail.com"}
    - slot{"email": "letmebe.asmita@gmail.com"}
    - utter_ask_confirmcomplain
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates
    - utter_ask_change_entity
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - utter_ask_confirmcomplain
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart
    
## Generated Story 1345795411873987434
* greet
    - utter_greet
* service_modify
    - utter_ask_trackid
* service_detail{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_what_to_modify
* service_modify_time
    - utter_ask_modify_time_confirm
* affirm
    - action_complain_modify_get_time
    - slot{"time1": "larry\ttuesday\t7 - 10 am"}
    - slot{"time2": "scott\tthursday\t7 - 10 am"}
    - slot{"time3": "scott\tfriday\t9 - 12 am"}
    - utter_ask_time
* log_complain{"date": "friday", "timeslots": "9 - 12 am"}
    - slot{"date": "friday"}
    - slot{"timeslots": "9 - 12 am"}
    - action_complain_modify_set_time
    - slot{"time": null}
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "9 - 12 am"}
    - slot{"time2": "8 - 11 am"}
    - slot{"time3": "5 - 8 pm"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "8 - 11 am"}
    - slot{"timeslots": "8 - 11 am"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_time
    - utter_ask_modify_time_confirm
* affirm
    - action_complain_modify_get_time
    - slot{"time1": "larry\ttuesday\t5 - 8 pm"}
    - slot{"time2": "larry\twednesday\t3 - 6 pm"}
    - slot{"time3": "scott\tthursday\t5 - 8 pm"}
    - utter_ask_time
* log_complain{"date": "thursday", "timeslots": "5 - 8 pm"}
    - slot{"date": "thursday"}
    - slot{"timeslots": "5 - 8 pm"}
    - action_complain_modify_set_time
    - slot{"time": null}
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story -59986106139642475
* service_modify_time
    - utter_ask_trackid
* service_detail{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_modify_time_confirm
* affirm
    - action_complain_modify_get_time
    - slot{"time1": "larry\ttuesday\t7 - 10 am"}
    - slot{"time2": "larry\twednesday\t8 - 11 am"}
    - slot{"time3": "larry\tfriday\t6 - 9 pm"}
    - utter_ask_time
* log_complain{"date": "wednesday", "timeslots": "8 - 11 am"}
    - slot{"date": "wednesday"}
    - slot{"timeslots": "8 - 11 am"}
    - action_complain_modify_set_time
    - slot{"time": null}
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story 3119121034525452737
* service_modify{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_what_to_modify
* service_modify_time
    - utter_ask_modify_time_confirm
* affirm
    - action_complain_modify_get_time
    - slot{"time1": "larry\ttuesday\t8 - 11 am"}
    - slot{"time2": "larry\tthursday\t7 - 10 am"}
    - slot{"time3": "larry\tfriday\t7 - 10 am"}
    - utter_ask_time
* log_complain{"date": "tuesday", "timeslots": "8 - 11 am"}
    - slot{"date": "tuesday"}
    - slot{"timeslots": "8 - 11 am"}
    - action_complain_modify_set_time
    - slot{"time": null}
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "2 - 5 pm"}
    - slot{"time2": "7 - 10 am"}
    - slot{"time3": "3 - 6 pm"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "7 - 10 am"}
    - slot{"timeslots": "7 - 10 am"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_time
    - utter_ask_modify_time_confirm
* deny
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story 3901267614806205793
* service_modify_time{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_modify_time_confirm
* affirm
    - action_complain_modify_get_time
    - slot{"time1": "tim\twednesday\t2 - 5 pm"}
    - slot{"time2": "larry\tthursday\t7 - 10 am"}
    - slot{"time3": "larry\tfriday\t7 - 10 am"}
    - utter_ask_time
* log_complain{"date": "thursday", "timeslots": "7 - 10 am"}
    - slot{"date": "thursday"}
    - slot{"timeslots": "7 - 10 am"}
    - action_complain_modify_set_time
    - slot{"time": null}
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story -5486825631731423975
* service_modify_timeslots{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_complain_modify_check_track_id
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "9 - 12 am"}
    - slot{"time2": "9 - 12 am"}
    - slot{"time3": "3 - 6 pm"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "9 - 12 am"}
    - slot{"timeslots": "9 - 12 am"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_time
    - utter_ask_modify_time_confirm
* affirm
    - action_complain_modify_get_time
    - slot{"time1": "larry\tmonday\t7 - 10 pm"}
    - slot{"time2": "tim\ttuesday\t8 - 11 am"}
    - slot{"time3": "tim\twednesday\t1 - 4 pm"}
    - utter_ask_time
* log_complain{"date": "wednesday", "timeslots": "1 - 4 pm"}
    - slot{"date": "wednesday"}
    - slot{"timeslots": "1 - 4 pm"}
    - action_complain_modify_set_time
    - slot{"time": null}
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story 4486674973035060790
* greet
    - utter_greet
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "rfaz3347"}
    - slot{"serialnumber": "rfaz3347"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"appliance": "refrigerator"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"requested_slot": "issue"}
* log_complain{"issue": "not working"}
    - slot{"issue": "not working"}
    - action_get_complaint_detail
    - slot{"issue": "not working"}
    - slot{"requested_slot": "name"}
* log_complain{"email": "akash.chandra8d@gmail.com", "phonenumber": "8250599363"}
    - slot{"email": "akash.chandra8d@gmail.com"}
    - slot{"phonenumber": "8250599363"}
    - action_get_complaint_detail
    - slot{"email": "akash.chandra8d@gmail.com"}
    - slot{"phonenumber": "8250599363"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "address"}
    - action_get_geo_location
    - slot{"address": "Kharagpur Paschim Medinipur West Bengal 721301 "}
    - slot{"pincode": "721301"}
    - utter_ask_confirm_address
* deny
    - action_set_geo_location
    - slot{"address": null}
    - slot{"pincode": null}
    - action_get_complaint_detail
    - slot{"requested_slot": "address"}
* log_complain{"address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - action_get_complaint_detail
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "larry\tmonday\t7 - 10 am"}
    - slot{"time2": "tim\ttuesday\t4 - 7 pm"}
    - slot{"time3": "larry\tthursday\t5 - 8 pm"}
    - utter_ask_time
* log_complain{"date": "tuesday", "timeslots": "4 - 7 pm"}
    - slot{"date": "tuesday"}
    - slot{"timeslots": "4 - 7 pm"}
    - action_set_timeslots
    - slot{"time": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"timeslots": "4 - 7 pm"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR33838"}
    - slot{"technician": "tim"}
    - slot{"time": null}
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## Generated Story -4780789759003665707
* greet
    - utter_greet
* log_complain{"appliance": "refrigerator", "issue": "broken"}
    - slot{"appliance": "refrigerator"}
    - slot{"issue": "broken"}
    - action_get_complaint_detail
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "rfaz3347"}
    - slot{"serialnumber": "rfaz3347"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"requested_slot": "name"}
* log_complain{"email": "akash.chandra8d@gmail.com", "phonenumber": "8250599363"}
    - slot{"email": "akash.chandra8d@gmail.com"}
    - slot{"phonenumber": "8250599363"}
    - action_get_complaint_detail
    - slot{"email": "akash.chandra8d@gmail.com"}
    - slot{"phonenumber": "8250599363"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "address"}
    - action_get_geo_location
    - slot{"address": "Kharagpur Paschim Medinipur West Bengal 721301 "}
    - slot{"pincode": "721301"}
    - utter_ask_confirm_address
* deny
    - action_set_geo_location
    - slot{"address": null}
    - slot{"pincode": null}
    - action_get_complaint_detail
    - slot{"requested_slot": "address"}
* log_complain{"address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - action_get_complaint_detail
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "tim\tmonday\t4 - 7 pm"}
    - slot{"time2": "larry\tthursday\t8 - 11 am"}
    - slot{"time3": "scott\tfriday\t2 - 5 pm"}
    - utter_ask_time
* log_complain{"date": "monday", "timeslots": "4 - 7 pm"}
    - slot{"date": "monday"}
    - slot{"timeslots": "4 - 7 pm"}
    - action_set_timeslots
    - slot{"time": null}
    - action_get_complaint_detail
    - slot{"date": "monday"}
    - slot{"timeslots": "4 - 7 pm"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR39567"}
    - slot{"technician": "tim"}
    - slot{"time": null}
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## Generated Story -4423545020723850
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "DRBG0119"}
    - slot{"serialnumber": "DRBG0119"}
    - action_get_complaint_detail
    - slot{"modelnumber": "gtd75ecslws"}
    - slot{"appliance": "dryer"}
    - slot{"serialnumber": "DRBG0119"}
    - slot{"requested_slot": "issue"}
* log_complain{"issue": "buttons do not work"}
    - slot{"issue": "buttons do not work"}
    - action_get_complaint_detail
    - slot{"issue": "buttons do not work"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "emma"}
    - slot{"name": "emma"}
    - action_get_complaint_detail
    - slot{"name": "emma"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "em@gma.com"}
    - slot{"email": "em@gma.com"}
    - action_get_complaint_detail
    - slot{"email": "em@gma.com"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "8294295135"}
    - slot{"phonenumber": "8294295135"}
    - action_get_complaint_detail
    - slot{"phonenumber": "8294295135"}
    - slot{"requested_slot": "address"}
    - action_get_geo_location
    - action_get_complaint_detail
    - slot{"phonenumber": "8294295135"}
    - slot{"requested_slot": "address"}
* log_complain{"address": "132 , my street , kingston , new york   united states", "pincode": "12401"}
    - slot{"address": "132 , my street , kingston , new york   united states"}
    - slot{"pincode": "12401"}
    - action_get_complaint_detail
    - slot{"address": "132 , my street , kingston , new york   united states"}
    - slot{"pincode": "12401"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "scott\ttuesday\t9 - 10 am"}
    - slot{"time2": "scott\twednesday\t8 - 9 am"}
    - slot{"time3": "scott\tthursday\t9 - 10 am"}
    - utter_ask_time
* log_complain{"date": "wednesday", "timeslots": "9 - 10 am"}
    - slot{"date": "wednesday"}
    - slot{"timeslots": "9 - 10 am"}
    - action_set_timeslots
    - slot{"time": null}
    - action_get_complaint_detail
    - slot{"date": "wednesday"}
    - slot{"timeslots": "9 - 10 am"}
    - slot{"requested_slot": "confirmcomplain"}
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_notupdates
    - utter_cannot_change_pincode
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* service_modify_timeslots
    - utter_cannot_change_timeslots
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates
    - utter_ask_change_entity
* log_complain{"email": "letmebe.asmita@gmail.com"}
    - slot{"email": "letmebe.asmita@gmail.com"}
    - utter_ask_confirmcomplain
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates
    - utter_ask_change_entity
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - utter_ask_confirmcomplain
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart
    
## Generated Story -7710418812771126863
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "drbg0107"}
    - slot{"serialnumber": "drbg0107"}
    - action_get_complaint_detail
    - slot{"modelnumber": "gfd48esskww"}
    - slot{"appliance": "dryer"}
    - slot{"serialnumber": "drbg0107"}
    - slot{"requested_slot": "issue"}
* log_complain{"issue": "noisy"}
    - slot{"issue": "noisy"}
    - action_get_complaint_detail
    - slot{"issue": "noisy"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "dev@gmail.com"}
    - slot{"email": "dev@gmail.com"}
    - action_get_complaint_detail
    - slot{"email": "dev@gmail.com"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "8294295135"}
    - slot{"phonenumber": "8294295135"}
    - action_get_complaint_detail
    - slot{"phonenumber": "8294295135"}
    - slot{"requested_slot": "address"}
    - action_get_geo_location
    - slot{"address": "Ranchi Ranchi Ranchi Jharkhand 834006 "}
    - slot{"pincode": "834006"}
    - utter_ask_confirm_address
* deny
    - action_set_geo_location
    - action_get_complaint_detail
    - slot{"requested_slot": "date"}
* log_complain{"address": "132 , my street , kingston , new york   united states", "pincode": "12401"}
    - slot{"address": "132 , my street , kingston , new york   united states"}
    - slot{"pincode": "12401"}
    - action_get_complaint_detail
    - slot{"address": "132 , my street , kingston , new york   united states"}
    - slot{"pincode": "12401"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "scott\ttuesday\t8 - 9 am"}
    - slot{"time2": "scott\twednesday\t6 - 7 pm"}
    - slot{"time3": "scott\tthursday\t3 - 4 pm"}
    - utter_ask_time
* log_complain{"date": "wednesday", "timeslots": "8 - 9 am"}
    - slot{"date": "wednesday"}
    - slot{"timeslots": "8 - 9 am"}
    - action_set_timeslots
    - slot{"time": null}
    - action_get_complaint_detail
    - slot{"date": "wednesday"}
    - slot{"timeslots": "8 - 9 am"}
    - slot{"requested_slot": "confirmcomplain"}
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_notupdates{"pincode": "567467"}
    - slot{"pincode": "567467"}
    - utter_cannot_change_pincode
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates
    - utter_ask_change_entity
* log_complain{"email": "letmebe.asmita@gmail.com"}
    - slot{"email": "letmebe.asmita@gmail.com"}
    - utter_ask_confirmcomplain
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* service_modify_time{"date": "wednesday"}
    - slot{"date": "wednesday"}
    - utter_cannot_change_time
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates
    - utter_ask_change_entity
* log_complain{"phonenumber": "9708518476"}
    - slot{"phonenumber": "9708518476"}
    - utter_ask_confirmcomplain
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates
    - utter_ask_change_entity
* log_complain{"address": "3 cardinal drive groton ct"}
    - slot{"address": "3 cardinal drive groton ct"}
    - utter_ask_confirmcomplain
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR99716"}
    - slot{"technician": null}
    - slot{"time": null}
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## Generated Story -77104112771126863
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "drbg0107"}
    - slot{"serialnumber": "drbg0107"}
    - action_get_complaint_detail
    - slot{"modelnumber": "gfd48esskww"}
    - slot{"appliance": "dryer"}
    - slot{"serialnumber": "drbg0107"}
    - slot{"requested_slot": "issue"}
* log_complain{"issue": "noisy"}
    - slot{"issue": "noisy"}
    - action_get_complaint_detail
    - slot{"issue": "noisy"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "dev@gmail.com"}
    - slot{"email": "dev@gmail.com"}
    - action_get_complaint_detail
    - slot{"email": "dev@gmail.com"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "8294295135"}
    - slot{"phonenumber": "8294295135"}
    - action_get_complaint_detail
    - slot{"phonenumber": "8294295135"}
    - slot{"requested_slot": "address"}
    - action_get_geo_location
    - slot{"address": "Ranchi Ranchi Ranchi Jharkhand 834006 "}
    - slot{"pincode": "834006"}
    - utter_ask_confirm_address
* deny
    - action_set_geo_location
    - action_get_complaint_detail
    - slot{"requested_slot": "date"}
* log_complain{"address": "132 , my street , kingston , new york   united states", "pincode": "12401"}
    - slot{"address": "132 , my street , kingston , new york   united states"}
    - slot{"pincode": "12401"}
    - action_get_complaint_detail
    - slot{"address": "132 , my street , kingston , new york   united states"}
    - slot{"pincode": "12401"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "scott\ttuesday\t8 - 9 am"}
    - slot{"time2": "scott\twednesday\t6 - 7 pm"}
    - slot{"time3": "scott\tthursday\t3 - 4 pm"}
    - utter_ask_time
* log_complain{"date": "wednesday", "timeslots": "8 - 9 am"}
    - slot{"date": "wednesday"}
    - slot{"timeslots": "8 - 9 am"}
    - action_set_timeslots
    - slot{"time": null}
    - action_get_complaint_detail
    - slot{"date": "wednesday"}
    - slot{"timeslots": "8 - 9 am"}
    - slot{"requested_slot": "confirmcomplain"}
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* service_modify_time{"date": "wednesday"}
    - slot{"date": "wednesday"}
    - utter_cannot_change_time
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_notupdates{"pincode": "567467"}
    - slot{"pincode": "567467"}
    - utter_cannot_change_pincode
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates
    - utter_ask_change_entity
* log_complain{"email": "letmebe.asmita@gmail.com"}
    - slot{"email": "letmebe.asmita@gmail.com"}
    - utter_ask_confirmcomplain
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* service_modify_time{"date": "wednesday"}
    - slot{"date": "wednesday"}
    - utter_cannot_change_time
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates
    - utter_ask_change_entity
* log_complain{"phonenumber": "9708518476"}
    - slot{"phonenumber": "9708518476"}
    - utter_ask_confirmcomplain
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* service_modify_timeslots
    - utter_cannot_change_timeslots
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates
    - utter_ask_change_entity
* log_complain{"address": "3 cardinal drive groton ct"}
    - slot{"address": "3 cardinal drive groton ct"}
    - utter_ask_confirmcomplain
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR99716"}
    - slot{"technician": null}
    - slot{"time": null}
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## Generated Story -204183084943054890
* greet
    - utter_greet
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "drbg0109"}
    - slot{"serialnumber": "drbg0109"}
    - action_get_complaint_detail
    - slot{"modelnumber": "gfd48esskww"}
    - slot{"appliance": "dryer"}
    - slot{"serialnumber": "drbg0109"}
    - slot{"requested_slot": "issue"}
* log_complain{"appliance": "air conditioner", "issue": "button do not work"}
    - slot{"appliance": "air conditioner"}
    - slot{"issue": "button do not work"}
    - action_get_complaint_detail
    - slot{"appliance": null}
    - slot{"issue": "button do not work"}
    - slot{"requested_slot": "appliance"}
* log_complain{"appliance": "dryer"}
    - slot{"appliance": "dryer"}
    - action_get_complaint_detail
    - slot{"appliance": "dryer"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "dev@gmail.com"}
    - slot{"email": "dev@gmail.com"}
    - action_get_complaint_detail
    - slot{"email": "dev@gmail.com"}
    - slot{"requested_slot": "phonenumber"}
* log_complain{"phonenumber": "8294295135"}
    - slot{"phonenumber": "8294295135"}
    - action_get_complaint_detail
    - slot{"phonenumber": "8294295135"}
    - slot{"requested_slot": "address"}
    - action_get_geo_location
    - action_get_complaint_detail
    - slot{"phonenumber": "8294295135"}
    - slot{"requested_slot": "address"}
* log_complain{"address": "50 water street mystic ct", "pincode": "06355"}
    - slot{"address": "50 water street mystic ct"}
    - slot{"pincode": "06355"}
    - action_get_complaint_detail
    - slot{"address": "50 water street mystic ct"}
    - slot{"pincode": "06355"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "scott\ttuesday\t8 - 9 am"}
    - slot{"time2": "scott\twednesday\t6 - 7 pm"}
    - slot{"time3": "scott\tthursday\t5 - 6 pm"}
    - utter_ask_time
* log_complain{"date": "wednesday", "timeslots": "8 - 9 am"}
    - slot{"date": "wednesday"}
    - slot{"timeslots": "8 - 9 am"}
    - action_set_timeslots
    - slot{"time": null}
    - action_get_complaint_detail
    - slot{"date": "wednesday"}
    - slot{"timeslots": "8 - 9 am"}
    - slot{"requested_slot": "confirmcomplain"}
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_notupdates{"pincode": "06353"}
    - slot{"pincode": "06353"}
    - utter_cannot_change_pincode
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* service_modify_timeslots
    - utter_cannot_change_timeslots
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates{"email": "letmebe.asmita@gmail.com"}
    - slot{"email": "letmebe.asmita@gmail.com"}
    - utter_ask_confirmcomplain
* deny
    - utter_notconfirmed
    - utter_ask_take_to_homepage
* deny
    - utter_ask_updates
* ask_updates
    - utter_ask_change_entity
* log_complain{"phonenumber": "9708518476"}
    - slot{"phonenumber": "9708518476"}
    - utter_ask_confirmcomplain
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR42593"}
    - slot{"technician": null}
    - slot{"time": null}
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## Generated Story -5455592899716019675
* service_query_time
    - utter_ask_trackid
* service_detail{"trackid": "tr42593"}
    - slot{"trackid": "tr42593"}
    - action_query_time_detail
    - utter_ask_take_to_homepage
* deny
    - utter_ask_more_query
* service_query_timeslots
    - action_query_timeslots_detail
    - utter_ask_take_to_homepage
* deny
    - utter_ask_more_query
* service_query
    - action_query_time_detail
    - utter_youarewelcome
    - action_restart

## Generated Story 1217119926007785341
* greet
    - utter_greet
* service_modify
    - utter_ask_trackid
* service_detail{"trackid": "tr42591"}
    - slot{"trackid": "tr42591"}
    - action_complain_modify_check_track_id
    - slot{"trackid": null}
    - utter_wrong_track_id
* service_detail{"trackid": "tr42593"}
    - slot{"trackid": "tr42593"}
    - action_complain_modify_check_track_id
    - utter_ask_what_to_modify
* service_modify_timeslots
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_get_timeslots
    - slot{"time1": "4 - 5 pm"}
    - slot{"time2": "9 - 10 am"}
    - slot{"time3": "6 - 7 pm"}
    - utter_ask_timeslot_change
* log_complain{"timeslots": "4 - 5 pm"}
    - slot{"timeslots": "4 - 5 pm"}
    - action_complain_modify_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - utter_ask_take_to_homepage
* deny
    - utter_ask_what_to_modify
* service_modify_time
    - utter_ask_modify_time_confirm
* affirm
    - action_complain_modify_get_time
    - utter_ask_time
* log_complain{"date": "wednesday", "timeslots": "5 - 9pm"}
    - slot{"date": "wednesday"}
    - slot{"timeslots": "5 - 9pm"}
    - action_complain_modify_set_time
    - utter_ask_take_to_homepage
* affirm
    - utter_youarewelcome
    - action_restart

## Generated Story 5360758895116014625
* service_modify_cancel{"trackid": "tr42593"}
    - slot{"trackid": "tr42593"}
    - utter_ask_cancel_complain_confirm
* affirm
    - action_cancel_complain
    - slot{"trackid": null}
    - utter_youarewelcome
    - action_restart